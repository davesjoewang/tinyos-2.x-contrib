/*
 * "Copyright (c) 2008 The Regents of the University  of California.
 * All rights reserved."
 *
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose, without fee, and without written agreement is
 * hereby granted, provided that the above copyright notice, the following
 * two paragraphs and the author appear in all copies of this software.
 *
 * IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR
 * DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT
 * OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF THE UNIVERSITY OF
 * CALIFORNIA HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * THE UNIVERSITY OF CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
 * AND FITNESS FOR A PARTICULAR PURPOSE.  THE SOFTWARE PROVIDED HEREUNDER IS
 * ON AN "AS IS" BASIS, AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATION TO
 * PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS."
 *
 */
/*
 * @author Stephen Dawson-Haggerty <stevedh@cs.berkeley.edu>
 */

#include <stdint.h>
#include <string.h>
#include <stdio.h>

#include "IP.h"

#include "6lowpan.h"
#include "lib6lowpan.h"
#include "lib6lowpanIP.h"
#include "lib6lowpanFrag.h"
#include "tunnel/IEEE154.h"

#define min(a,b) ( ((a)>(b)) ? (b) : (a) )
#define max(a,b) ( ((a)<(b)) ? (b) : (a) )

uint16_t frag_tag = 0;

void ip_memclr(uint8_t *buf, uint16_t len) {
  for (; len > 0; len--)
    *buf++ = 0;
  
}

void *ip_memcpy(void *dst0, const void *src0, size_t len) {
  uint8_t *dst = (uint8_t *) dst0;
  uint8_t *src = (uint8_t *) src0;
  void *ret = dst0;
  
  for (; len > 0; len--)
    *dst++ = *src++;
  
  return ret;
}

/*
 *  this function writes the next fragment which needs to be sent into
 *  the buffer passed in.  It updates the structures in process to
 *  reflect how much of the packet has been sent so far.
 *
 *  if the packet does not require fragmentation, this function will
 *  not insert a fragmentation header and will merely compress the
 *  headers into the packet.
 *
 *  returns the number of bytes used in buf, or zero if there was no
 *  fragment to be sent.
 *
 */
uint8_t getNextFrag(ip_msg_t *msg, fragment_t *progress,
                     uint8_t *buf, uint16_t len) {
  if (msg == NULL || progress == NULL || buf == NULL) return 0;
  packed_lowmsg_t pkt;
  uint16_t compressed_len;
  uint16_t frag_length = 0;
  pkt.headers = 0;
  pkt.data = buf;
  pkt.len = len;

  // if this is the first fragment, we will compress the headers in
  // the ip message, and only insert a fragmentation header if
  // necessary to pack it into buffer
  if (progress->offset == 0) {
    uint8_t compressed_headers[sizeof(struct ip6_hdr) + sizeof(struct udp_hdr)];
    uint16_t payload_remaining = ntoh16(msg->hdr.plen);
    uint8_t *payload;
    uint8_t header_len = 0;
    
    // pack the headers into a temporary buffer
    payload = packHeaders(msg, compressed_headers,
                          sizeof(compressed_headers));
    compressed_len = payload - compressed_headers;
    payload_remaining -= packs_header(msg);

    // printBuf(compressed_headers, compressed_len);
    // printf("payload: %p\n", payload);

    // maybe add a fragmentation header
    if (compressed_len + payload_remaining > len) {
      pkt.headers |= LOWMSG_FRAG1_HDR;
      if (setupHeaders(&pkt, pkt.headers)) goto fail;
      if (setFragDgramTag(&pkt, ++frag_tag)) goto fail;
      if (setFragDgramSize(&pkt, ntoh16(msg->hdr.plen) + sizeof(struct ip6_hdr))) goto fail;
      header_len = LOWMSG_FRAG1_LEN;
    } else {
      if (setupHeaders(&pkt, pkt.headers)) goto fail;
    }
    ip_memcpy(getLowpanPayload(&pkt), compressed_headers, compressed_len);
    
    /*
     * calculate how much to put into this fragment
     *
     * if the whole packet fits in the buffer, this is easy; it's the
     * compressed headers plus the payload length.
     *
     * given fragmentation, we need to do a little more work.
     */
    if (pkt.headers & LOWMSG_FRAG1_HDR) {
      frag_length = len - compressed_len - LOWMSG_FRAG1_LEN + sizeof(struct ip6_hdr) + packs_header(msg);
      frag_length -= (frag_length % 8);
      frag_length -= (sizeof(struct ip6_hdr) + packs_header(msg));
    } else {
      frag_length = ntoh16(msg->hdr.plen) - packs_header(msg);
    }
    // frag_length contains the number of bytes in uncompressed headers.

    ip_memcpy(getLowpanPayload(&pkt) + compressed_len, 
              msg->data + packs_header(msg), frag_length);

    progress->tag = frag_tag;
    progress->offset = frag_length + sizeof(struct ip6_hdr) + packs_header(msg);

    // printfUART("frag: 0x%x 0x%x 0x%x\n", header_len, frag_length, compressed_len);

    return header_len + frag_length + compressed_len;
  } else {
    /*
     * we've already sent the first fragment; we only need to send a
     * subsequent one or return zero if we're at the end of the buffer;
     *
     */
    //printf("offset: 0x%x plen: 0x%x\n", progress->offset, ntoh16(ip->plen) + sizeof(struct ip6_hdr));

    // NOTE : this should be a >= to detect runaway lengths.  However,
    // it is useful for debugging to require equality.
    if (progress->offset == ntoh16(msg->hdr.plen) + sizeof(struct ip6_hdr)) return 0;
    // the only headers we need now is the fragn header.

    pkt.headers |= LOWMSG_FRAGN_HDR;
    
    // send out the fragments some frasgments.
    //printf ("--- sending fragment\n");
    // now we're pointing at the start of the 6loWPAN frame in the packet.
    pkt.data = buf;
    pkt.len = len;
    // setup the fragmentation headers
    if (setupHeaders(&pkt, pkt.headers)) goto fail;
    if (setFragDgramTag(&pkt, progress->tag)) goto fail;

    //printf ("frag dgram size 0x%x progress: 0x%x\n", ntoh16(ip->plen) + sizeof(struct ip6_hdr),
/*     progress->offset); */

    if (setFragDgramSize(&pkt, ntoh16(msg->hdr.plen) + sizeof(struct ip6_hdr))) goto fail;
    if (setFragDgramOffset(&pkt, (progress->offset) / 8)) goto fail;

    frag_length = min(len - LOWMSG_FRAGN_LEN, 
                      ntoh16(msg->hdr.plen) + sizeof(struct ip6_hdr) - progress->offset);

    

    // unless this is the last fragment, we must sent a multiple of 8 bytes;
    if (frag_length + progress->offset != ntoh16(msg->hdr.plen) + sizeof(struct ip6_hdr))
      frag_length -= (frag_length % 8);

    pkt.len = frag_length + LOWMSG_FRAGN_LEN;

    memcpy(buf + LOWMSG_FRAGN_LEN, ((uint8_t *)&msg->hdr) + progress->offset, frag_length);
    progress->offset += frag_length;

    //printf("frag length is: 0x%x offset: 0x%x max: 0x%x\n", frag_length, progress->offset, LOWPAN_MTU);
    
    return frag_length + LOWMSG_FRAGN_LEN;
  }
 fail:
  return 0;
}


/*
 *  this function will copy the fragmented data located at pkt into
 *  the buffers allocated in the reconstruction structure.  This
 *  function should not be passed packets without fragmentation
 *  headers.
 *
 *  returns non-zero if reconstruction is complete and the structures
 *  in reconstruct_t are ready for the application
 */
uint8_t addFragment(packed_lowmsg_t *lowmsg, reconstruct_t *recon) {
  if (lowmsg == NULL || recon == NULL) return 0;
  struct ip6_hdr *ip = &(recon->buf->hdr);
  uint8_t offset_cmpr = 0;
  uint16_t offset, amount_here;
  uint8_t *payload;
  
  // given a first fragment, uncompress any headers into it
  if (hasFrag1Header(lowmsg)) {
    //printf("unpacking ip headers\n");
    payload = unpackHeaders(lowmsg, (uint8_t *)ip, recon->size);

    if (payload == NULL) goto fail;
    offset = sizeof(struct ip6_hdr) + packs_header(recon->buf);
    recon->bytes_rcvd += sizeof(struct ip6_hdr) + packs_header(recon->buf);

  } else if (hasFragNHeader(lowmsg)) {
    if (getFragDgramOffset(lowmsg, &offset_cmpr)) goto fail;
    offset = offset_cmpr * 8;
    payload = getLowpanPayload(lowmsg);
  } else {
    return 0;
  }
  amount_here = lowmsg->len - (payload - lowmsg->data);

  if (offset + amount_here > recon->size) goto fail;

  ip_memcpy(((uint8_t *)ip) + offset,
            payload, amount_here);
  
  recon->bytes_rcvd += amount_here;
  
  if (recon->bytes_rcvd == ntoh16(ip->plen) + sizeof(struct ip6_hdr)) {
    return 1;
  }
 fail:
  return 0;
}

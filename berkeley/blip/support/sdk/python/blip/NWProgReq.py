#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'NWProgReq'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 4

# The Active Message type associated with this message.
AM_TYPE = -1

class NWProgReq(tinyos.message.Message.Message):
    # Create a new NWProgReq of size 4.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=4):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <NWProgReq> \n"
        try:
            s += "  [cmd=0x%x]\n" % (self.get_cmd())
        except:
            pass
        try:
            s += "  [imgno=0x%x]\n" % (self.get_imgno())
        except:
            pass
        try:
            s += "  [cmd_data.offset=0x%x]\n" % (self.get_cmd_data_offset())
        except:
            pass
        try:
            s += "  [cmd_data.when=0x%x]\n" % (self.get_cmd_data_when())
        except:
            pass
        try:
            s += "  [cmd_data.nimages=0x%x]\n" % (self.get_cmd_data_nimages())
        except:
            pass
        try:
            pass
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: cmd
    #   Field type: short
    #   Offset (bits): 0
    #   Size (bits): 8
    #

    #
    # Return whether the field 'cmd' is signed (False).
    #
    def isSigned_cmd(self):
        return False
    
    #
    # Return whether the field 'cmd' is an array (False).
    #
    def isArray_cmd(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'cmd'
    #
    def offset_cmd(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'cmd'
    #
    def offsetBits_cmd(self):
        return 0
    
    #
    # Return the value (as a short) of the field 'cmd'
    #
    def get_cmd(self):
        return self.getUIntElement(self.offsetBits_cmd(), 8, 1)
    
    #
    # Set the value of the field 'cmd'
    #
    def set_cmd(self, value):
        self.setUIntElement(self.offsetBits_cmd(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'cmd'
    #
    def size_cmd(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'cmd'
    #
    def sizeBits_cmd(self):
        return 8
    
    #
    # Accessor methods for field: imgno
    #   Field type: short
    #   Offset (bits): 8
    #   Size (bits): 8
    #

    #
    # Return whether the field 'imgno' is signed (False).
    #
    def isSigned_imgno(self):
        return False
    
    #
    # Return whether the field 'imgno' is an array (False).
    #
    def isArray_imgno(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'imgno'
    #
    def offset_imgno(self):
        return (8 / 8)
    
    #
    # Return the offset (in bits) of the field 'imgno'
    #
    def offsetBits_imgno(self):
        return 8
    
    #
    # Return the value (as a short) of the field 'imgno'
    #
    def get_imgno(self):
        return self.getUIntElement(self.offsetBits_imgno(), 8, 1)
    
    #
    # Set the value of the field 'imgno'
    #
    def set_imgno(self, value):
        self.setUIntElement(self.offsetBits_imgno(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'imgno'
    #
    def size_imgno(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'imgno'
    #
    def sizeBits_imgno(self):
        return 8
    
    #
    # Accessor methods for field: cmd_data.offset
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'cmd_data.offset' is signed (False).
    #
    def isSigned_cmd_data_offset(self):
        return False
    
    #
    # Return whether the field 'cmd_data.offset' is an array (False).
    #
    def isArray_cmd_data_offset(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'cmd_data.offset'
    #
    def offset_cmd_data_offset(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'cmd_data.offset'
    #
    def offsetBits_cmd_data_offset(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'cmd_data.offset'
    #
    def get_cmd_data_offset(self):
        return self.getUIntElement(self.offsetBits_cmd_data_offset(), 16, 1)
    
    #
    # Set the value of the field 'cmd_data.offset'
    #
    def set_cmd_data_offset(self, value):
        self.setUIntElement(self.offsetBits_cmd_data_offset(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'cmd_data.offset'
    #
    def size_cmd_data_offset(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'cmd_data.offset'
    #
    def sizeBits_cmd_data_offset(self):
        return 16
    
    #
    # Accessor methods for field: cmd_data.when
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'cmd_data.when' is signed (False).
    #
    def isSigned_cmd_data_when(self):
        return False
    
    #
    # Return whether the field 'cmd_data.when' is an array (False).
    #
    def isArray_cmd_data_when(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'cmd_data.when'
    #
    def offset_cmd_data_when(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'cmd_data.when'
    #
    def offsetBits_cmd_data_when(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'cmd_data.when'
    #
    def get_cmd_data_when(self):
        return self.getUIntElement(self.offsetBits_cmd_data_when(), 16, 1)
    
    #
    # Set the value of the field 'cmd_data.when'
    #
    def set_cmd_data_when(self, value):
        self.setUIntElement(self.offsetBits_cmd_data_when(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'cmd_data.when'
    #
    def size_cmd_data_when(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'cmd_data.when'
    #
    def sizeBits_cmd_data_when(self):
        return 16
    
    #
    # Accessor methods for field: cmd_data.nimages
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'cmd_data.nimages' is signed (False).
    #
    def isSigned_cmd_data_nimages(self):
        return False
    
    #
    # Return whether the field 'cmd_data.nimages' is an array (False).
    #
    def isArray_cmd_data_nimages(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'cmd_data.nimages'
    #
    def offset_cmd_data_nimages(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'cmd_data.nimages'
    #
    def offsetBits_cmd_data_nimages(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'cmd_data.nimages'
    #
    def get_cmd_data_nimages(self):
        return self.getUIntElement(self.offsetBits_cmd_data_nimages(), 16, 1)
    
    #
    # Set the value of the field 'cmd_data.nimages'
    #
    def set_cmd_data_nimages(self, value):
        self.setUIntElement(self.offsetBits_cmd_data_nimages(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'cmd_data.nimages'
    #
    def size_cmd_data_nimages(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'cmd_data.nimages'
    #
    def sizeBits_cmd_data_nimages(self):
        return 16
    
    #
    # Accessor methods for field: data
    #   Field type: short[]
    #   Offset (bits): 32
    #   Size of each element (bits): 8
    #

    #
    # Return whether the field 'data' is signed (False).
    #
    def isSigned_data(self):
        return False
    
    #
    # Return whether the field 'data' is an array (True).
    #
    def isArray_data(self):
        return True
    
    #
    # Return the offset (in bytes) of the field 'data'
    #
    def offset_data(self, index1):
        offset = 32
        if index1 < 0:
            raise IndexError
        offset += 0 + index1 * 8
        return (offset / 8)
    
    #
    # Return the offset (in bits) of the field 'data'
    #
    def offsetBits_data(self, index1):
        offset = 32
        if index1 < 0:
            raise IndexError
        offset += 0 + index1 * 8
        return offset
    
    #
    # Return the entire array 'data' as a short[]
    #
    def get_data(self):
        raise IndexError
    
    #
    # Set the contents of the array 'data' from the given short[]
    #
    def set_data(self, value):
        for index0 in range(0, len(value)):
            self.setElement_data(index0, value[index0])

    #
    # Return an element (as a short) of the array 'data'
    #
    def getElement_data(self, index1):
        return self.getUIntElement(self.offsetBits_data(index1), 8, 1)
    
    #
    # Set an element of the array 'data'
    #
    def setElement_data(self, index1, value):
        self.setUIntElement(self.offsetBits_data(index1), 8, value, 1)
    
    #
    # Return the size, in bytes, of each element of the array 'data'
    #
    def elementSize_data(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of each element of the array 'data'
    #
    def elementSizeBits_data(self):
        return 8
    
    #
    # Return the number of dimensions in the array 'data'
    #
    def numDimensions_data(self):
        return 1
    
    #
    # Return the number of elements in the array 'data'
    # for the given dimension.
    #
    def numElements_data(self, dimension):
        array_dims = [ 0,  ]
        if dimension < 0 or dimension >= 1:
            raise IndexException
        if array_dims[dimension] == 0:
            raise IndexError
        return array_dims[dimension]
    
    #
    # Fill in the array 'data' with a String
    #
    def setString_data(self, s):
         l = len(s)
         for i in range(0, l):
             self.setElement_data(i, ord(s[i]));
         self.setElement_data(l, 0) #null terminate
    
    #
    # Read the array 'data' as a String
    #
    def getString_data(self):
        carr = "";
        for i in range(0, 4000):
            if self.getElement_data(i) == chr(0):
                break
            carr += self.getElement_data(i)
        return carr
    
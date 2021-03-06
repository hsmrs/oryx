"""autogenerated by genpy from oryx_msgs/Heartbeat.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class Heartbeat(genpy.Message):
  _md5sum = "3ee530bfddeca639d0cefeb562b0d361"
  _type = "oryx_msgs/Heartbeat"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#Message for sending a heartbeat to the oryx_diagnostics management software.

#timestamp (does not use header to save weight. Used by the diagnostics package for transmission latency purposes
time timestamp

#The unique node_id that was provided at registration with the diagnostics system to the node
uint16 node_id


"""
  __slots__ = ['timestamp','node_id']
  _slot_types = ['time','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,node_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Heartbeat, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = genpy.Time()
      if self.node_id is None:
        self.node_id = 0
    else:
      self.timestamp = genpy.Time()
      self.node_id = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2IH.pack(_x.timestamp.secs, _x.timestamp.nsecs, _x.node_id))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.timestamp is None:
        self.timestamp = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 10
      (_x.timestamp.secs, _x.timestamp.nsecs, _x.node_id,) = _struct_2IH.unpack(str[start:end])
      self.timestamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2IH.pack(_x.timestamp.secs, _x.timestamp.nsecs, _x.node_id))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.timestamp is None:
        self.timestamp = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 10
      (_x.timestamp.secs, _x.timestamp.nsecs, _x.node_id,) = _struct_2IH.unpack(str[start:end])
      self.timestamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2IH = struct.Struct("<2IH")

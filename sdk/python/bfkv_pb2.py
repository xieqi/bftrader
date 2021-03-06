# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bfkv.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bfgateway_pb2 as bfgateway__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bfkv.proto',
  package='bftrader',
  syntax='proto3',
  serialized_pb=_b('\n\nbfkv.proto\x12\x08\x62\x66trader\x1a\x0f\x62\x66gateway.proto\x1a\x19google/protobuf/any.proto2\xe7\x02\n\x0b\x42\x66KvService\x12\x34\n\x04Ping\x12\x14.bftrader.BfPingData\x1a\x14.bftrader.BfPingData\"\x00\x12@\n\x0cPingStreamCS\x12\x14.google.protobuf.Any\x1a\x14.google.protobuf.Any\"\x00(\x01\x30\x01\x12=\n\x0bPingStreamC\x12\x14.google.protobuf.Any\x1a\x14.google.protobuf.Any\"\x00(\x01\x12=\n\x0bPingStreamS\x12\x14.google.protobuf.Any\x1a\x14.google.protobuf.Any\"\x00\x30\x01\x12/\n\x05SetKv\x12\x12.bftrader.BfKvData\x1a\x10.bftrader.BfVoid\"\x00\x12\x31\n\x05GetKv\x12\x12.bftrader.BfKvData\x1a\x12.bftrader.BfKvData\"\x00\x62\x06proto3')
  ,
  dependencies=[bfgateway__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaBfKvServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def PingStreamCS(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def PingStreamC(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def PingStreamS(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetKv(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetKv(self, request, context):
    raise NotImplementedError()

class BetaBfKvServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request, timeout):
    raise NotImplementedError()
  Ping.future = None
  @abc.abstractmethod
  def PingStreamCS(self, request_iterator, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def PingStreamC(self, request_iterator, timeout):
    raise NotImplementedError()
  PingStreamC.future = None
  @abc.abstractmethod
  def PingStreamS(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetKv(self, request, timeout):
    raise NotImplementedError()
  SetKv.future = None
  @abc.abstractmethod
  def GetKv(self, request, timeout):
    raise NotImplementedError()
  GetKv.future = None

def beta_create_BfKvService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import bfgateway_pb2
  import bfgateway_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  request_deserializers = {
    ('bftrader.BfKvService', 'GetKv'): bfgateway_pb2.BfKvData.FromString,
    ('bftrader.BfKvService', 'Ping'): bfgateway_pb2.BfPingData.FromString,
    ('bftrader.BfKvService', 'PingStreamC'): google.protobuf.any_pb2.Any.FromString,
    ('bftrader.BfKvService', 'PingStreamCS'): google.protobuf.any_pb2.Any.FromString,
    ('bftrader.BfKvService', 'PingStreamS'): google.protobuf.any_pb2.Any.FromString,
    ('bftrader.BfKvService', 'SetKv'): bfgateway_pb2.BfKvData.FromString,
  }
  response_serializers = {
    ('bftrader.BfKvService', 'GetKv'): bfgateway_pb2.BfKvData.SerializeToString,
    ('bftrader.BfKvService', 'Ping'): bfgateway_pb2.BfPingData.SerializeToString,
    ('bftrader.BfKvService', 'PingStreamC'): google.protobuf.any_pb2.Any.SerializeToString,
    ('bftrader.BfKvService', 'PingStreamCS'): google.protobuf.any_pb2.Any.SerializeToString,
    ('bftrader.BfKvService', 'PingStreamS'): google.protobuf.any_pb2.Any.SerializeToString,
    ('bftrader.BfKvService', 'SetKv'): bfgateway_pb2.BfVoid.SerializeToString,
  }
  method_implementations = {
    ('bftrader.BfKvService', 'GetKv'): face_utilities.unary_unary_inline(servicer.GetKv),
    ('bftrader.BfKvService', 'Ping'): face_utilities.unary_unary_inline(servicer.Ping),
    ('bftrader.BfKvService', 'PingStreamC'): face_utilities.stream_unary_inline(servicer.PingStreamC),
    ('bftrader.BfKvService', 'PingStreamCS'): face_utilities.stream_stream_inline(servicer.PingStreamCS),
    ('bftrader.BfKvService', 'PingStreamS'): face_utilities.unary_stream_inline(servicer.PingStreamS),
    ('bftrader.BfKvService', 'SetKv'): face_utilities.unary_unary_inline(servicer.SetKv),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_BfKvService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import bfgateway_pb2
  import bfgateway_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import google.protobuf.any_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  request_serializers = {
    ('bftrader.BfKvService', 'GetKv'): bfgateway_pb2.BfKvData.SerializeToString,
    ('bftrader.BfKvService', 'Ping'): bfgateway_pb2.BfPingData.SerializeToString,
    ('bftrader.BfKvService', 'PingStreamC'): google.protobuf.any_pb2.Any.SerializeToString,
    ('bftrader.BfKvService', 'PingStreamCS'): google.protobuf.any_pb2.Any.SerializeToString,
    ('bftrader.BfKvService', 'PingStreamS'): google.protobuf.any_pb2.Any.SerializeToString,
    ('bftrader.BfKvService', 'SetKv'): bfgateway_pb2.BfKvData.SerializeToString,
  }
  response_deserializers = {
    ('bftrader.BfKvService', 'GetKv'): bfgateway_pb2.BfKvData.FromString,
    ('bftrader.BfKvService', 'Ping'): bfgateway_pb2.BfPingData.FromString,
    ('bftrader.BfKvService', 'PingStreamC'): google.protobuf.any_pb2.Any.FromString,
    ('bftrader.BfKvService', 'PingStreamCS'): google.protobuf.any_pb2.Any.FromString,
    ('bftrader.BfKvService', 'PingStreamS'): google.protobuf.any_pb2.Any.FromString,
    ('bftrader.BfKvService', 'SetKv'): bfgateway_pb2.BfVoid.FromString,
  }
  cardinalities = {
    'GetKv': cardinality.Cardinality.UNARY_UNARY,
    'Ping': cardinality.Cardinality.UNARY_UNARY,
    'PingStreamC': cardinality.Cardinality.STREAM_UNARY,
    'PingStreamCS': cardinality.Cardinality.STREAM_STREAM,
    'PingStreamS': cardinality.Cardinality.UNARY_STREAM,
    'SetKv': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'bftrader.BfKvService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)

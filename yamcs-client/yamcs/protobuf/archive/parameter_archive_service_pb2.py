# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/archive/parameter_archive_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.protobuf.archive import archive_pb2 as yamcs_dot_protobuf_dot_archive_dot_archive__pb2
from yamcs.protobuf.pvalue import pvalue_pb2 as yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2
from yamcs.protobuf import yamcs_pb2 as yamcs_dot_protobuf_dot_yamcs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/archive/parameter_archive_service.proto',
  package='yamcs.protobuf.archive',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\034ParameterArchiveServiceProtoP\001'),
  serialized_pb=_b('\n6yamcs/protobuf/archive/parameter_archive_service.proto\x12\x16yamcs.protobuf.archive\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\x1a$yamcs/protobuf/archive/archive.proto\x1a\"yamcs/protobuf/pvalue/pvalue.proto\x1a\x1ayamcs/protobuf/yamcs.proto\"|\n\x13RebuildRangeRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x80\x01\n\x17\x44\x65letePartitionsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"A\n\x1fGetArchivedParameterInfoRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xe7\x01\n\x19GetParameterRangesRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12)\n\x05start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06minGap\x18\x05 \x01(\x03\x12\x0e\n\x06maxGap\x18\x06 \x01(\x03\x12\x12\n\nnorealtime\x18\x07 \x01(\x08\x12\x11\n\tprocessor\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t2\x8e\x08\n\x13ParameterArchiveApi\x12\x90\x01\n\x0cRebuildRange\x12+.yamcs.protobuf.archive.RebuildRangeRequest\x1a\x16.google.protobuf.Empty\";\x8a\x92\x03\x37\x1a\x30/api/archive/{instance}/parameterArchive:rebuild:\x01*H\x01\x12\xa6\x01\n\x10\x44\x65letePartitions\x12/.yamcs.protobuf.archive.DeletePartitionsRequest\x1a\x1d.yamcs.protobuf.StringMessage\"B\x8a\x92\x03>\x1a\x39/api/archive/{instance}/parameterArchive:deletePartitions:\x01*\x12\xb9\x01\n\x18GetArchivedParameterInfo\x12\x37.yamcs.protobuf.archive.GetArchivedParameterInfoRequest\x1a\x1d.yamcs.protobuf.StringMessage\"E\x8a\x92\x03\x41\n?/api/archive/{instance}/parameterArchive/info/parameter/{name*}\x12\xa6\x01\n\x13GetParameterSamples\x12\x32.yamcs.protobuf.archive.GetParameterSamplesRequest\x1a!.yamcs.protobuf.pvalue.TimeSeries\"8\x8a\x92\x03\x34\n2/api/archive/{instance}/parameters/{name*}/samples\x12\x9f\x01\n\x12GetParameterRanges\x12\x31.yamcs.protobuf.archive.GetParameterRangesRequest\x1a\x1d.yamcs.protobuf.pvalue.Ranges\"7\x8a\x92\x03\x33\n1/api/archive/{instance}/parameters/{name*}/ranges\x12\xb3\x01\n\x14ListParameterHistory\x12\x33.yamcs.protobuf.archive.ListParameterHistoryRequest\x1a\x34.yamcs.protobuf.archive.ListParameterHistoryResponse\"0\x8a\x92\x03,\n*/api/archive/{instance}/parameters/{name*}B4\n\x12org.yamcs.protobufB\x1cParameterArchiveServiceProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_archive_dot_archive__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_yamcs__pb2.DESCRIPTOR,])




_REBUILDRANGEREQUEST = _descriptor.Descriptor(
  name='RebuildRangeRequest',
  full_name='yamcs.protobuf.archive.RebuildRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.RebuildRangeRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.archive.RebuildRangeRequest.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.archive.RebuildRangeRequest.stop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=399,
)


_DELETEPARTITIONSREQUEST = _descriptor.Descriptor(
  name='DeletePartitionsRequest',
  full_name='yamcs.protobuf.archive.DeletePartitionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.DeletePartitionsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.archive.DeletePartitionsRequest.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.archive.DeletePartitionsRequest.stop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=530,
)


_GETARCHIVEDPARAMETERINFOREQUEST = _descriptor.Descriptor(
  name='GetArchivedParameterInfoRequest',
  full_name='yamcs.protobuf.archive.GetArchivedParameterInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.GetArchivedParameterInfoRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.archive.GetArchivedParameterInfoRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=597,
)


_GETPARAMETERRANGESREQUEST = _descriptor.Descriptor(
  name='GetParameterRangesRequest',
  full_name='yamcs.protobuf.archive.GetParameterRangesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.start', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.stop', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minGap', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.minGap', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxGap', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.maxGap', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='norealtime', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.norealtime', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.processor', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='yamcs.protobuf.archive.GetParameterRangesRequest.source', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=600,
  serialized_end=831,
)

_REBUILDRANGEREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REBUILDRANGEREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DELETEPARTITIONSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DELETEPARTITIONSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETPARAMETERRANGESREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETPARAMETERRANGESREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['RebuildRangeRequest'] = _REBUILDRANGEREQUEST
DESCRIPTOR.message_types_by_name['DeletePartitionsRequest'] = _DELETEPARTITIONSREQUEST
DESCRIPTOR.message_types_by_name['GetArchivedParameterInfoRequest'] = _GETARCHIVEDPARAMETERINFOREQUEST
DESCRIPTOR.message_types_by_name['GetParameterRangesRequest'] = _GETPARAMETERRANGESREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RebuildRangeRequest = _reflection.GeneratedProtocolMessageType('RebuildRangeRequest', (_message.Message,), dict(
  DESCRIPTOR = _REBUILDRANGEREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.RebuildRangeRequest)
  ))
_sym_db.RegisterMessage(RebuildRangeRequest)

DeletePartitionsRequest = _reflection.GeneratedProtocolMessageType('DeletePartitionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPARTITIONSREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.DeletePartitionsRequest)
  ))
_sym_db.RegisterMessage(DeletePartitionsRequest)

GetArchivedParameterInfoRequest = _reflection.GeneratedProtocolMessageType('GetArchivedParameterInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETARCHIVEDPARAMETERINFOREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.GetArchivedParameterInfoRequest)
  ))
_sym_db.RegisterMessage(GetArchivedParameterInfoRequest)

GetParameterRangesRequest = _reflection.GeneratedProtocolMessageType('GetParameterRangesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPARAMETERRANGESREQUEST,
  __module__ = 'yamcs.protobuf.archive.parameter_archive_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.archive.GetParameterRangesRequest)
  ))
_sym_db.RegisterMessage(GetParameterRangesRequest)


DESCRIPTOR._options = None

_PARAMETERARCHIVEAPI = _descriptor.ServiceDescriptor(
  name='ParameterArchiveApi',
  full_name='yamcs.protobuf.archive.ParameterArchiveApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=834,
  serialized_end=1872,
  methods=[
  _descriptor.MethodDescriptor(
    name='RebuildRange',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.RebuildRange',
    index=0,
    containing_service=None,
    input_type=_REBUILDRANGEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\0037\0320/api/archive/{instance}/parameterArchive:rebuild:\001*H\001'),
  ),
  _descriptor.MethodDescriptor(
    name='DeletePartitions',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.DeletePartitions',
    index=1,
    containing_service=None,
    input_type=_DELETEPARTITIONSREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._STRINGMESSAGE,
    serialized_options=_b('\212\222\003>\0329/api/archive/{instance}/parameterArchive:deletePartitions:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetArchivedParameterInfo',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetArchivedParameterInfo',
    index=2,
    containing_service=None,
    input_type=_GETARCHIVEDPARAMETERINFOREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._STRINGMESSAGE,
    serialized_options=_b('\212\222\003A\n?/api/archive/{instance}/parameterArchive/info/parameter/{name*}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetParameterSamples',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetParameterSamples',
    index=3,
    containing_service=None,
    input_type=yamcs_dot_protobuf_dot_archive_dot_archive__pb2._GETPARAMETERSAMPLESREQUEST,
    output_type=yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2._TIMESERIES,
    serialized_options=_b('\212\222\0034\n2/api/archive/{instance}/parameters/{name*}/samples'),
  ),
  _descriptor.MethodDescriptor(
    name='GetParameterRanges',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.GetParameterRanges',
    index=4,
    containing_service=None,
    input_type=_GETPARAMETERRANGESREQUEST,
    output_type=yamcs_dot_protobuf_dot_pvalue_dot_pvalue__pb2._RANGES,
    serialized_options=_b('\212\222\0033\n1/api/archive/{instance}/parameters/{name*}/ranges'),
  ),
  _descriptor.MethodDescriptor(
    name='ListParameterHistory',
    full_name='yamcs.protobuf.archive.ParameterArchiveApi.ListParameterHistory',
    index=5,
    containing_service=None,
    input_type=yamcs_dot_protobuf_dot_archive_dot_archive__pb2._LISTPARAMETERHISTORYREQUEST,
    output_type=yamcs_dot_protobuf_dot_archive_dot_archive__pb2._LISTPARAMETERHISTORYRESPONSE,
    serialized_options=_b('\212\222\003,\n*/api/archive/{instance}/parameters/{name*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_PARAMETERARCHIVEAPI)

DESCRIPTOR.services_by_name['ParameterArchiveApi'] = _PARAMETERARCHIVEAPI

# @@protoc_insertion_point(module_scope)

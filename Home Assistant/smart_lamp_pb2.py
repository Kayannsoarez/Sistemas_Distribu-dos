# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart_lamp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='smart_lamp.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10smart_lamp.proto\"\x1f\n\rLampadaStatus\x12\x0e\n\x06status\x18\x01 \x01(\x05\x32p\n\x07Lampada\x12\x30\n\x0cligarLampada\x12\x0e.LampadaStatus\x1a\x0e.LampadaStatus\"\x00\x12\x33\n\x0f\x64\x65sligarLampada\x12\x0e.LampadaStatus\x1a\x0e.LampadaStatus\"\x00\x62\x06proto3'
)




_LAMPADASTATUS = _descriptor.Descriptor(
  name='LampadaStatus',
  full_name='LampadaStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='LampadaStatus.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=51,
)

DESCRIPTOR.message_types_by_name['LampadaStatus'] = _LAMPADASTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LampadaStatus = _reflection.GeneratedProtocolMessageType('LampadaStatus', (_message.Message,), {
  'DESCRIPTOR' : _LAMPADASTATUS,
  '__module__' : 'smart_lamp_pb2'
  # @@protoc_insertion_point(class_scope:LampadaStatus)
  })
_sym_db.RegisterMessage(LampadaStatus)



_LAMPADA = _descriptor.ServiceDescriptor(
  name='Lampada',
  full_name='Lampada',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=53,
  serialized_end=165,
  methods=[
  _descriptor.MethodDescriptor(
    name='ligarLampada',
    full_name='Lampada.ligarLampada',
    index=0,
    containing_service=None,
    input_type=_LAMPADASTATUS,
    output_type=_LAMPADASTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='desligarLampada',
    full_name='Lampada.desligarLampada',
    index=1,
    containing_service=None,
    input_type=_LAMPADASTATUS,
    output_type=_LAMPADASTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LAMPADA)

DESCRIPTOR.services_by_name['Lampada'] = _LAMPADA

# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fabric_next.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fabric_next.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x66\x61\x62ric_next.proto\x12\x06protos\x1a\x1fgoogle/protobuf/timestamp.proto\"@\n\x08\x45nvelope\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12!\n\x07message\x18\x02 \x01(\x0b\x32\x10.protos.Message2\"\x90\x02\n\x08Message2\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.protos.Message2.Type\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\"\x8d\x01\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tDISCOVERY\x10\x01\x12\x08\n\x04SYNC\x10\x02\x12\x0c\n\x08PROPOSAL\x10\x03\x12\x10\n\x0cPROPOSAL_SET\x10\x04\x12\x13\n\x0fPROPOSAL_RESULT\x10\x05\x12\x17\n\x13PROPOSAL_SET_RESULT\x10\x06\x12\x0f\n\x0bTRANSACTION\x10\x07\"r\n\x08Proposal\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.protos.Proposal.Type\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"$\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tCHAINCODE\x10\x01\"=\n\tResponse2\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"\x1d\n\x0fSystemChaincode\x12\n\n\x02id\x18\x01 \x01(\t\"\x96\x01\n\x06\x41\x63tion\x12\x14\n\x0cproposalHash\x18\x01 \x01(\x0c\x12\x18\n\x10simulationResult\x18\x02 \x01(\x0c\x12\x0e\n\x06\x65vents\x18\x03 \x03(\x0c\x12%\n\x04\x65scc\x18\x04 \x01(\x0b\x32\x17.protos.SystemChaincode\x12%\n\x04vscc\x18\x05 \x01(\x0b\x32\x17.protos.SystemChaincode\" \n\x0b\x45ndorsement\x12\x11\n\tsignature\x18\x01 \x01(\x0c\"v\n\x10ProposalResponse\x12#\n\x08response\x18\x01 \x01(\x0b\x32\x11.protos.Response2\x12\x13\n\x0b\x61\x63tionBytes\x18\x02 \x01(\x0c\x12(\n\x0b\x65ndorsement\x18\x03 \x01(\x0b\x32\x13.protos.Endorsement\"g\n\x0e\x45ndorsedAction\x12\x13\n\x0b\x61\x63tionBytes\x18\x01 \x01(\x0c\x12)\n\x0c\x65ndorsements\x18\x02 \x03(\x0b\x32\x13.protos.Endorsement\x12\x15\n\rproposalBytes\x18\x03 \x01(\x0c\"?\n\x0cTransaction2\x12/\n\x0f\x65ndorsedActions\x18\x01 \x03(\x0b\x32\x16.protos.EndorsedAction2K\n\x08\x45ndorser\x12?\n\x0fProcessProposal\x12\x10.protos.Proposal\x1a\x18.protos.ProposalResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MESSAGE2_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='protos.Message2.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOVERY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSAL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSAL_SET', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSAL_RESULT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSAL_SET_RESULT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTION', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=260,
  serialized_end=401,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE2_TYPE)

_PROPOSAL_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='protos.Proposal.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAINCODE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=481,
  serialized_end=517,
)
_sym_db.RegisterEnumDescriptor(_PROPOSAL_TYPE)


_ENVELOPE = _descriptor.Descriptor(
  name='Envelope',
  full_name='protos.Envelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='protos.Envelope.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='protos.Envelope.message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=126,
)


_MESSAGE2 = _descriptor.Descriptor(
  name='Message2',
  full_name='protos.Message2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.Message2.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='protos.Message2.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protos.Message2.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.Message2.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE2_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=401,
)


_PROPOSAL = _descriptor.Descriptor(
  name='Proposal',
  full_name='protos.Proposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.Proposal.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='protos.Proposal.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.Proposal.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROPOSAL_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=517,
)


_RESPONSE2 = _descriptor.Descriptor(
  name='Response2',
  full_name='protos.Response2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='protos.Response2.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='protos.Response2.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.Response2.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=580,
)


_SYSTEMCHAINCODE = _descriptor.Descriptor(
  name='SystemChaincode',
  full_name='protos.SystemChaincode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protos.SystemChaincode.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=611,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='protos.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposalHash', full_name='protos.Action.proposalHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simulationResult', full_name='protos.Action.simulationResult', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events', full_name='protos.Action.events', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escc', full_name='protos.Action.escc', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vscc', full_name='protos.Action.vscc', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=764,
)


_ENDORSEMENT = _descriptor.Descriptor(
  name='Endorsement',
  full_name='protos.Endorsement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='protos.Endorsement.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=798,
)


_PROPOSALRESPONSE = _descriptor.Descriptor(
  name='ProposalResponse',
  full_name='protos.ProposalResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='protos.ProposalResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actionBytes', full_name='protos.ProposalResponse.actionBytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endorsement', full_name='protos.ProposalResponse.endorsement', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=918,
)


_ENDORSEDACTION = _descriptor.Descriptor(
  name='EndorsedAction',
  full_name='protos.EndorsedAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionBytes', full_name='protos.EndorsedAction.actionBytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endorsements', full_name='protos.EndorsedAction.endorsements', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proposalBytes', full_name='protos.EndorsedAction.proposalBytes', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=920,
  serialized_end=1023,
)


_TRANSACTION2 = _descriptor.Descriptor(
  name='Transaction2',
  full_name='protos.Transaction2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endorsedActions', full_name='protos.Transaction2.endorsedActions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1025,
  serialized_end=1088,
)

_ENVELOPE.fields_by_name['message'].message_type = _MESSAGE2
_MESSAGE2.fields_by_name['type'].enum_type = _MESSAGE2_TYPE
_MESSAGE2.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MESSAGE2_TYPE.containing_type = _MESSAGE2
_PROPOSAL.fields_by_name['type'].enum_type = _PROPOSAL_TYPE
_PROPOSAL_TYPE.containing_type = _PROPOSAL
_ACTION.fields_by_name['escc'].message_type = _SYSTEMCHAINCODE
_ACTION.fields_by_name['vscc'].message_type = _SYSTEMCHAINCODE
_PROPOSALRESPONSE.fields_by_name['response'].message_type = _RESPONSE2
_PROPOSALRESPONSE.fields_by_name['endorsement'].message_type = _ENDORSEMENT
_ENDORSEDACTION.fields_by_name['endorsements'].message_type = _ENDORSEMENT
_TRANSACTION2.fields_by_name['endorsedActions'].message_type = _ENDORSEDACTION
DESCRIPTOR.message_types_by_name['Envelope'] = _ENVELOPE
DESCRIPTOR.message_types_by_name['Message2'] = _MESSAGE2
DESCRIPTOR.message_types_by_name['Proposal'] = _PROPOSAL
DESCRIPTOR.message_types_by_name['Response2'] = _RESPONSE2
DESCRIPTOR.message_types_by_name['SystemChaincode'] = _SYSTEMCHAINCODE
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['Endorsement'] = _ENDORSEMENT
DESCRIPTOR.message_types_by_name['ProposalResponse'] = _PROPOSALRESPONSE
DESCRIPTOR.message_types_by_name['EndorsedAction'] = _ENDORSEDACTION
DESCRIPTOR.message_types_by_name['Transaction2'] = _TRANSACTION2

Envelope = _reflection.GeneratedProtocolMessageType('Envelope', (_message.Message,), dict(
  DESCRIPTOR = _ENVELOPE,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.Envelope)
  ))
_sym_db.RegisterMessage(Envelope)

Message2 = _reflection.GeneratedProtocolMessageType('Message2', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE2,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.Message2)
  ))
_sym_db.RegisterMessage(Message2)

Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSAL,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.Proposal)
  ))
_sym_db.RegisterMessage(Proposal)

Response2 = _reflection.GeneratedProtocolMessageType('Response2', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE2,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.Response2)
  ))
_sym_db.RegisterMessage(Response2)

SystemChaincode = _reflection.GeneratedProtocolMessageType('SystemChaincode', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMCHAINCODE,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.SystemChaincode)
  ))
_sym_db.RegisterMessage(SystemChaincode)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.Action)
  ))
_sym_db.RegisterMessage(Action)

Endorsement = _reflection.GeneratedProtocolMessageType('Endorsement', (_message.Message,), dict(
  DESCRIPTOR = _ENDORSEMENT,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.Endorsement)
  ))
_sym_db.RegisterMessage(Endorsement)

ProposalResponse = _reflection.GeneratedProtocolMessageType('ProposalResponse', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSALRESPONSE,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProposalResponse)
  ))
_sym_db.RegisterMessage(ProposalResponse)

EndorsedAction = _reflection.GeneratedProtocolMessageType('EndorsedAction', (_message.Message,), dict(
  DESCRIPTOR = _ENDORSEDACTION,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.EndorsedAction)
  ))
_sym_db.RegisterMessage(EndorsedAction)

Transaction2 = _reflection.GeneratedProtocolMessageType('Transaction2', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION2,
  __module__ = 'fabric_next_pb2'
  # @@protoc_insertion_point(class_scope:protos.Transaction2)
  ))
_sym_db.RegisterMessage(Transaction2)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class EndorserStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProcessProposal = channel.unary_unary(
        '/protos.Endorser/ProcessProposal',
        request_serializer=Proposal.SerializeToString,
        response_deserializer=ProposalResponse.FromString,
        )


class EndorserServicer(object):

  def ProcessProposal(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EndorserServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProcessProposal': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessProposal,
          request_deserializer=Proposal.FromString,
          response_serializer=ProposalResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.Endorser', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaEndorserServicer(object):
  def ProcessProposal(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaEndorserStub(object):
  def ProcessProposal(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  ProcessProposal.future = None


def beta_create_Endorser_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('protos.Endorser', 'ProcessProposal'): Proposal.FromString,
  }
  response_serializers = {
    ('protos.Endorser', 'ProcessProposal'): ProposalResponse.SerializeToString,
  }
  method_implementations = {
    ('protos.Endorser', 'ProcessProposal'): face_utilities.unary_unary_inline(servicer.ProcessProposal),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Endorser_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('protos.Endorser', 'ProcessProposal'): Proposal.SerializeToString,
  }
  response_deserializers = {
    ('protos.Endorser', 'ProcessProposal'): ProposalResponse.FromString,
  }
  cardinalities = {
    'ProcessProposal': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'protos.Endorser', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)

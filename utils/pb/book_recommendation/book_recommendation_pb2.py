# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book_recommendation.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x62ook_recommendation.proto\x12\x0erecommendation\",\n\x19GetRecommendationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"U\n\x1aGetRecommendationsResponse\x12\x37\n\x0frecommendations\x18\x01 \x03(\x0b\x32\x1e.recommendation.Recommendation\"\xbc\x01\n\x0eRecommendation\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0e\n\x06\x63opies\x18\x05 \x01(\t\x12\x18\n\x10\x63opies_available\x18\x06 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x07 \x01(\t\x12\x11\n\timage_url\x18\x08 \x01(\t\x12\r\n\x05price\x18\t \x01(\x02\x12\x0c\n\x04tags\x18\n \x03(\t\"\x14\n\x12HealthCheckRequest\"%\n\x13HealthCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xdc\x01\n\x15RecommendationService\x12V\n\x0bHealthCheck\x12\".recommendation.HealthCheckRequest\x1a#.recommendation.HealthCheckResponse\x12k\n\x12GetRecommendations\x12).recommendation.GetRecommendationsRequest\x1a*.recommendation.GetRecommendationsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_recommendation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETRECOMMENDATIONSREQUEST']._serialized_start=45
  _globals['_GETRECOMMENDATIONSREQUEST']._serialized_end=89
  _globals['_GETRECOMMENDATIONSRESPONSE']._serialized_start=91
  _globals['_GETRECOMMENDATIONSRESPONSE']._serialized_end=176
  _globals['_RECOMMENDATION']._serialized_start=179
  _globals['_RECOMMENDATION']._serialized_end=367
  _globals['_HEALTHCHECKREQUEST']._serialized_start=369
  _globals['_HEALTHCHECKREQUEST']._serialized_end=389
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=391
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=428
  _globals['_RECOMMENDATIONSERVICE']._serialized_start=431
  _globals['_RECOMMENDATIONSERVICE']._serialized_end=651
# @@protoc_insertion_point(module_scope)

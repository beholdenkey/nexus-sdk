# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from nexus_sdk import schemas  # noqa: F401


class S3BlobStoreApiAdvancedBucketConnection(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            endpoint = schemas.StrSchema
            signerType = schemas.StrSchema
            forcePathStyle = schemas.BoolSchema
            maxConnectionPoolSize = schemas.Int32Schema
            __annotations__ = {
                "endpoint": endpoint,
                "signerType": signerType,
                "forcePathStyle": forcePathStyle,
                "maxConnectionPoolSize": maxConnectionPoolSize,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signerType"]) -> MetaOapg.properties.signerType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forcePathStyle"]) -> MetaOapg.properties.forcePathStyle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxConnectionPoolSize"]) -> MetaOapg.properties.maxConnectionPoolSize: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["endpoint", "signerType", "forcePathStyle", "maxConnectionPoolSize", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> typing.Union[MetaOapg.properties.endpoint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signerType"]) -> typing.Union[MetaOapg.properties.signerType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forcePathStyle"]) -> typing.Union[MetaOapg.properties.forcePathStyle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxConnectionPoolSize"]) -> typing.Union[MetaOapg.properties.maxConnectionPoolSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["endpoint", "signerType", "forcePathStyle", "maxConnectionPoolSize", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        endpoint: typing.Union[MetaOapg.properties.endpoint, str, schemas.Unset] = schemas.unset,
        signerType: typing.Union[MetaOapg.properties.signerType, str, schemas.Unset] = schemas.unset,
        forcePathStyle: typing.Union[MetaOapg.properties.forcePathStyle, bool, schemas.Unset] = schemas.unset,
        maxConnectionPoolSize: typing.Union[MetaOapg.properties.maxConnectionPoolSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'S3BlobStoreApiAdvancedBucketConnection':
        return super().__new__(
            cls,
            *_args,
            endpoint=endpoint,
            signerType=signerType,
            forcePathStyle=forcePathStyle,
            maxConnectionPoolSize=maxConnectionPoolSize,
            _configuration=_configuration,
            **kwargs,
        )

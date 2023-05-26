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


class DockerHostedStorageAttributes(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "strictContentTypeValidation",
            "writePolicy",
        }
        
        class properties:
            strictContentTypeValidation = schemas.BoolSchema
            
            
            class writePolicy(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALLOW(cls):
                    return cls("allow")
                
                @schemas.classproperty
                def ALLOW_ONCE(cls):
                    return cls("allow_once")
                
                @schemas.classproperty
                def DENY(cls):
                    return cls("deny")
            blobStoreName = schemas.StrSchema
            latestPolicy = schemas.BoolSchema
            __annotations__ = {
                "strictContentTypeValidation": strictContentTypeValidation,
                "writePolicy": writePolicy,
                "blobStoreName": blobStoreName,
                "latestPolicy": latestPolicy,
            }
    
    strictContentTypeValidation: MetaOapg.properties.strictContentTypeValidation
    writePolicy: MetaOapg.properties.writePolicy
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strictContentTypeValidation"]) -> MetaOapg.properties.strictContentTypeValidation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["writePolicy"]) -> MetaOapg.properties.writePolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blobStoreName"]) -> MetaOapg.properties.blobStoreName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latestPolicy"]) -> MetaOapg.properties.latestPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["strictContentTypeValidation", "writePolicy", "blobStoreName", "latestPolicy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strictContentTypeValidation"]) -> MetaOapg.properties.strictContentTypeValidation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["writePolicy"]) -> MetaOapg.properties.writePolicy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blobStoreName"]) -> typing.Union[MetaOapg.properties.blobStoreName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latestPolicy"]) -> typing.Union[MetaOapg.properties.latestPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["strictContentTypeValidation", "writePolicy", "blobStoreName", "latestPolicy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        strictContentTypeValidation: typing.Union[MetaOapg.properties.strictContentTypeValidation, bool, ],
        writePolicy: typing.Union[MetaOapg.properties.writePolicy, str, ],
        blobStoreName: typing.Union[MetaOapg.properties.blobStoreName, str, schemas.Unset] = schemas.unset,
        latestPolicy: typing.Union[MetaOapg.properties.latestPolicy, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DockerHostedStorageAttributes':
        return super().__new__(
            cls,
            *_args,
            strictContentTypeValidation=strictContentTypeValidation,
            writePolicy=writePolicy,
            blobStoreName=blobStoreName,
            latestPolicy=latestPolicy,
            _configuration=_configuration,
            **kwargs,
        )

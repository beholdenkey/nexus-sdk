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


class MavenAttributes(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class versionPolicy(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def RELEASE(cls):
                    return cls("RELEASE")
                
                @schemas.classproperty
                def SNAPSHOT(cls):
                    return cls("SNAPSHOT")
                
                @schemas.classproperty
                def MIXED(cls):
                    return cls("MIXED")
            
            
            class layoutPolicy(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STRICT(cls):
                    return cls("STRICT")
                
                @schemas.classproperty
                def PERMISSIVE(cls):
                    return cls("PERMISSIVE")
            
            
            class contentDisposition(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INLINE(cls):
                    return cls("INLINE")
                
                @schemas.classproperty
                def ATTACHMENT(cls):
                    return cls("ATTACHMENT")
            __annotations__ = {
                "versionPolicy": versionPolicy,
                "layoutPolicy": layoutPolicy,
                "contentDisposition": contentDisposition,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versionPolicy"]) -> MetaOapg.properties.versionPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layoutPolicy"]) -> MetaOapg.properties.layoutPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentDisposition"]) -> MetaOapg.properties.contentDisposition: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["versionPolicy", "layoutPolicy", "contentDisposition", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versionPolicy"]) -> typing.Union[MetaOapg.properties.versionPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layoutPolicy"]) -> typing.Union[MetaOapg.properties.layoutPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentDisposition"]) -> typing.Union[MetaOapg.properties.contentDisposition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["versionPolicy", "layoutPolicy", "contentDisposition", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        versionPolicy: typing.Union[MetaOapg.properties.versionPolicy, str, schemas.Unset] = schemas.unset,
        layoutPolicy: typing.Union[MetaOapg.properties.layoutPolicy, str, schemas.Unset] = schemas.unset,
        contentDisposition: typing.Union[MetaOapg.properties.contentDisposition, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MavenAttributes':
        return super().__new__(
            cls,
            *_args,
            versionPolicy=versionPolicy,
            layoutPolicy=layoutPolicy,
            contentDisposition=contentDisposition,
            _configuration=_configuration,
            **kwargs,
        )
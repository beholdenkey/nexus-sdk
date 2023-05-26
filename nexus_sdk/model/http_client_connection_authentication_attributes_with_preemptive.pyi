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


class HttpClientConnectionAuthenticationAttributesWithPreemptive(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def USERNAME(cls):
                    return cls("username")
                
                @schemas.classproperty
                def NTLM(cls):
                    return cls("ntlm")
            username = schemas.StrSchema
            password = schemas.StrSchema
            ntlmHost = schemas.StrSchema
            ntlmDomain = schemas.StrSchema
            preemptive = schemas.BoolSchema
            __annotations__ = {
                "type": type,
                "username": username,
                "password": password,
                "ntlmHost": ntlmHost,
                "ntlmDomain": ntlmDomain,
                "preemptive": preemptive,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ntlmHost"]) -> MetaOapg.properties.ntlmHost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ntlmDomain"]) -> MetaOapg.properties.ntlmDomain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preemptive"]) -> MetaOapg.properties.preemptive: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "username", "password", "ntlmHost", "ntlmDomain", "preemptive", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ntlmHost"]) -> typing.Union[MetaOapg.properties.ntlmHost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ntlmDomain"]) -> typing.Union[MetaOapg.properties.ntlmDomain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preemptive"]) -> typing.Union[MetaOapg.properties.preemptive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "username", "password", "ntlmHost", "ntlmDomain", "preemptive", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        ntlmHost: typing.Union[MetaOapg.properties.ntlmHost, str, schemas.Unset] = schemas.unset,
        ntlmDomain: typing.Union[MetaOapg.properties.ntlmDomain, str, schemas.Unset] = schemas.unset,
        preemptive: typing.Union[MetaOapg.properties.preemptive, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HttpClientConnectionAuthenticationAttributesWithPreemptive':
        return super().__new__(
            cls,
            *_args,
            type=type,
            username=username,
            password=password,
            ntlmHost=ntlmHost,
            ntlmDomain=ntlmDomain,
            preemptive=preemptive,
            _configuration=_configuration,
            **kwargs,
        )

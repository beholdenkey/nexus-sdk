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


class DockerAttributes(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "v1Enabled",
            "forceBasicAuth",
        }
        
        class properties:
            v1Enabled = schemas.BoolSchema
            forceBasicAuth = schemas.BoolSchema
            httpPort = schemas.Int32Schema
            httpsPort = schemas.Int32Schema
            subdomain = schemas.StrSchema
            __annotations__ = {
                "v1Enabled": v1Enabled,
                "forceBasicAuth": forceBasicAuth,
                "httpPort": httpPort,
                "httpsPort": httpsPort,
                "subdomain": subdomain,
            }
    
    v1Enabled: MetaOapg.properties.v1Enabled
    forceBasicAuth: MetaOapg.properties.forceBasicAuth
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["v1Enabled"]) -> MetaOapg.properties.v1Enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forceBasicAuth"]) -> MetaOapg.properties.forceBasicAuth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpPort"]) -> MetaOapg.properties.httpPort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpsPort"]) -> MetaOapg.properties.httpsPort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subdomain"]) -> MetaOapg.properties.subdomain: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["v1Enabled", "forceBasicAuth", "httpPort", "httpsPort", "subdomain", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["v1Enabled"]) -> MetaOapg.properties.v1Enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forceBasicAuth"]) -> MetaOapg.properties.forceBasicAuth: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpPort"]) -> typing.Union[MetaOapg.properties.httpPort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpsPort"]) -> typing.Union[MetaOapg.properties.httpsPort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subdomain"]) -> typing.Union[MetaOapg.properties.subdomain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["v1Enabled", "forceBasicAuth", "httpPort", "httpsPort", "subdomain", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        v1Enabled: typing.Union[MetaOapg.properties.v1Enabled, bool, ],
        forceBasicAuth: typing.Union[MetaOapg.properties.forceBasicAuth, bool, ],
        httpPort: typing.Union[MetaOapg.properties.httpPort, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        httpsPort: typing.Union[MetaOapg.properties.httpsPort, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subdomain: typing.Union[MetaOapg.properties.subdomain, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DockerAttributes':
        return super().__new__(
            cls,
            *_args,
            v1Enabled=v1Enabled,
            forceBasicAuth=forceBasicAuth,
            httpPort=httpPort,
            httpsPort=httpsPort,
            subdomain=subdomain,
            _configuration=_configuration,
            **kwargs,
        )
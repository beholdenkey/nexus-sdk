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


class ApiEmailConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "port",
        }
        
        class properties:
            port = schemas.Int32Schema
            enabled = schemas.BoolSchema
            host = schemas.StrSchema
            username = schemas.StrSchema
            password = schemas.StrSchema
            fromAddress = schemas.StrSchema
            subjectPrefix = schemas.StrSchema
            startTlsEnabled = schemas.BoolSchema
            startTlsRequired = schemas.BoolSchema
            sslOnConnectEnabled = schemas.BoolSchema
            sslServerIdentityCheckEnabled = schemas.BoolSchema
            nexusTrustStoreEnabled = schemas.BoolSchema
            __annotations__ = {
                "port": port,
                "enabled": enabled,
                "host": host,
                "username": username,
                "password": password,
                "fromAddress": fromAddress,
                "subjectPrefix": subjectPrefix,
                "startTlsEnabled": startTlsEnabled,
                "startTlsRequired": startTlsRequired,
                "sslOnConnectEnabled": sslOnConnectEnabled,
                "sslServerIdentityCheckEnabled": sslServerIdentityCheckEnabled,
                "nexusTrustStoreEnabled": nexusTrustStoreEnabled,
            }
    
    port: MetaOapg.properties.port
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromAddress"]) -> MetaOapg.properties.fromAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subjectPrefix"]) -> MetaOapg.properties.subjectPrefix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTlsEnabled"]) -> MetaOapg.properties.startTlsEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTlsRequired"]) -> MetaOapg.properties.startTlsRequired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sslOnConnectEnabled"]) -> MetaOapg.properties.sslOnConnectEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sslServerIdentityCheckEnabled"]) -> MetaOapg.properties.sslServerIdentityCheckEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nexusTrustStoreEnabled"]) -> MetaOapg.properties.nexusTrustStoreEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["port", "enabled", "host", "username", "password", "fromAddress", "subjectPrefix", "startTlsEnabled", "startTlsRequired", "sslOnConnectEnabled", "sslServerIdentityCheckEnabled", "nexusTrustStoreEnabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> typing.Union[MetaOapg.properties.host, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromAddress"]) -> typing.Union[MetaOapg.properties.fromAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subjectPrefix"]) -> typing.Union[MetaOapg.properties.subjectPrefix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTlsEnabled"]) -> typing.Union[MetaOapg.properties.startTlsEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTlsRequired"]) -> typing.Union[MetaOapg.properties.startTlsRequired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sslOnConnectEnabled"]) -> typing.Union[MetaOapg.properties.sslOnConnectEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sslServerIdentityCheckEnabled"]) -> typing.Union[MetaOapg.properties.sslServerIdentityCheckEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nexusTrustStoreEnabled"]) -> typing.Union[MetaOapg.properties.nexusTrustStoreEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["port", "enabled", "host", "username", "password", "fromAddress", "subjectPrefix", "startTlsEnabled", "startTlsRequired", "sslOnConnectEnabled", "sslServerIdentityCheckEnabled", "nexusTrustStoreEnabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        host: typing.Union[MetaOapg.properties.host, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        fromAddress: typing.Union[MetaOapg.properties.fromAddress, str, schemas.Unset] = schemas.unset,
        subjectPrefix: typing.Union[MetaOapg.properties.subjectPrefix, str, schemas.Unset] = schemas.unset,
        startTlsEnabled: typing.Union[MetaOapg.properties.startTlsEnabled, bool, schemas.Unset] = schemas.unset,
        startTlsRequired: typing.Union[MetaOapg.properties.startTlsRequired, bool, schemas.Unset] = schemas.unset,
        sslOnConnectEnabled: typing.Union[MetaOapg.properties.sslOnConnectEnabled, bool, schemas.Unset] = schemas.unset,
        sslServerIdentityCheckEnabled: typing.Union[MetaOapg.properties.sslServerIdentityCheckEnabled, bool, schemas.Unset] = schemas.unset,
        nexusTrustStoreEnabled: typing.Union[MetaOapg.properties.nexusTrustStoreEnabled, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiEmailConfiguration':
        return super().__new__(
            cls,
            *_args,
            port=port,
            enabled=enabled,
            host=host,
            username=username,
            password=password,
            fromAddress=fromAddress,
            subjectPrefix=subjectPrefix,
            startTlsEnabled=startTlsEnabled,
            startTlsRequired=startTlsRequired,
            sslOnConnectEnabled=sslOnConnectEnabled,
            sslServerIdentityCheckEnabled=sslServerIdentityCheckEnabled,
            nexusTrustStoreEnabled=nexusTrustStoreEnabled,
            _configuration=_configuration,
            **kwargs,
        )

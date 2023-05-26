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


class SimpleApiProxyRepository(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "httpClient",
            "proxy",
            "negativeCache",
            "online",
            "storage",
        }
        
        class properties:
            online = schemas.BoolSchema
        
            @staticmethod
            def storage() -> typing.Type['StorageAttributes']:
                return StorageAttributes
        
            @staticmethod
            def proxy() -> typing.Type['ProxyAttributes']:
                return ProxyAttributes
        
            @staticmethod
            def negativeCache() -> typing.Type['NegativeCacheAttributes']:
                return NegativeCacheAttributes
        
            @staticmethod
            def httpClient() -> typing.Type['HttpClientAttributes']:
                return HttpClientAttributes
            
            
            class name(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def cleanup() -> typing.Type['CleanupPolicyAttributes']:
                return CleanupPolicyAttributes
            routingRuleName = schemas.StrSchema
        
            @staticmethod
            def replication() -> typing.Type['ReplicationAttributes']:
                return ReplicationAttributes
            __annotations__ = {
                "online": online,
                "storage": storage,
                "proxy": proxy,
                "negativeCache": negativeCache,
                "httpClient": httpClient,
                "name": name,
                "cleanup": cleanup,
                "routingRuleName": routingRuleName,
                "replication": replication,
            }
    
    httpClient: 'HttpClientAttributes'
    proxy: 'ProxyAttributes'
    negativeCache: 'NegativeCacheAttributes'
    online: MetaOapg.properties.online
    storage: 'StorageAttributes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["online"]) -> MetaOapg.properties.online: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storage"]) -> 'StorageAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proxy"]) -> 'ProxyAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["negativeCache"]) -> 'NegativeCacheAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpClient"]) -> 'HttpClientAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cleanup"]) -> 'CleanupPolicyAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routingRuleName"]) -> MetaOapg.properties.routingRuleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replication"]) -> 'ReplicationAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["online", "storage", "proxy", "negativeCache", "httpClient", "name", "cleanup", "routingRuleName", "replication", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["online"]) -> MetaOapg.properties.online: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storage"]) -> 'StorageAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proxy"]) -> 'ProxyAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["negativeCache"]) -> 'NegativeCacheAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpClient"]) -> 'HttpClientAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cleanup"]) -> typing.Union['CleanupPolicyAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routingRuleName"]) -> typing.Union[MetaOapg.properties.routingRuleName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replication"]) -> typing.Union['ReplicationAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["online", "storage", "proxy", "negativeCache", "httpClient", "name", "cleanup", "routingRuleName", "replication", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        httpClient: 'HttpClientAttributes',
        proxy: 'ProxyAttributes',
        negativeCache: 'NegativeCacheAttributes',
        online: typing.Union[MetaOapg.properties.online, bool, ],
        storage: 'StorageAttributes',
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        cleanup: typing.Union['CleanupPolicyAttributes', schemas.Unset] = schemas.unset,
        routingRuleName: typing.Union[MetaOapg.properties.routingRuleName, str, schemas.Unset] = schemas.unset,
        replication: typing.Union['ReplicationAttributes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SimpleApiProxyRepository':
        return super().__new__(
            cls,
            *_args,
            httpClient=httpClient,
            proxy=proxy,
            negativeCache=negativeCache,
            online=online,
            storage=storage,
            name=name,
            cleanup=cleanup,
            routingRuleName=routingRuleName,
            replication=replication,
            _configuration=_configuration,
            **kwargs,
        )

from nexus_sdk.model.cleanup_policy_attributes import CleanupPolicyAttributes
from nexus_sdk.model.http_client_attributes import HttpClientAttributes
from nexus_sdk.model.negative_cache_attributes import NegativeCacheAttributes
from nexus_sdk.model.proxy_attributes import ProxyAttributes
from nexus_sdk.model.replication_attributes import ReplicationAttributes
from nexus_sdk.model.storage_attributes import StorageAttributes

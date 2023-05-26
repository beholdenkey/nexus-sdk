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


class AptHostedRepositoryApiRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "apt",
            "name",
            "online",
            "storage",
            "aptSigning",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            online = schemas.BoolSchema
        
            @staticmethod
            def storage() -> typing.Type['HostedStorageAttributes']:
                return HostedStorageAttributes
        
            @staticmethod
            def apt() -> typing.Type['AptHostedRepositoriesAttributes']:
                return AptHostedRepositoriesAttributes
        
            @staticmethod
            def aptSigning() -> typing.Type['AptSigningRepositoriesAttributes']:
                return AptSigningRepositoriesAttributes
        
            @staticmethod
            def cleanup() -> typing.Type['CleanupPolicyAttributes']:
                return CleanupPolicyAttributes
        
            @staticmethod
            def component() -> typing.Type['ComponentAttributes']:
                return ComponentAttributes
            __annotations__ = {
                "name": name,
                "online": online,
                "storage": storage,
                "apt": apt,
                "aptSigning": aptSigning,
                "cleanup": cleanup,
                "component": component,
            }
    
    apt: 'AptHostedRepositoriesAttributes'
    name: MetaOapg.properties.name
    online: MetaOapg.properties.online
    storage: 'HostedStorageAttributes'
    aptSigning: 'AptSigningRepositoriesAttributes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["online"]) -> MetaOapg.properties.online: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storage"]) -> 'HostedStorageAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apt"]) -> 'AptHostedRepositoriesAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aptSigning"]) -> 'AptSigningRepositoriesAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cleanup"]) -> 'CleanupPolicyAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["component"]) -> 'ComponentAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "online", "storage", "apt", "aptSigning", "cleanup", "component", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["online"]) -> MetaOapg.properties.online: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storage"]) -> 'HostedStorageAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apt"]) -> 'AptHostedRepositoriesAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aptSigning"]) -> 'AptSigningRepositoriesAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cleanup"]) -> typing.Union['CleanupPolicyAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["component"]) -> typing.Union['ComponentAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "online", "storage", "apt", "aptSigning", "cleanup", "component", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        apt: 'AptHostedRepositoriesAttributes',
        name: typing.Union[MetaOapg.properties.name, str, ],
        online: typing.Union[MetaOapg.properties.online, bool, ],
        storage: 'HostedStorageAttributes',
        aptSigning: 'AptSigningRepositoriesAttributes',
        cleanup: typing.Union['CleanupPolicyAttributes', schemas.Unset] = schemas.unset,
        component: typing.Union['ComponentAttributes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AptHostedRepositoryApiRequest':
        return super().__new__(
            cls,
            *_args,
            apt=apt,
            name=name,
            online=online,
            storage=storage,
            aptSigning=aptSigning,
            cleanup=cleanup,
            component=component,
            _configuration=_configuration,
            **kwargs,
        )

from nexus_sdk.model.apt_hosted_repositories_attributes import AptHostedRepositoriesAttributes
from nexus_sdk.model.apt_signing_repositories_attributes import AptSigningRepositoriesAttributes
from nexus_sdk.model.cleanup_policy_attributes import CleanupPolicyAttributes
from nexus_sdk.model.component_attributes import ComponentAttributes
from nexus_sdk.model.hosted_storage_attributes import HostedStorageAttributes

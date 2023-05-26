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


class DockerGroupRepositoryApiRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "online",
            "storage",
            "docker",
            "group",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            online = schemas.BoolSchema
        
            @staticmethod
            def storage() -> typing.Type['StorageAttributes']:
                return StorageAttributes
        
            @staticmethod
            def group() -> typing.Type['GroupDeployAttributes']:
                return GroupDeployAttributes
        
            @staticmethod
            def docker() -> typing.Type['DockerAttributes']:
                return DockerAttributes
            __annotations__ = {
                "name": name,
                "online": online,
                "storage": storage,
                "group": group,
                "docker": docker,
            }
    
    name: MetaOapg.properties.name
    online: MetaOapg.properties.online
    storage: 'StorageAttributes'
    docker: 'DockerAttributes'
    group: 'GroupDeployAttributes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["online"]) -> MetaOapg.properties.online: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storage"]) -> 'StorageAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group"]) -> 'GroupDeployAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["docker"]) -> 'DockerAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "online", "storage", "group", "docker", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["online"]) -> MetaOapg.properties.online: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storage"]) -> 'StorageAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group"]) -> 'GroupDeployAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["docker"]) -> 'DockerAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "online", "storage", "group", "docker", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        online: typing.Union[MetaOapg.properties.online, bool, ],
        storage: 'StorageAttributes',
        docker: 'DockerAttributes',
        group: 'GroupDeployAttributes',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DockerGroupRepositoryApiRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            online=online,
            storage=storage,
            docker=docker,
            group=group,
            _configuration=_configuration,
            **kwargs,
        )

from nexus_sdk.model.docker_attributes import DockerAttributes
from nexus_sdk.model.group_deploy_attributes import GroupDeployAttributes
from nexus_sdk.model.storage_attributes import StorageAttributes

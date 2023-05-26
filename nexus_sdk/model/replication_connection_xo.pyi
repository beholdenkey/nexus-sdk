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


class ReplicationConnectionXO(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "destinationInstanceUrl",
            "name",
            "destinationRepositoryName",
            "sourceRepositoryName",
        }
        
        class properties:
            name = schemas.StrSchema
            sourceRepositoryName = schemas.StrSchema
            destinationInstanceUrl = schemas.StrSchema
            destinationRepositoryName = schemas.StrSchema
            id = schemas.StrSchema
            destinationInstanceUsername = schemas.StrSchema
            destinationInstancePassword = schemas.StrSchema
            
            
            class contentRegexes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contentRegexes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            includeExistingContent = schemas.BoolSchema
            useTrustStore = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "sourceRepositoryName": sourceRepositoryName,
                "destinationInstanceUrl": destinationInstanceUrl,
                "destinationRepositoryName": destinationRepositoryName,
                "id": id,
                "destinationInstanceUsername": destinationInstanceUsername,
                "destinationInstancePassword": destinationInstancePassword,
                "contentRegexes": contentRegexes,
                "includeExistingContent": includeExistingContent,
                "useTrustStore": useTrustStore,
            }
    
    destinationInstanceUrl: MetaOapg.properties.destinationInstanceUrl
    name: MetaOapg.properties.name
    destinationRepositoryName: MetaOapg.properties.destinationRepositoryName
    sourceRepositoryName: MetaOapg.properties.sourceRepositoryName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceRepositoryName"]) -> MetaOapg.properties.sourceRepositoryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationInstanceUrl"]) -> MetaOapg.properties.destinationInstanceUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationRepositoryName"]) -> MetaOapg.properties.destinationRepositoryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationInstanceUsername"]) -> MetaOapg.properties.destinationInstanceUsername: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationInstancePassword"]) -> MetaOapg.properties.destinationInstancePassword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentRegexes"]) -> MetaOapg.properties.contentRegexes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeExistingContent"]) -> MetaOapg.properties.includeExistingContent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useTrustStore"]) -> MetaOapg.properties.useTrustStore: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "sourceRepositoryName", "destinationInstanceUrl", "destinationRepositoryName", "id", "destinationInstanceUsername", "destinationInstancePassword", "contentRegexes", "includeExistingContent", "useTrustStore", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceRepositoryName"]) -> MetaOapg.properties.sourceRepositoryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationInstanceUrl"]) -> MetaOapg.properties.destinationInstanceUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationRepositoryName"]) -> MetaOapg.properties.destinationRepositoryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationInstanceUsername"]) -> typing.Union[MetaOapg.properties.destinationInstanceUsername, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationInstancePassword"]) -> typing.Union[MetaOapg.properties.destinationInstancePassword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentRegexes"]) -> typing.Union[MetaOapg.properties.contentRegexes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeExistingContent"]) -> typing.Union[MetaOapg.properties.includeExistingContent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useTrustStore"]) -> typing.Union[MetaOapg.properties.useTrustStore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "sourceRepositoryName", "destinationInstanceUrl", "destinationRepositoryName", "id", "destinationInstanceUsername", "destinationInstancePassword", "contentRegexes", "includeExistingContent", "useTrustStore", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        destinationInstanceUrl: typing.Union[MetaOapg.properties.destinationInstanceUrl, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        destinationRepositoryName: typing.Union[MetaOapg.properties.destinationRepositoryName, str, ],
        sourceRepositoryName: typing.Union[MetaOapg.properties.sourceRepositoryName, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        destinationInstanceUsername: typing.Union[MetaOapg.properties.destinationInstanceUsername, str, schemas.Unset] = schemas.unset,
        destinationInstancePassword: typing.Union[MetaOapg.properties.destinationInstancePassword, str, schemas.Unset] = schemas.unset,
        contentRegexes: typing.Union[MetaOapg.properties.contentRegexes, list, tuple, schemas.Unset] = schemas.unset,
        includeExistingContent: typing.Union[MetaOapg.properties.includeExistingContent, bool, schemas.Unset] = schemas.unset,
        useTrustStore: typing.Union[MetaOapg.properties.useTrustStore, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReplicationConnectionXO':
        return super().__new__(
            cls,
            *_args,
            destinationInstanceUrl=destinationInstanceUrl,
            name=name,
            destinationRepositoryName=destinationRepositoryName,
            sourceRepositoryName=sourceRepositoryName,
            id=id,
            destinationInstanceUsername=destinationInstanceUsername,
            destinationInstancePassword=destinationInstancePassword,
            contentRegexes=contentRegexes,
            includeExistingContent=includeExistingContent,
            useTrustStore=useTrustStore,
            _configuration=_configuration,
            **kwargs,
        )

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


class GroupBlobStoreApiCreateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def softQuota() -> typing.Type['BlobStoreApiSoftQuota']:
                return BlobStoreApiSoftQuota
            
            
            class members(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'members':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class fillPolicy(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ROUND_ROBIN(cls):
                    return cls("roundRobin")
                
                @schemas.classproperty
                def WRITE_TO_FIRST(cls):
                    return cls("writeToFirst")
            name = schemas.StrSchema
            __annotations__ = {
                "softQuota": softQuota,
                "members": members,
                "fillPolicy": fillPolicy,
                "name": name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["softQuota"]) -> 'BlobStoreApiSoftQuota': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fillPolicy"]) -> MetaOapg.properties.fillPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["softQuota", "members", "fillPolicy", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["softQuota"]) -> typing.Union['BlobStoreApiSoftQuota', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> typing.Union[MetaOapg.properties.members, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fillPolicy"]) -> typing.Union[MetaOapg.properties.fillPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["softQuota", "members", "fillPolicy", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        softQuota: typing.Union['BlobStoreApiSoftQuota', schemas.Unset] = schemas.unset,
        members: typing.Union[MetaOapg.properties.members, list, tuple, schemas.Unset] = schemas.unset,
        fillPolicy: typing.Union[MetaOapg.properties.fillPolicy, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupBlobStoreApiCreateRequest':
        return super().__new__(
            cls,
            *_args,
            softQuota=softQuota,
            members=members,
            fillPolicy=fillPolicy,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from nexus_sdk.model.blob_store_api_soft_quota import BlobStoreApiSoftQuota

# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401

from nexus_sdk import schemas  # noqa: F401


class AzureConnectionXO(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            accountName = schemas.StrSchema
            accountKey = schemas.StrSchema
            containerName = schemas.StrSchema
            authenticationMethod = schemas.StrSchema
            __annotations__ = {
                "accountName": accountName,
                "accountKey": accountKey,
                "containerName": containerName,
                "authenticationMethod": authenticationMethod,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["accountName"]
    ) -> MetaOapg.properties.accountName:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["accountKey"]
    ) -> MetaOapg.properties.accountKey:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["containerName"]
    ) -> MetaOapg.properties.containerName:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["authenticationMethod"]
    ) -> MetaOapg.properties.authenticationMethod:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "accountName",
                "accountKey",
                "containerName",
                "authenticationMethod",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["accountName"]
    ) -> typing.Union[MetaOapg.properties.accountName, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["accountKey"]
    ) -> typing.Union[MetaOapg.properties.accountKey, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["containerName"]
    ) -> typing.Union[MetaOapg.properties.containerName, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["authenticationMethod"]
    ) -> typing.Union[MetaOapg.properties.authenticationMethod, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "accountName",
                "accountKey",
                "containerName",
                "authenticationMethod",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        accountName: typing.Union[
            MetaOapg.properties.accountName, str, schemas.Unset
        ] = schemas.unset,
        accountKey: typing.Union[
            MetaOapg.properties.accountKey, str, schemas.Unset
        ] = schemas.unset,
        containerName: typing.Union[
            MetaOapg.properties.containerName, str, schemas.Unset
        ] = schemas.unset,
        authenticationMethod: typing.Union[
            MetaOapg.properties.authenticationMethod, str, schemas.Unset
        ] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "AzureConnectionXO":
        return super().__new__(
            cls,
            *_args,
            accountName=accountName,
            accountKey=accountKey,
            containerName=containerName,
            authenticationMethod=authenticationMethod,
            _configuration=_configuration,
            **kwargs,
        )

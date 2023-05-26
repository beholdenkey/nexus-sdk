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


class ProxyAttributes(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "contentMaxAge",
            "metadataMaxAge",
        }

        class properties:
            contentMaxAge = schemas.Int32Schema
            metadataMaxAge = schemas.Int32Schema
            remoteUrl = schemas.StrSchema
            __annotations__ = {
                "contentMaxAge": contentMaxAge,
                "metadataMaxAge": metadataMaxAge,
                "remoteUrl": remoteUrl,
            }

    contentMaxAge: MetaOapg.properties.contentMaxAge
    metadataMaxAge: MetaOapg.properties.metadataMaxAge

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["contentMaxAge"]
    ) -> MetaOapg.properties.contentMaxAge:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["metadataMaxAge"]
    ) -> MetaOapg.properties.metadataMaxAge:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["remoteUrl"]
    ) -> MetaOapg.properties.remoteUrl:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "contentMaxAge",
                "metadataMaxAge",
                "remoteUrl",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["contentMaxAge"]
    ) -> MetaOapg.properties.contentMaxAge:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["metadataMaxAge"]
    ) -> MetaOapg.properties.metadataMaxAge:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["remoteUrl"]
    ) -> typing.Union[MetaOapg.properties.remoteUrl, schemas.Unset]:
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
                "contentMaxAge",
                "metadataMaxAge",
                "remoteUrl",
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
        contentMaxAge: typing.Union[
            MetaOapg.properties.contentMaxAge,
            decimal.Decimal,
            int,
        ],
        metadataMaxAge: typing.Union[
            MetaOapg.properties.metadataMaxAge,
            decimal.Decimal,
            int,
        ],
        remoteUrl: typing.Union[
            MetaOapg.properties.remoteUrl, str, schemas.Unset
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
    ) -> "ProxyAttributes":
        return super().__new__(
            cls,
            *_args,
            contentMaxAge=contentMaxAge,
            metadataMaxAge=metadataMaxAge,
            remoteUrl=remoteUrl,
            _configuration=_configuration,
            **kwargs,
        )

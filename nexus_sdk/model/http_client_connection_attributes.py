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


class HttpClientConnectionAttributes(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            class retries(schemas.Int32Schema):
                class MetaOapg:
                    format = "int32"
                    inclusive_maximum = 10
                    inclusive_minimum = 0

            userAgentSuffix = schemas.StrSchema

            class timeout(schemas.Int32Schema):
                class MetaOapg:
                    format = "int32"
                    inclusive_maximum = 3600
                    inclusive_minimum = 1

            enableCircularRedirects = schemas.BoolSchema
            enableCookies = schemas.BoolSchema
            useTrustStore = schemas.BoolSchema
            __annotations__ = {
                "retries": retries,
                "userAgentSuffix": userAgentSuffix,
                "timeout": timeout,
                "enableCircularRedirects": enableCircularRedirects,
                "enableCookies": enableCookies,
                "useTrustStore": useTrustStore,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["retries"]
    ) -> MetaOapg.properties.retries:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["userAgentSuffix"]
    ) -> MetaOapg.properties.userAgentSuffix:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["timeout"]
    ) -> MetaOapg.properties.timeout:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["enableCircularRedirects"]
    ) -> MetaOapg.properties.enableCircularRedirects:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["enableCookies"]
    ) -> MetaOapg.properties.enableCookies:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["useTrustStore"]
    ) -> MetaOapg.properties.useTrustStore:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "retries",
                "userAgentSuffix",
                "timeout",
                "enableCircularRedirects",
                "enableCookies",
                "useTrustStore",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["retries"]
    ) -> typing.Union[MetaOapg.properties.retries, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["userAgentSuffix"]
    ) -> typing.Union[MetaOapg.properties.userAgentSuffix, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["timeout"]
    ) -> typing.Union[MetaOapg.properties.timeout, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["enableCircularRedirects"]
    ) -> typing.Union[MetaOapg.properties.enableCircularRedirects, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["enableCookies"]
    ) -> typing.Union[MetaOapg.properties.enableCookies, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["useTrustStore"]
    ) -> typing.Union[MetaOapg.properties.useTrustStore, schemas.Unset]:
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
                "retries",
                "userAgentSuffix",
                "timeout",
                "enableCircularRedirects",
                "enableCookies",
                "useTrustStore",
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
        retries: typing.Union[
            MetaOapg.properties.retries, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        userAgentSuffix: typing.Union[
            MetaOapg.properties.userAgentSuffix, str, schemas.Unset
        ] = schemas.unset,
        timeout: typing.Union[
            MetaOapg.properties.timeout, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        enableCircularRedirects: typing.Union[
            MetaOapg.properties.enableCircularRedirects, bool, schemas.Unset
        ] = schemas.unset,
        enableCookies: typing.Union[
            MetaOapg.properties.enableCookies, bool, schemas.Unset
        ] = schemas.unset,
        useTrustStore: typing.Union[
            MetaOapg.properties.useTrustStore, bool, schemas.Unset
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
    ) -> "HttpClientConnectionAttributes":
        return super().__new__(
            cls,
            *_args,
            retries=retries,
            userAgentSuffix=userAgentSuffix,
            timeout=timeout,
            enableCircularRedirects=enableCircularRedirects,
            enableCookies=enableCookies,
            useTrustStore=useTrustStore,
            _configuration=_configuration,
            **kwargs,
        )

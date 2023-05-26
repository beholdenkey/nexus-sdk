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


class MavenProxyRepositoryApiRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "httpClient",
            "proxy",
            "negativeCache",
            "maven",
            "name",
            "online",
            "storage",
        }

        class properties:
            class name(schemas.StrSchema):
                class MetaOapg:
                    regex = [
                        {
                            "pattern": r"^[a-zA-Z0-9\-]{1}[a-zA-Z0-9_\-\.]*$",  # noqa: E501
                        }
                    ]

            online = schemas.BoolSchema

            @staticmethod
            def storage() -> typing.Type["StorageAttributes"]:
                return StorageAttributes

            @staticmethod
            def proxy() -> typing.Type["ProxyAttributes"]:
                return ProxyAttributes

            @staticmethod
            def negativeCache() -> typing.Type["NegativeCacheAttributes"]:
                return NegativeCacheAttributes

            @staticmethod
            def httpClient() -> typing.Type["HttpClientAttributesWithPreemptiveAuth"]:
                return HttpClientAttributesWithPreemptiveAuth

            @staticmethod
            def maven() -> typing.Type["MavenAttributes"]:
                return MavenAttributes

            @staticmethod
            def cleanup() -> typing.Type["CleanupPolicyAttributes"]:
                return CleanupPolicyAttributes

            routingRule = schemas.StrSchema

            @staticmethod
            def replication() -> typing.Type["ReplicationAttributes"]:
                return ReplicationAttributes

            __annotations__ = {
                "name": name,
                "online": online,
                "storage": storage,
                "proxy": proxy,
                "negativeCache": negativeCache,
                "httpClient": httpClient,
                "maven": maven,
                "cleanup": cleanup,
                "routingRule": routingRule,
                "replication": replication,
            }

    httpClient: "HttpClientAttributesWithPreemptiveAuth"
    proxy: "ProxyAttributes"
    negativeCache: "NegativeCacheAttributes"
    maven: "MavenAttributes"
    name: MetaOapg.properties.name
    online: MetaOapg.properties.online
    storage: "StorageAttributes"

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["online"]
    ) -> MetaOapg.properties.online:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["storage"]
    ) -> "StorageAttributes":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["proxy"]
    ) -> "ProxyAttributes":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["negativeCache"]
    ) -> "NegativeCacheAttributes":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["httpClient"]
    ) -> "HttpClientAttributesWithPreemptiveAuth":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["maven"]
    ) -> "MavenAttributes":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["cleanup"]
    ) -> "CleanupPolicyAttributes":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["routingRule"]
    ) -> MetaOapg.properties.routingRule:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["replication"]
    ) -> "ReplicationAttributes":
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "name",
                "online",
                "storage",
                "proxy",
                "negativeCache",
                "httpClient",
                "maven",
                "cleanup",
                "routingRule",
                "replication",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["online"]
    ) -> MetaOapg.properties.online:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["storage"]
    ) -> "StorageAttributes":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["proxy"]
    ) -> "ProxyAttributes":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["negativeCache"]
    ) -> "NegativeCacheAttributes":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["httpClient"]
    ) -> "HttpClientAttributesWithPreemptiveAuth":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["maven"]
    ) -> "MavenAttributes":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["cleanup"]
    ) -> typing.Union["CleanupPolicyAttributes", schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["routingRule"]
    ) -> typing.Union[MetaOapg.properties.routingRule, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["replication"]
    ) -> typing.Union["ReplicationAttributes", schemas.Unset]:
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
                "name",
                "online",
                "storage",
                "proxy",
                "negativeCache",
                "httpClient",
                "maven",
                "cleanup",
                "routingRule",
                "replication",
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
        httpClient: "HttpClientAttributesWithPreemptiveAuth",
        proxy: "ProxyAttributes",
        negativeCache: "NegativeCacheAttributes",
        maven: "MavenAttributes",
        name: typing.Union[
            MetaOapg.properties.name,
            str,
        ],
        online: typing.Union[
            MetaOapg.properties.online,
            bool,
        ],
        storage: "StorageAttributes",
        cleanup: typing.Union["CleanupPolicyAttributes", schemas.Unset] = schemas.unset,
        routingRule: typing.Union[
            MetaOapg.properties.routingRule, str, schemas.Unset
        ] = schemas.unset,
        replication: typing.Union[
            "ReplicationAttributes", schemas.Unset
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
    ) -> "MavenProxyRepositoryApiRequest":
        return super().__new__(
            cls,
            *_args,
            httpClient=httpClient,
            proxy=proxy,
            negativeCache=negativeCache,
            maven=maven,
            name=name,
            online=online,
            storage=storage,
            cleanup=cleanup,
            routingRule=routingRule,
            replication=replication,
            _configuration=_configuration,
            **kwargs,
        )


from nexus_sdk.model.cleanup_policy_attributes import CleanupPolicyAttributes
from nexus_sdk.model.http_client_attributes_with_preemptive_auth import (
    HttpClientAttributesWithPreemptiveAuth,
)
from nexus_sdk.model.maven_attributes import MavenAttributes
from nexus_sdk.model.negative_cache_attributes import NegativeCacheAttributes
from nexus_sdk.model.proxy_attributes import ProxyAttributes
from nexus_sdk.model.replication_attributes import ReplicationAttributes
from nexus_sdk.model.storage_attributes import StorageAttributes

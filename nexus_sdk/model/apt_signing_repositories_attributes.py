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


class AptSigningRepositoriesAttributes(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            keypair = schemas.StrSchema
            passphrase = schemas.StrSchema
            __annotations__ = {
                "keypair": keypair,
                "passphrase": passphrase,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["keypair"]
    ) -> MetaOapg.properties.keypair:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["passphrase"]
    ) -> MetaOapg.properties.passphrase:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "keypair",
                "passphrase",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["keypair"]
    ) -> typing.Union[MetaOapg.properties.keypair, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["passphrase"]
    ) -> typing.Union[MetaOapg.properties.passphrase, schemas.Unset]:
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
                "keypair",
                "passphrase",
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
        keypair: typing.Union[
            MetaOapg.properties.keypair, str, schemas.Unset
        ] = schemas.unset,
        passphrase: typing.Union[
            MetaOapg.properties.passphrase, str, schemas.Unset
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
    ) -> "AptSigningRepositoriesAttributes":
        return super().__new__(
            cls,
            *_args,
            keypair=keypair,
            passphrase=passphrase,
            _configuration=_configuration,
            **kwargs,
        )

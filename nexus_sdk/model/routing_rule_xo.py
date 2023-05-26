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


class RoutingRuleXO(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            class name(schemas.StrSchema):
                class MetaOapg:
                    regex = [
                        {
                            "pattern": r"^[a-zA-Z0-9\-]{1}[a-zA-Z0-9_\-\.]*$",  # noqa: E501
                        }
                    ]

            description = schemas.StrSchema

            class mode(schemas.EnumBase, schemas.StrSchema):
                class MetaOapg:
                    enum_value_to_name = {
                        "BLOCK": "BLOCK",
                        "ALLOW": "ALLOW",
                    }

                @schemas.classproperty
                def BLOCK(cls):
                    return cls("BLOCK")

                @schemas.classproperty
                def ALLOW(cls):
                    return cls("ALLOW")

            class matchers(schemas.ListSchema):
                class MetaOapg:
                    items = schemas.StrSchema

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                MetaOapg.items,
                                str,
                            ]
                        ],
                        typing.List[
                            typing.Union[
                                MetaOapg.items,
                                str,
                            ]
                        ],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "matchers":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            __annotations__ = {
                "name": name,
                "description": description,
                "mode": mode,
                "matchers": matchers,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["description"]
    ) -> MetaOapg.properties.description:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["mode"]
    ) -> MetaOapg.properties.mode:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["matchers"]
    ) -> MetaOapg.properties.matchers:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "name",
                "description",
                "mode",
                "matchers",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> typing.Union[MetaOapg.properties.name, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["description"]
    ) -> typing.Union[MetaOapg.properties.description, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["mode"]
    ) -> typing.Union[MetaOapg.properties.mode, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["matchers"]
    ) -> typing.Union[MetaOapg.properties.matchers, schemas.Unset]:
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
                "description",
                "mode",
                "matchers",
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
        name: typing.Union[
            MetaOapg.properties.name, str, schemas.Unset
        ] = schemas.unset,
        description: typing.Union[
            MetaOapg.properties.description, str, schemas.Unset
        ] = schemas.unset,
        mode: typing.Union[
            MetaOapg.properties.mode, str, schemas.Unset
        ] = schemas.unset,
        matchers: typing.Union[
            MetaOapg.properties.matchers, list, tuple, schemas.Unset
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
    ) -> "RoutingRuleXO":
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            mode=mode,
            matchers=matchers,
            _configuration=_configuration,
            **kwargs,
        )

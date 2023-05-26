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


class PageTaskXO(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            class items(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["TaskXO"]:
                        return TaskXO

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple["TaskXO"], typing.List["TaskXO"]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "items":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> "TaskXO":
                    return super().__getitem__(i)

            continuationToken = schemas.StrSchema
            __annotations__ = {
                "items": items,
                "continuationToken": continuationToken,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["items"]
    ) -> MetaOapg.properties.items:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["continuationToken"]
    ) -> MetaOapg.properties.continuationToken:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "items",
                "continuationToken",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["items"]
    ) -> typing.Union[MetaOapg.properties.items, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["continuationToken"]
    ) -> typing.Union[MetaOapg.properties.continuationToken, schemas.Unset]:
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
                "items",
                "continuationToken",
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
        items: typing.Union[
            MetaOapg.properties.items, list, tuple, schemas.Unset
        ] = schemas.unset,
        continuationToken: typing.Union[
            MetaOapg.properties.continuationToken, str, schemas.Unset
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
    ) -> "PageTaskXO":
        return super().__new__(
            cls,
            *_args,
            items=items,
            continuationToken=continuationToken,
            _configuration=_configuration,
            **kwargs,
        )


from nexus_sdk.model.task_xo import TaskXO

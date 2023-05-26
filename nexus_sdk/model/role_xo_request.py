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


class RoleXORequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            description = schemas.StrSchema

            class privileges(schemas.ListSchema):
                class MetaOapg:
                    unique_items = True
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
                ) -> "privileges":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            class roles(schemas.ListSchema):
                class MetaOapg:
                    unique_items = True
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
                ) -> "roles":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            __annotations__ = {
                "id": id,
                "name": name,
                "description": description,
                "privileges": privileges,
                "roles": roles,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

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
        self, name: typing_extensions.Literal["privileges"]
    ) -> MetaOapg.properties.privileges:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["roles"]
    ) -> MetaOapg.properties.roles:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "id",
                "name",
                "description",
                "privileges",
                "roles",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> typing.Union[MetaOapg.properties.id, schemas.Unset]:
        ...

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
        self, name: typing_extensions.Literal["privileges"]
    ) -> typing.Union[MetaOapg.properties.privileges, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["roles"]
    ) -> typing.Union[MetaOapg.properties.roles, schemas.Unset]:
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
                "id",
                "name",
                "description",
                "privileges",
                "roles",
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
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[
            MetaOapg.properties.name, str, schemas.Unset
        ] = schemas.unset,
        description: typing.Union[
            MetaOapg.properties.description, str, schemas.Unset
        ] = schemas.unset,
        privileges: typing.Union[
            MetaOapg.properties.privileges, list, tuple, schemas.Unset
        ] = schemas.unset,
        roles: typing.Union[
            MetaOapg.properties.roles, list, tuple, schemas.Unset
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
    ) -> "RoleXORequest":
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            description=description,
            privileges=privileges,
            roles=roles,
            _configuration=_configuration,
            **kwargs,
        )

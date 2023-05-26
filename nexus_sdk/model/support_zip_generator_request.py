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


class SupportZipGeneratorRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            systemInformation = schemas.BoolSchema
            threadDump = schemas.BoolSchema
            metrics = schemas.BoolSchema
            configuration = schemas.BoolSchema
            security = schemas.BoolSchema
            log = schemas.BoolSchema
            taskLog = schemas.BoolSchema
            auditLog = schemas.BoolSchema
            jmx = schemas.BoolSchema
            replication = schemas.BoolSchema
            limitFileSizes = schemas.BoolSchema
            limitZipSize = schemas.BoolSchema
            __annotations__ = {
                "systemInformation": systemInformation,
                "threadDump": threadDump,
                "metrics": metrics,
                "configuration": configuration,
                "security": security,
                "log": log,
                "taskLog": taskLog,
                "auditLog": auditLog,
                "jmx": jmx,
                "replication": replication,
                "limitFileSizes": limitFileSizes,
                "limitZipSize": limitZipSize,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["systemInformation"]
    ) -> MetaOapg.properties.systemInformation:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["threadDump"]
    ) -> MetaOapg.properties.threadDump:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["metrics"]
    ) -> MetaOapg.properties.metrics:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["configuration"]
    ) -> MetaOapg.properties.configuration:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["security"]
    ) -> MetaOapg.properties.security:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["log"]
    ) -> MetaOapg.properties.log:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["taskLog"]
    ) -> MetaOapg.properties.taskLog:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["auditLog"]
    ) -> MetaOapg.properties.auditLog:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["jmx"]
    ) -> MetaOapg.properties.jmx:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["replication"]
    ) -> MetaOapg.properties.replication:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["limitFileSizes"]
    ) -> MetaOapg.properties.limitFileSizes:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["limitZipSize"]
    ) -> MetaOapg.properties.limitZipSize:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "systemInformation",
                "threadDump",
                "metrics",
                "configuration",
                "security",
                "log",
                "taskLog",
                "auditLog",
                "jmx",
                "replication",
                "limitFileSizes",
                "limitZipSize",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["systemInformation"]
    ) -> typing.Union[MetaOapg.properties.systemInformation, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["threadDump"]
    ) -> typing.Union[MetaOapg.properties.threadDump, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["metrics"]
    ) -> typing.Union[MetaOapg.properties.metrics, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["configuration"]
    ) -> typing.Union[MetaOapg.properties.configuration, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["security"]
    ) -> typing.Union[MetaOapg.properties.security, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["log"]
    ) -> typing.Union[MetaOapg.properties.log, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["taskLog"]
    ) -> typing.Union[MetaOapg.properties.taskLog, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["auditLog"]
    ) -> typing.Union[MetaOapg.properties.auditLog, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["jmx"]
    ) -> typing.Union[MetaOapg.properties.jmx, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["replication"]
    ) -> typing.Union[MetaOapg.properties.replication, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["limitFileSizes"]
    ) -> typing.Union[MetaOapg.properties.limitFileSizes, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["limitZipSize"]
    ) -> typing.Union[MetaOapg.properties.limitZipSize, schemas.Unset]:
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
                "systemInformation",
                "threadDump",
                "metrics",
                "configuration",
                "security",
                "log",
                "taskLog",
                "auditLog",
                "jmx",
                "replication",
                "limitFileSizes",
                "limitZipSize",
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
        systemInformation: typing.Union[
            MetaOapg.properties.systemInformation, bool, schemas.Unset
        ] = schemas.unset,
        threadDump: typing.Union[
            MetaOapg.properties.threadDump, bool, schemas.Unset
        ] = schemas.unset,
        metrics: typing.Union[
            MetaOapg.properties.metrics, bool, schemas.Unset
        ] = schemas.unset,
        configuration: typing.Union[
            MetaOapg.properties.configuration, bool, schemas.Unset
        ] = schemas.unset,
        security: typing.Union[
            MetaOapg.properties.security, bool, schemas.Unset
        ] = schemas.unset,
        log: typing.Union[MetaOapg.properties.log, bool, schemas.Unset] = schemas.unset,
        taskLog: typing.Union[
            MetaOapg.properties.taskLog, bool, schemas.Unset
        ] = schemas.unset,
        auditLog: typing.Union[
            MetaOapg.properties.auditLog, bool, schemas.Unset
        ] = schemas.unset,
        jmx: typing.Union[MetaOapg.properties.jmx, bool, schemas.Unset] = schemas.unset,
        replication: typing.Union[
            MetaOapg.properties.replication, bool, schemas.Unset
        ] = schemas.unset,
        limitFileSizes: typing.Union[
            MetaOapg.properties.limitFileSizes, bool, schemas.Unset
        ] = schemas.unset,
        limitZipSize: typing.Union[
            MetaOapg.properties.limitZipSize, bool, schemas.Unset
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
    ) -> "SupportZipGeneratorRequest":
        return super().__new__(
            cls,
            *_args,
            systemInformation=systemInformation,
            threadDump=threadDump,
            metrics=metrics,
            configuration=configuration,
            security=security,
            log=log,
            taskLog=taskLog,
            auditLog=auditLog,
            jmx=jmx,
            replication=replication,
            limitFileSizes=limitFileSizes,
            limitZipSize=limitZipSize,
            _configuration=_configuration,
            **kwargs,
        )

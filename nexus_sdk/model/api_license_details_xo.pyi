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


class ApiLicenseDetailsXO(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            contactEmail = schemas.StrSchema
            contactCompany = schemas.StrSchema
            contactName = schemas.StrSchema
            effectiveDate = schemas.DateTimeSchema
            expirationDate = schemas.DateTimeSchema
            licenseType = schemas.StrSchema
            licensedUsers = schemas.StrSchema
            fingerprint = schemas.StrSchema
            features = schemas.StrSchema
            __annotations__ = {
                "contactEmail": contactEmail,
                "contactCompany": contactCompany,
                "contactName": contactName,
                "effectiveDate": effectiveDate,
                "expirationDate": expirationDate,
                "licenseType": licenseType,
                "licensedUsers": licensedUsers,
                "fingerprint": fingerprint,
                "features": features,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactEmail"]) -> MetaOapg.properties.contactEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactCompany"]) -> MetaOapg.properties.contactCompany: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactName"]) -> MetaOapg.properties.contactName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveDate"]) -> MetaOapg.properties.effectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationDate"]) -> MetaOapg.properties.expirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licenseType"]) -> MetaOapg.properties.licenseType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licensedUsers"]) -> MetaOapg.properties.licensedUsers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fingerprint"]) -> MetaOapg.properties.fingerprint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> MetaOapg.properties.features: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contactEmail", "contactCompany", "contactName", "effectiveDate", "expirationDate", "licenseType", "licensedUsers", "fingerprint", "features", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactEmail"]) -> typing.Union[MetaOapg.properties.contactEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactCompany"]) -> typing.Union[MetaOapg.properties.contactCompany, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactName"]) -> typing.Union[MetaOapg.properties.contactName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveDate"]) -> typing.Union[MetaOapg.properties.effectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationDate"]) -> typing.Union[MetaOapg.properties.expirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licenseType"]) -> typing.Union[MetaOapg.properties.licenseType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licensedUsers"]) -> typing.Union[MetaOapg.properties.licensedUsers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fingerprint"]) -> typing.Union[MetaOapg.properties.fingerprint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> typing.Union[MetaOapg.properties.features, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contactEmail", "contactCompany", "contactName", "effectiveDate", "expirationDate", "licenseType", "licensedUsers", "fingerprint", "features", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        contactEmail: typing.Union[MetaOapg.properties.contactEmail, str, schemas.Unset] = schemas.unset,
        contactCompany: typing.Union[MetaOapg.properties.contactCompany, str, schemas.Unset] = schemas.unset,
        contactName: typing.Union[MetaOapg.properties.contactName, str, schemas.Unset] = schemas.unset,
        effectiveDate: typing.Union[MetaOapg.properties.effectiveDate, str, datetime, schemas.Unset] = schemas.unset,
        expirationDate: typing.Union[MetaOapg.properties.expirationDate, str, datetime, schemas.Unset] = schemas.unset,
        licenseType: typing.Union[MetaOapg.properties.licenseType, str, schemas.Unset] = schemas.unset,
        licensedUsers: typing.Union[MetaOapg.properties.licensedUsers, str, schemas.Unset] = schemas.unset,
        fingerprint: typing.Union[MetaOapg.properties.fingerprint, str, schemas.Unset] = schemas.unset,
        features: typing.Union[MetaOapg.properties.features, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiLicenseDetailsXO':
        return super().__new__(
            cls,
            *_args,
            contactEmail=contactEmail,
            contactCompany=contactCompany,
            contactName=contactName,
            effectiveDate=effectiveDate,
            expirationDate=expirationDate,
            licenseType=licenseType,
            licensedUsers=licensedUsers,
            fingerprint=fingerprint,
            features=features,
            _configuration=_configuration,
            **kwargs,
        )

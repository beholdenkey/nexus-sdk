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


class UpdateLdapServerXo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "maxIncidentsCount",
            "groupType",
            "protocol",
            "connectionRetryDelaySeconds",
            "port",
            "searchBase",
            "connectionTimeoutSeconds",
            "host",
            "name",
            "authScheme",
            "authPassword",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class protocol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LDAP(cls):
                    return cls("ldap")
                
                @schemas.classproperty
                def LDAPS(cls):
                    return cls("ldaps")
            host = schemas.StrSchema
            port = schemas.Int32Schema
            searchBase = schemas.StrSchema
            
            
            class authScheme(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
                
                @schemas.classproperty
                def SIMPLE(cls):
                    return cls("SIMPLE")
                
                @schemas.classproperty
                def DIGEST_MD5(cls):
                    return cls("DIGEST_MD5")
                
                @schemas.classproperty
                def CRAM_MD5(cls):
                    return cls("CRAM_MD5")
            
            
            class connectionTimeoutSeconds(
                schemas.Int32Schema
            ):
                pass
            
            
            class connectionRetryDelaySeconds(
                schemas.Int32Schema
            ):
                pass
            
            
            class maxIncidentsCount(
                schemas.Int32Schema
            ):
                pass
            
            
            class groupType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STATIC(cls):
                    return cls("static")
                
                @schemas.classproperty
                def DYNAMIC(cls):
                    return cls("dynamic")
            authPassword = schemas.StrSchema
            useTrustStore = schemas.BoolSchema
            authRealm = schemas.StrSchema
            authUsername = schemas.StrSchema
            userBaseDn = schemas.StrSchema
            userSubtree = schemas.BoolSchema
            userObjectClass = schemas.StrSchema
            userLdapFilter = schemas.StrSchema
            userIdAttribute = schemas.StrSchema
            userRealNameAttribute = schemas.StrSchema
            userEmailAddressAttribute = schemas.StrSchema
            userPasswordAttribute = schemas.StrSchema
            ldapGroupsAsRoles = schemas.BoolSchema
            groupBaseDn = schemas.StrSchema
            groupSubtree = schemas.BoolSchema
            
            
            class groupObjectClass(
                schemas.StrSchema
            ):
                pass
            
            
            class groupIdAttribute(
                schemas.StrSchema
            ):
                pass
            
            
            class groupMemberAttribute(
                schemas.StrSchema
            ):
                pass
            
            
            class groupMemberFormat(
                schemas.StrSchema
            ):
                pass
            
            
            class userMemberOfAttribute(
                schemas.StrSchema
            ):
                pass
            id = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "protocol": protocol,
                "host": host,
                "port": port,
                "searchBase": searchBase,
                "authScheme": authScheme,
                "connectionTimeoutSeconds": connectionTimeoutSeconds,
                "connectionRetryDelaySeconds": connectionRetryDelaySeconds,
                "maxIncidentsCount": maxIncidentsCount,
                "groupType": groupType,
                "authPassword": authPassword,
                "useTrustStore": useTrustStore,
                "authRealm": authRealm,
                "authUsername": authUsername,
                "userBaseDn": userBaseDn,
                "userSubtree": userSubtree,
                "userObjectClass": userObjectClass,
                "userLdapFilter": userLdapFilter,
                "userIdAttribute": userIdAttribute,
                "userRealNameAttribute": userRealNameAttribute,
                "userEmailAddressAttribute": userEmailAddressAttribute,
                "userPasswordAttribute": userPasswordAttribute,
                "ldapGroupsAsRoles": ldapGroupsAsRoles,
                "groupBaseDn": groupBaseDn,
                "groupSubtree": groupSubtree,
                "groupObjectClass": groupObjectClass,
                "groupIdAttribute": groupIdAttribute,
                "groupMemberAttribute": groupMemberAttribute,
                "groupMemberFormat": groupMemberFormat,
                "userMemberOfAttribute": userMemberOfAttribute,
                "id": id,
            }
    
    maxIncidentsCount: MetaOapg.properties.maxIncidentsCount
    groupType: MetaOapg.properties.groupType
    protocol: MetaOapg.properties.protocol
    connectionRetryDelaySeconds: MetaOapg.properties.connectionRetryDelaySeconds
    port: MetaOapg.properties.port
    searchBase: MetaOapg.properties.searchBase
    connectionTimeoutSeconds: MetaOapg.properties.connectionTimeoutSeconds
    host: MetaOapg.properties.host
    name: MetaOapg.properties.name
    authScheme: MetaOapg.properties.authScheme
    authPassword: MetaOapg.properties.authPassword
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searchBase"]) -> MetaOapg.properties.searchBase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authScheme"]) -> MetaOapg.properties.authScheme: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionTimeoutSeconds"]) -> MetaOapg.properties.connectionTimeoutSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionRetryDelaySeconds"]) -> MetaOapg.properties.connectionRetryDelaySeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxIncidentsCount"]) -> MetaOapg.properties.maxIncidentsCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupType"]) -> MetaOapg.properties.groupType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authPassword"]) -> MetaOapg.properties.authPassword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useTrustStore"]) -> MetaOapg.properties.useTrustStore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authRealm"]) -> MetaOapg.properties.authRealm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authUsername"]) -> MetaOapg.properties.authUsername: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userBaseDn"]) -> MetaOapg.properties.userBaseDn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userSubtree"]) -> MetaOapg.properties.userSubtree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userObjectClass"]) -> MetaOapg.properties.userObjectClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userLdapFilter"]) -> MetaOapg.properties.userLdapFilter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userIdAttribute"]) -> MetaOapg.properties.userIdAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userRealNameAttribute"]) -> MetaOapg.properties.userRealNameAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userEmailAddressAttribute"]) -> MetaOapg.properties.userEmailAddressAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userPasswordAttribute"]) -> MetaOapg.properties.userPasswordAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ldapGroupsAsRoles"]) -> MetaOapg.properties.ldapGroupsAsRoles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupBaseDn"]) -> MetaOapg.properties.groupBaseDn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupSubtree"]) -> MetaOapg.properties.groupSubtree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupObjectClass"]) -> MetaOapg.properties.groupObjectClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupIdAttribute"]) -> MetaOapg.properties.groupIdAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupMemberAttribute"]) -> MetaOapg.properties.groupMemberAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupMemberFormat"]) -> MetaOapg.properties.groupMemberFormat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userMemberOfAttribute"]) -> MetaOapg.properties.userMemberOfAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "protocol", "host", "port", "searchBase", "authScheme", "connectionTimeoutSeconds", "connectionRetryDelaySeconds", "maxIncidentsCount", "groupType", "authPassword", "useTrustStore", "authRealm", "authUsername", "userBaseDn", "userSubtree", "userObjectClass", "userLdapFilter", "userIdAttribute", "userRealNameAttribute", "userEmailAddressAttribute", "userPasswordAttribute", "ldapGroupsAsRoles", "groupBaseDn", "groupSubtree", "groupObjectClass", "groupIdAttribute", "groupMemberAttribute", "groupMemberFormat", "userMemberOfAttribute", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searchBase"]) -> MetaOapg.properties.searchBase: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authScheme"]) -> MetaOapg.properties.authScheme: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionTimeoutSeconds"]) -> MetaOapg.properties.connectionTimeoutSeconds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionRetryDelaySeconds"]) -> MetaOapg.properties.connectionRetryDelaySeconds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxIncidentsCount"]) -> MetaOapg.properties.maxIncidentsCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupType"]) -> MetaOapg.properties.groupType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authPassword"]) -> MetaOapg.properties.authPassword: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useTrustStore"]) -> typing.Union[MetaOapg.properties.useTrustStore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authRealm"]) -> typing.Union[MetaOapg.properties.authRealm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authUsername"]) -> typing.Union[MetaOapg.properties.authUsername, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userBaseDn"]) -> typing.Union[MetaOapg.properties.userBaseDn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userSubtree"]) -> typing.Union[MetaOapg.properties.userSubtree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userObjectClass"]) -> typing.Union[MetaOapg.properties.userObjectClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userLdapFilter"]) -> typing.Union[MetaOapg.properties.userLdapFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userIdAttribute"]) -> typing.Union[MetaOapg.properties.userIdAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userRealNameAttribute"]) -> typing.Union[MetaOapg.properties.userRealNameAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userEmailAddressAttribute"]) -> typing.Union[MetaOapg.properties.userEmailAddressAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userPasswordAttribute"]) -> typing.Union[MetaOapg.properties.userPasswordAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ldapGroupsAsRoles"]) -> typing.Union[MetaOapg.properties.ldapGroupsAsRoles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupBaseDn"]) -> typing.Union[MetaOapg.properties.groupBaseDn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupSubtree"]) -> typing.Union[MetaOapg.properties.groupSubtree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupObjectClass"]) -> typing.Union[MetaOapg.properties.groupObjectClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupIdAttribute"]) -> typing.Union[MetaOapg.properties.groupIdAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupMemberAttribute"]) -> typing.Union[MetaOapg.properties.groupMemberAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupMemberFormat"]) -> typing.Union[MetaOapg.properties.groupMemberFormat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userMemberOfAttribute"]) -> typing.Union[MetaOapg.properties.userMemberOfAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "protocol", "host", "port", "searchBase", "authScheme", "connectionTimeoutSeconds", "connectionRetryDelaySeconds", "maxIncidentsCount", "groupType", "authPassword", "useTrustStore", "authRealm", "authUsername", "userBaseDn", "userSubtree", "userObjectClass", "userLdapFilter", "userIdAttribute", "userRealNameAttribute", "userEmailAddressAttribute", "userPasswordAttribute", "ldapGroupsAsRoles", "groupBaseDn", "groupSubtree", "groupObjectClass", "groupIdAttribute", "groupMemberAttribute", "groupMemberFormat", "userMemberOfAttribute", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxIncidentsCount: typing.Union[MetaOapg.properties.maxIncidentsCount, decimal.Decimal, int, ],
        groupType: typing.Union[MetaOapg.properties.groupType, str, ],
        protocol: typing.Union[MetaOapg.properties.protocol, str, ],
        connectionRetryDelaySeconds: typing.Union[MetaOapg.properties.connectionRetryDelaySeconds, decimal.Decimal, int, ],
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, ],
        searchBase: typing.Union[MetaOapg.properties.searchBase, str, ],
        connectionTimeoutSeconds: typing.Union[MetaOapg.properties.connectionTimeoutSeconds, decimal.Decimal, int, ],
        host: typing.Union[MetaOapg.properties.host, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        authScheme: typing.Union[MetaOapg.properties.authScheme, str, ],
        authPassword: typing.Union[MetaOapg.properties.authPassword, str, ],
        useTrustStore: typing.Union[MetaOapg.properties.useTrustStore, bool, schemas.Unset] = schemas.unset,
        authRealm: typing.Union[MetaOapg.properties.authRealm, str, schemas.Unset] = schemas.unset,
        authUsername: typing.Union[MetaOapg.properties.authUsername, str, schemas.Unset] = schemas.unset,
        userBaseDn: typing.Union[MetaOapg.properties.userBaseDn, str, schemas.Unset] = schemas.unset,
        userSubtree: typing.Union[MetaOapg.properties.userSubtree, bool, schemas.Unset] = schemas.unset,
        userObjectClass: typing.Union[MetaOapg.properties.userObjectClass, str, schemas.Unset] = schemas.unset,
        userLdapFilter: typing.Union[MetaOapg.properties.userLdapFilter, str, schemas.Unset] = schemas.unset,
        userIdAttribute: typing.Union[MetaOapg.properties.userIdAttribute, str, schemas.Unset] = schemas.unset,
        userRealNameAttribute: typing.Union[MetaOapg.properties.userRealNameAttribute, str, schemas.Unset] = schemas.unset,
        userEmailAddressAttribute: typing.Union[MetaOapg.properties.userEmailAddressAttribute, str, schemas.Unset] = schemas.unset,
        userPasswordAttribute: typing.Union[MetaOapg.properties.userPasswordAttribute, str, schemas.Unset] = schemas.unset,
        ldapGroupsAsRoles: typing.Union[MetaOapg.properties.ldapGroupsAsRoles, bool, schemas.Unset] = schemas.unset,
        groupBaseDn: typing.Union[MetaOapg.properties.groupBaseDn, str, schemas.Unset] = schemas.unset,
        groupSubtree: typing.Union[MetaOapg.properties.groupSubtree, bool, schemas.Unset] = schemas.unset,
        groupObjectClass: typing.Union[MetaOapg.properties.groupObjectClass, str, schemas.Unset] = schemas.unset,
        groupIdAttribute: typing.Union[MetaOapg.properties.groupIdAttribute, str, schemas.Unset] = schemas.unset,
        groupMemberAttribute: typing.Union[MetaOapg.properties.groupMemberAttribute, str, schemas.Unset] = schemas.unset,
        groupMemberFormat: typing.Union[MetaOapg.properties.groupMemberFormat, str, schemas.Unset] = schemas.unset,
        userMemberOfAttribute: typing.Union[MetaOapg.properties.userMemberOfAttribute, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateLdapServerXo':
        return super().__new__(
            cls,
            *_args,
            maxIncidentsCount=maxIncidentsCount,
            groupType=groupType,
            protocol=protocol,
            connectionRetryDelaySeconds=connectionRetryDelaySeconds,
            port=port,
            searchBase=searchBase,
            connectionTimeoutSeconds=connectionTimeoutSeconds,
            host=host,
            name=name,
            authScheme=authScheme,
            authPassword=authPassword,
            useTrustStore=useTrustStore,
            authRealm=authRealm,
            authUsername=authUsername,
            userBaseDn=userBaseDn,
            userSubtree=userSubtree,
            userObjectClass=userObjectClass,
            userLdapFilter=userLdapFilter,
            userIdAttribute=userIdAttribute,
            userRealNameAttribute=userRealNameAttribute,
            userEmailAddressAttribute=userEmailAddressAttribute,
            userPasswordAttribute=userPasswordAttribute,
            ldapGroupsAsRoles=ldapGroupsAsRoles,
            groupBaseDn=groupBaseDn,
            groupSubtree=groupSubtree,
            groupObjectClass=groupObjectClass,
            groupIdAttribute=groupIdAttribute,
            groupMemberAttribute=groupMemberAttribute,
            groupMemberFormat=groupMemberFormat,
            userMemberOfAttribute=userMemberOfAttribute,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )

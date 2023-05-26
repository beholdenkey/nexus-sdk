# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from nexus_sdk.paths.v1_security_realms_active.get import GetActiveRealms
from nexus_sdk.paths.v1_security_realms_available.get import GetRealms
from nexus_sdk.paths.v1_security_realms_active.put import SetActiveRealms


class SecurityManagementRealmsApi(
    GetActiveRealms,
    GetRealms,
    SetActiveRealms,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

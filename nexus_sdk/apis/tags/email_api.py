# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from nexus_sdk.paths.v1_email.delete import DeleteEmailConfiguration
from nexus_sdk.paths.v1_email.get import GetEmailConfiguration
from nexus_sdk.paths.v1_email.put import SetEmailConfiguration
from nexus_sdk.paths.v1_email_verify.post import TestEmailConfiguration


class EmailApi(
    DeleteEmailConfiguration,
    GetEmailConfiguration,
    SetEmailConfiguration,
    TestEmailConfiguration,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    pass

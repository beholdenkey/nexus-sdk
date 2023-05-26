# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from nexus_sdk.paths.beta_replication_connection.get import CallList
from nexus_sdk.paths.beta_replication_connection.post import Create2
from nexus_sdk.paths.beta_replication_connection_name.delete import Delete3
from nexus_sdk.paths.beta_replicationtarget_repository_repository_name_enable.delete import Disable
from nexus_sdk.paths.beta_replicationtarget_repository_enable.put import Enable
from nexus_sdk.paths.beta_replication_connection_name.get import Get4
from nexus_sdk.paths.beta_replication_connection_name.put import Update2


class ReplicationApi(
    CallList,
    Create2,
    Delete3,
    Disable,
    Enable,
    Get4,
    Update2,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from nexus_sdk.paths.v1_script.get import Browse
from nexus_sdk.paths.v1_script.post import Add
from nexus_sdk.paths.v1_script_name.delete import Delete1
from nexus_sdk.paths.v1_script_name.get import Read1
from nexus_sdk.paths.v1_script_name.put import Edit
from nexus_sdk.paths.v1_script_name_run.post import Run1


class ScriptApi(
    Add,
    Browse,
    Delete1,
    Edit,
    Read1,
    Run1,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    pass

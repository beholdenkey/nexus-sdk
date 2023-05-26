# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from dataclasses import dataclass
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
import urllib3

from nexus_sdk import schemas  # noqa: F401
from nexus_sdk import api_client, exceptions

from . import path

# Query params


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "group": "GROUP",
            "name": "NAME",
            "version": "VERSION",
            "repository": "REPOSITORY",
        }
    
    @schemas.classproperty
    def GROUP(cls):
        return cls("group")
    
    @schemas.classproperty
    def NAME(cls):
        return cls("name")
    
    @schemas.classproperty
    def VERSION(cls):
        return cls("version")
    
    @schemas.classproperty
    def REPOSITORY(cls):
        return cls("repository")


class DirectionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "asc": "ASC",
            "desc": "DESC",
        }
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")
TimeoutSchema = schemas.Int32Schema
QSchema = schemas.StrSchema
RepositorySchema = schemas.StrSchema
FormatSchema = schemas.StrSchema
GroupSchema = schemas.StrSchema
NameSchema = schemas.StrSchema
VersionSchema = schemas.StrSchema
PrereleaseSchema = schemas.StrSchema
Md5Schema = schemas.StrSchema
Sha1Schema = schemas.StrSchema
Sha256Schema = schemas.StrSchema
Sha512Schema = schemas.StrSchema
ConanBaseVersionSchema = schemas.StrSchema
ConanChannelSchema = schemas.StrSchema
DockerImageNameSchema = schemas.StrSchema
DockerImageTagSchema = schemas.StrSchema
DockerLayerIdSchema = schemas.StrSchema
DockerContentDigestSchema = schemas.StrSchema
MavenGroupIdSchema = schemas.StrSchema
MavenArtifactIdSchema = schemas.StrSchema
MavenBaseVersionSchema = schemas.StrSchema
MavenExtensionSchema = schemas.StrSchema
MavenClassifierSchema = schemas.StrSchema
NpmScopeSchema = schemas.StrSchema
NugetIdSchema = schemas.StrSchema
NugetTagsSchema = schemas.StrSchema
P2PluginNameSchema = schemas.StrSchema
PypiClassifiersSchema = schemas.StrSchema
PypiDescriptionSchema = schemas.StrSchema
PypiKeywordsSchema = schemas.StrSchema
PypiSummarySchema = schemas.StrSchema
RubygemsDescriptionSchema = schemas.StrSchema
RubygemsPlatformSchema = schemas.StrSchema
RubygemsSummarySchema = schemas.StrSchema
TagSchema = schemas.StrSchema
YumArchitectureSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'sort': typing.Union[SortSchema, str, ],
        'direction': typing.Union[DirectionSchema, str, ],
        'timeout': typing.Union[TimeoutSchema, decimal.Decimal, int, ],
        'q': typing.Union[QSchema, str, ],
        'repository': typing.Union[RepositorySchema, str, ],
        'format': typing.Union[FormatSchema, str, ],
        'group': typing.Union[GroupSchema, str, ],
        'name': typing.Union[NameSchema, str, ],
        'version': typing.Union[VersionSchema, str, ],
        'prerelease': typing.Union[PrereleaseSchema, str, ],
        'md5': typing.Union[Md5Schema, str, ],
        'sha1': typing.Union[Sha1Schema, str, ],
        'sha256': typing.Union[Sha256Schema, str, ],
        'sha512': typing.Union[Sha512Schema, str, ],
        'conan.baseVersion': typing.Union[ConanBaseVersionSchema, str, ],
        'conan.channel': typing.Union[ConanChannelSchema, str, ],
        'docker.imageName': typing.Union[DockerImageNameSchema, str, ],
        'docker.imageTag': typing.Union[DockerImageTagSchema, str, ],
        'docker.layerId': typing.Union[DockerLayerIdSchema, str, ],
        'docker.contentDigest': typing.Union[DockerContentDigestSchema, str, ],
        'maven.groupId': typing.Union[MavenGroupIdSchema, str, ],
        'maven.artifactId': typing.Union[MavenArtifactIdSchema, str, ],
        'maven.baseVersion': typing.Union[MavenBaseVersionSchema, str, ],
        'maven.extension': typing.Union[MavenExtensionSchema, str, ],
        'maven.classifier': typing.Union[MavenClassifierSchema, str, ],
        'npm.scope': typing.Union[NpmScopeSchema, str, ],
        'nuget.id': typing.Union[NugetIdSchema, str, ],
        'nuget.tags': typing.Union[NugetTagsSchema, str, ],
        'p2.pluginName': typing.Union[P2PluginNameSchema, str, ],
        'pypi.classifiers': typing.Union[PypiClassifiersSchema, str, ],
        'pypi.description': typing.Union[PypiDescriptionSchema, str, ],
        'pypi.keywords': typing.Union[PypiKeywordsSchema, str, ],
        'pypi.summary': typing.Union[PypiSummarySchema, str, ],
        'rubygems.description': typing.Union[RubygemsDescriptionSchema, str, ],
        'rubygems.platform': typing.Union[RubygemsPlatformSchema, str, ],
        'rubygems.summary': typing.Union[RubygemsSummarySchema, str, ],
        'tag': typing.Union[TagSchema, str, ],
        'yum.architecture': typing.Union[YumArchitectureSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_direction = api_client.QueryParameter(
    name="direction",
    style=api_client.ParameterStyle.FORM,
    schema=DirectionSchema,
    explode=True,
)
request_query_timeout = api_client.QueryParameter(
    name="timeout",
    style=api_client.ParameterStyle.FORM,
    schema=TimeoutSchema,
    explode=True,
)
request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
    explode=True,
)
request_query_repository = api_client.QueryParameter(
    name="repository",
    style=api_client.ParameterStyle.FORM,
    schema=RepositorySchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
request_query_group = api_client.QueryParameter(
    name="group",
    style=api_client.ParameterStyle.FORM,
    schema=GroupSchema,
    explode=True,
)
request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    explode=True,
)
request_query_version = api_client.QueryParameter(
    name="version",
    style=api_client.ParameterStyle.FORM,
    schema=VersionSchema,
    explode=True,
)
request_query_prerelease = api_client.QueryParameter(
    name="prerelease",
    style=api_client.ParameterStyle.FORM,
    schema=PrereleaseSchema,
    explode=True,
)
request_query_md5 = api_client.QueryParameter(
    name="md5",
    style=api_client.ParameterStyle.FORM,
    schema=Md5Schema,
    explode=True,
)
request_query_sha1 = api_client.QueryParameter(
    name="sha1",
    style=api_client.ParameterStyle.FORM,
    schema=Sha1Schema,
    explode=True,
)
request_query_sha256 = api_client.QueryParameter(
    name="sha256",
    style=api_client.ParameterStyle.FORM,
    schema=Sha256Schema,
    explode=True,
)
request_query_sha512 = api_client.QueryParameter(
    name="sha512",
    style=api_client.ParameterStyle.FORM,
    schema=Sha512Schema,
    explode=True,
)
request_query_conan_base_version = api_client.QueryParameter(
    name="conan.baseVersion",
    style=api_client.ParameterStyle.FORM,
    schema=ConanBaseVersionSchema,
    explode=True,
)
request_query_conan_channel = api_client.QueryParameter(
    name="conan.channel",
    style=api_client.ParameterStyle.FORM,
    schema=ConanChannelSchema,
    explode=True,
)
request_query_docker_image_name = api_client.QueryParameter(
    name="docker.imageName",
    style=api_client.ParameterStyle.FORM,
    schema=DockerImageNameSchema,
    explode=True,
)
request_query_docker_image_tag = api_client.QueryParameter(
    name="docker.imageTag",
    style=api_client.ParameterStyle.FORM,
    schema=DockerImageTagSchema,
    explode=True,
)
request_query_docker_layer_id = api_client.QueryParameter(
    name="docker.layerId",
    style=api_client.ParameterStyle.FORM,
    schema=DockerLayerIdSchema,
    explode=True,
)
request_query_docker_content_digest = api_client.QueryParameter(
    name="docker.contentDigest",
    style=api_client.ParameterStyle.FORM,
    schema=DockerContentDigestSchema,
    explode=True,
)
request_query_maven_group_id = api_client.QueryParameter(
    name="maven.groupId",
    style=api_client.ParameterStyle.FORM,
    schema=MavenGroupIdSchema,
    explode=True,
)
request_query_maven_artifact_id = api_client.QueryParameter(
    name="maven.artifactId",
    style=api_client.ParameterStyle.FORM,
    schema=MavenArtifactIdSchema,
    explode=True,
)
request_query_maven_base_version = api_client.QueryParameter(
    name="maven.baseVersion",
    style=api_client.ParameterStyle.FORM,
    schema=MavenBaseVersionSchema,
    explode=True,
)
request_query_maven_extension = api_client.QueryParameter(
    name="maven.extension",
    style=api_client.ParameterStyle.FORM,
    schema=MavenExtensionSchema,
    explode=True,
)
request_query_maven_classifier = api_client.QueryParameter(
    name="maven.classifier",
    style=api_client.ParameterStyle.FORM,
    schema=MavenClassifierSchema,
    explode=True,
)
request_query_npm_scope = api_client.QueryParameter(
    name="npm.scope",
    style=api_client.ParameterStyle.FORM,
    schema=NpmScopeSchema,
    explode=True,
)
request_query_nuget_id = api_client.QueryParameter(
    name="nuget.id",
    style=api_client.ParameterStyle.FORM,
    schema=NugetIdSchema,
    explode=True,
)
request_query_nuget_tags = api_client.QueryParameter(
    name="nuget.tags",
    style=api_client.ParameterStyle.FORM,
    schema=NugetTagsSchema,
    explode=True,
)
request_query_p2_plugin_name = api_client.QueryParameter(
    name="p2.pluginName",
    style=api_client.ParameterStyle.FORM,
    schema=P2PluginNameSchema,
    explode=True,
)
request_query_pypi_classifiers = api_client.QueryParameter(
    name="pypi.classifiers",
    style=api_client.ParameterStyle.FORM,
    schema=PypiClassifiersSchema,
    explode=True,
)
request_query_pypi_description = api_client.QueryParameter(
    name="pypi.description",
    style=api_client.ParameterStyle.FORM,
    schema=PypiDescriptionSchema,
    explode=True,
)
request_query_pypi_keywords = api_client.QueryParameter(
    name="pypi.keywords",
    style=api_client.ParameterStyle.FORM,
    schema=PypiKeywordsSchema,
    explode=True,
)
request_query_pypi_summary = api_client.QueryParameter(
    name="pypi.summary",
    style=api_client.ParameterStyle.FORM,
    schema=PypiSummarySchema,
    explode=True,
)
request_query_rubygems_description = api_client.QueryParameter(
    name="rubygems.description",
    style=api_client.ParameterStyle.FORM,
    schema=RubygemsDescriptionSchema,
    explode=True,
)
request_query_rubygems_platform = api_client.QueryParameter(
    name="rubygems.platform",
    style=api_client.ParameterStyle.FORM,
    schema=RubygemsPlatformSchema,
    explode=True,
)
request_query_rubygems_summary = api_client.QueryParameter(
    name="rubygems.summary",
    style=api_client.ParameterStyle.FORM,
    schema=RubygemsSummarySchema,
    explode=True,
)
request_query_tag = api_client.QueryParameter(
    name="tag",
    style=api_client.ParameterStyle.FORM,
    schema=TagSchema,
    explode=True,
)
request_query_yum_architecture = api_client.QueryParameter(
    name="yum.architecture",
    style=api_client.ParameterStyle.FORM,
    schema=YumArchitectureSchema,
    explode=True,
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)
_status_code_to_response = {
    '400': _response_for_400,
    '404': _response_for_404,
}


class BaseApi(api_client.Api):
    @typing.overload
    def _search_and_download_assets_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _search_and_download_assets_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _search_and_download_assets_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _search_and_download_assets_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Search and download asset
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_sort,
            request_query_direction,
            request_query_timeout,
            request_query_q,
            request_query_repository,
            request_query_format,
            request_query_group,
            request_query_name,
            request_query_version,
            request_query_prerelease,
            request_query_md5,
            request_query_sha1,
            request_query_sha256,
            request_query_sha512,
            request_query_conan_base_version,
            request_query_conan_channel,
            request_query_docker_image_name,
            request_query_docker_image_tag,
            request_query_docker_layer_id,
            request_query_docker_content_digest,
            request_query_maven_group_id,
            request_query_maven_artifact_id,
            request_query_maven_base_version,
            request_query_maven_extension,
            request_query_maven_classifier,
            request_query_npm_scope,
            request_query_nuget_id,
            request_query_nuget_tags,
            request_query_p2_plugin_name,
            request_query_pypi_classifiers,
            request_query_pypi_description,
            request_query_pypi_keywords,
            request_query_pypi_summary,
            request_query_rubygems_description,
            request_query_rubygems_platform,
            request_query_rubygems_summary,
            request_query_tag,
            request_query_yum_architecture,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class SearchAndDownloadAssets(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def search_and_download_assets(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def search_and_download_assets(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def search_and_download_assets(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def search_and_download_assets(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_and_download_assets_oapg(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_and_download_assets_oapg(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )



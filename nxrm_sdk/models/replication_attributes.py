"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ReplicationAttributes:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {'preemptive_pull_enabled': 'bool', 'asset_path_regex': 'str'}

    attribute_map = {
        'preemptive_pull_enabled': 'preemptivePullEnabled',
        'asset_path_regex': 'assetPathRegex',
    }

    def __init__(
        self, preemptive_pull_enabled=None, asset_path_regex=None
    ):  # noqa: E501
        """ReplicationAttributes - a model defined in Swagger"""  # noqa: E501
        self._preemptive_pull_enabled = None
        self._asset_path_regex = None
        self.discriminator = None
        self.preemptive_pull_enabled = preemptive_pull_enabled
        if asset_path_regex is not None:
            self.asset_path_regex = asset_path_regex

    @property
    def preemptive_pull_enabled(self):
        """Gets the preemptive_pull_enabled of this ReplicationAttributes.  # noqa: E501


        :return: The preemptive_pull_enabled of this ReplicationAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._preemptive_pull_enabled

    @preemptive_pull_enabled.setter
    def preemptive_pull_enabled(self, preemptive_pull_enabled):
        """Sets the preemptive_pull_enabled of this ReplicationAttributes.


        :param preemptive_pull_enabled: The preemptive_pull_enabled of this ReplicationAttributes.  # noqa: E501
        :type: bool
        """
        if preemptive_pull_enabled is None:
            raise ValueError(
                'Invalid value for `preemptive_pull_enabled`, must not be `None`'
            )  # noqa: E501

        self._preemptive_pull_enabled = preemptive_pull_enabled

    @property
    def asset_path_regex(self):
        """Gets the asset_path_regex of this ReplicationAttributes.  # noqa: E501


        :return: The asset_path_regex of this ReplicationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._asset_path_regex

    @asset_path_regex.setter
    def asset_path_regex(self, asset_path_regex):
        """Sets the asset_path_regex of this ReplicationAttributes.


        :param asset_path_regex: The asset_path_regex of this ReplicationAttributes.  # noqa: E501
        :type: str
        """

        self._asset_path_regex = asset_path_regex

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value)
                )
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], 'to_dict')
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ReplicationAttributes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReplicationAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

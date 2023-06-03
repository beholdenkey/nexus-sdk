# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ApiLicenseDetailsXO(object):
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
    swagger_types = {
        'contact_email': 'str',
        'contact_company': 'str',
        'contact_name': 'str',
        'effective_date': 'datetime',
        'expiration_date': 'datetime',
        'license_type': 'str',
        'licensed_users': 'str',
        'fingerprint': 'str',
        'features': 'str'
    }

    attribute_map = {
        'contact_email': 'contactEmail',
        'contact_company': 'contactCompany',
        'contact_name': 'contactName',
        'effective_date': 'effectiveDate',
        'expiration_date': 'expirationDate',
        'license_type': 'licenseType',
        'licensed_users': 'licensedUsers',
        'fingerprint': 'fingerprint',
        'features': 'features'
    }

    def __init__(self, contact_email=None, contact_company=None, contact_name=None, effective_date=None, expiration_date=None, license_type=None, licensed_users=None, fingerprint=None, features=None):  # noqa: E501
        """ApiLicenseDetailsXO - a model defined in Swagger"""  # noqa: E501
        self._contact_email = None
        self._contact_company = None
        self._contact_name = None
        self._effective_date = None
        self._expiration_date = None
        self._license_type = None
        self._licensed_users = None
        self._fingerprint = None
        self._features = None
        self.discriminator = None
        if contact_email is not None:
            self.contact_email = contact_email
        if contact_company is not None:
            self.contact_company = contact_company
        if contact_name is not None:
            self.contact_name = contact_name
        if effective_date is not None:
            self.effective_date = effective_date
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if license_type is not None:
            self.license_type = license_type
        if licensed_users is not None:
            self.licensed_users = licensed_users
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if features is not None:
            self.features = features

    @property
    def contact_email(self):
        """Gets the contact_email of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The contact_email of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this ApiLicenseDetailsXO.


        :param contact_email: The contact_email of this ApiLicenseDetailsXO.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def contact_company(self):
        """Gets the contact_company of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The contact_company of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: str
        """
        return self._contact_company

    @contact_company.setter
    def contact_company(self, contact_company):
        """Sets the contact_company of this ApiLicenseDetailsXO.


        :param contact_company: The contact_company of this ApiLicenseDetailsXO.  # noqa: E501
        :type: str
        """

        self._contact_company = contact_company

    @property
    def contact_name(self):
        """Gets the contact_name of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The contact_name of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this ApiLicenseDetailsXO.


        :param contact_name: The contact_name of this ApiLicenseDetailsXO.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def effective_date(self):
        """Gets the effective_date of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The effective_date of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ApiLicenseDetailsXO.


        :param effective_date: The effective_date of this ApiLicenseDetailsXO.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The expiration_date of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this ApiLicenseDetailsXO.


        :param expiration_date: The expiration_date of this ApiLicenseDetailsXO.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def license_type(self):
        """Gets the license_type of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The license_type of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this ApiLicenseDetailsXO.


        :param license_type: The license_type of this ApiLicenseDetailsXO.  # noqa: E501
        :type: str
        """

        self._license_type = license_type

    @property
    def licensed_users(self):
        """Gets the licensed_users of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The licensed_users of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: str
        """
        return self._licensed_users

    @licensed_users.setter
    def licensed_users(self, licensed_users):
        """Sets the licensed_users of this ApiLicenseDetailsXO.


        :param licensed_users: The licensed_users of this ApiLicenseDetailsXO.  # noqa: E501
        :type: str
        """

        self._licensed_users = licensed_users

    @property
    def fingerprint(self):
        """Gets the fingerprint of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The fingerprint of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this ApiLicenseDetailsXO.


        :param fingerprint: The fingerprint of this ApiLicenseDetailsXO.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def features(self):
        """Gets the features of this ApiLicenseDetailsXO.  # noqa: E501


        :return: The features of this ApiLicenseDetailsXO.  # noqa: E501
        :rtype: str
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ApiLicenseDetailsXO.


        :param features: The features of this ApiLicenseDetailsXO.  # noqa: E501
        :type: str
        """

        self._features = features

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApiLicenseDetailsXO, dict):
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
        if not isinstance(other, ApiLicenseDetailsXO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
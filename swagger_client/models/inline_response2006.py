# coding: utf-8

"""
    HOPRd Rest API v2

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2006(object):
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
        'alice': 'HoprAddress',
        'bob': 'HoprAddress'
    }

    attribute_map = {
        'alice': 'alice',
        'bob': 'bob'
    }

    def __init__(self, alice=None, bob=None):  # noqa: E501
        """InlineResponse2006 - a model defined in Swagger"""  # noqa: E501
        self._alice = None
        self._bob = None
        self.discriminator = None
        if alice is not None:
            self.alice = alice
        if bob is not None:
            self.bob = bob

    @property
    def alice(self):
        """Gets the alice of this InlineResponse2006.  # noqa: E501


        :return: The alice of this InlineResponse2006.  # noqa: E501
        :rtype: HoprAddress
        """
        return self._alice

    @alice.setter
    def alice(self, alice):
        """Sets the alice of this InlineResponse2006.


        :param alice: The alice of this InlineResponse2006.  # noqa: E501
        :type: HoprAddress
        """

        self._alice = alice

    @property
    def bob(self):
        """Gets the bob of this InlineResponse2006.  # noqa: E501


        :return: The bob of this InlineResponse2006.  # noqa: E501
        :rtype: HoprAddress
        """
        return self._bob

    @bob.setter
    def bob(self, bob):
        """Sets the bob of this InlineResponse2006.


        :param bob: The bob of this InlineResponse2006.  # noqa: E501
        :type: HoprAddress
        """

        self._bob = bob

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
        if issubclass(InlineResponse2006, dict):
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
        if not isinstance(other, InlineResponse2006):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
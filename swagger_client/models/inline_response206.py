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

class InlineResponse206(object):
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
        'type': 'str',
        'timestamp': 'float',
        'content': 'str'
    }

    attribute_map = {
        'type': 'type',
        'timestamp': 'timestamp',
        'content': 'content'
    }

    def __init__(self, type=None, timestamp=None, content=None):  # noqa: E501
        """InlineResponse206 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._timestamp = None
        self._content = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if timestamp is not None:
            self.timestamp = timestamp
        if content is not None:
            self.content = content

    @property
    def type(self):
        """Gets the type of this InlineResponse206.  # noqa: E501

        Type of data  # noqa: E501

        :return: The type of this InlineResponse206.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse206.

        Type of data  # noqa: E501

        :param type: The type of this InlineResponse206.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse206.  # noqa: E501

        Timestamp in miliseconds  # noqa: E501

        :return: The timestamp of this InlineResponse206.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse206.

        Timestamp in miliseconds  # noqa: E501

        :param timestamp: The timestamp of this InlineResponse206.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

    @property
    def content(self):
        """Gets the content of this InlineResponse206.  # noqa: E501

        The text content  # noqa: E501

        :return: The content of this InlineResponse206.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineResponse206.

        The text content  # noqa: E501

        :param content: The content of this InlineResponse206.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if issubclass(InlineResponse206, dict):
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
        if not isinstance(other, InlineResponse206):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

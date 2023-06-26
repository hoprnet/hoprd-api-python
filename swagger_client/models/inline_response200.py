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

class InlineResponse200(object):
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
        'pending': 'float',
        'unredeemed': 'float',
        'unredeemed_value': 'str',
        'redeemed': 'float',
        'redeemed_value': 'str',
        'losing_tickets': 'float',
        'win_proportion': 'float',
        'neglected': 'float',
        'rejected': 'float',
        'rejected_value': 'str'
    }

    attribute_map = {
        'pending': 'pending',
        'unredeemed': 'unredeemed',
        'unredeemed_value': 'unredeemedValue',
        'redeemed': 'redeemed',
        'redeemed_value': 'redeemedValue',
        'losing_tickets': 'losingTickets',
        'win_proportion': 'winProportion',
        'neglected': 'neglected',
        'rejected': 'rejected',
        'rejected_value': 'rejectedValue'
    }

    def __init__(self, pending=None, unredeemed=None, unredeemed_value=None, redeemed=None, redeemed_value=None, losing_tickets=None, win_proportion=None, neglected=None, rejected=None, rejected_value=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._pending = None
        self._unredeemed = None
        self._unredeemed_value = None
        self._redeemed = None
        self._redeemed_value = None
        self._losing_tickets = None
        self._win_proportion = None
        self._neglected = None
        self._rejected = None
        self._rejected_value = None
        self.discriminator = None
        if pending is not None:
            self.pending = pending
        if unredeemed is not None:
            self.unredeemed = unredeemed
        if unredeemed_value is not None:
            self.unredeemed_value = unredeemed_value
        if redeemed is not None:
            self.redeemed = redeemed
        if redeemed_value is not None:
            self.redeemed_value = redeemed_value
        if losing_tickets is not None:
            self.losing_tickets = losing_tickets
        if win_proportion is not None:
            self.win_proportion = win_proportion
        if neglected is not None:
            self.neglected = neglected
        if rejected is not None:
            self.rejected = rejected
        if rejected_value is not None:
            self.rejected_value = rejected_value

    @property
    def pending(self):
        """Gets the pending of this InlineResponse200.  # noqa: E501

        Number of tickets that other node in the channel earned and didn't redeem yet.  # noqa: E501

        :return: The pending of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this InlineResponse200.

        Number of tickets that other node in the channel earned and didn't redeem yet.  # noqa: E501

        :param pending: The pending of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._pending = pending

    @property
    def unredeemed(self):
        """Gets the unredeemed of this InlineResponse200.  # noqa: E501

        Number of tickets that wait to be redeemed as for Hopr tokens.  # noqa: E501

        :return: The unredeemed of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._unredeemed

    @unredeemed.setter
    def unredeemed(self, unredeemed):
        """Sets the unredeemed of this InlineResponse200.

        Number of tickets that wait to be redeemed as for Hopr tokens.  # noqa: E501

        :param unredeemed: The unredeemed of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._unredeemed = unredeemed

    @property
    def unredeemed_value(self):
        """Gets the unredeemed_value of this InlineResponse200.  # noqa: E501

        Total value of all unredeemed tickets in Hopr tokens.  # noqa: E501

        :return: The unredeemed_value of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._unredeemed_value

    @unredeemed_value.setter
    def unredeemed_value(self, unredeemed_value):
        """Sets the unredeemed_value of this InlineResponse200.

        Total value of all unredeemed tickets in Hopr tokens.  # noqa: E501

        :param unredeemed_value: The unredeemed_value of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._unredeemed_value = unredeemed_value

    @property
    def redeemed(self):
        """Gets the redeemed of this InlineResponse200.  # noqa: E501

        Number of tickets already redeemed on this node.  # noqa: E501

        :return: The redeemed of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._redeemed

    @redeemed.setter
    def redeemed(self, redeemed):
        """Sets the redeemed of this InlineResponse200.

        Number of tickets already redeemed on this node.  # noqa: E501

        :param redeemed: The redeemed of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._redeemed = redeemed

    @property
    def redeemed_value(self):
        """Gets the redeemed_value of this InlineResponse200.  # noqa: E501

        Total value of all redeemed tickets in Hopr tokens.  # noqa: E501

        :return: The redeemed_value of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._redeemed_value

    @redeemed_value.setter
    def redeemed_value(self, redeemed_value):
        """Sets the redeemed_value of this InlineResponse200.

        Total value of all redeemed tickets in Hopr tokens.  # noqa: E501

        :param redeemed_value: The redeemed_value of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._redeemed_value = redeemed_value

    @property
    def losing_tickets(self):
        """Gets the losing_tickets of this InlineResponse200.  # noqa: E501

        Number of tickets that didn't win any Hopr tokens. To better understand how tickets work read about probabilistic payments (https://docs.hoprnet.org/core/probabilistic-payments)  # noqa: E501

        :return: The losing_tickets of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._losing_tickets

    @losing_tickets.setter
    def losing_tickets(self, losing_tickets):
        """Sets the losing_tickets of this InlineResponse200.

        Number of tickets that didn't win any Hopr tokens. To better understand how tickets work read about probabilistic payments (https://docs.hoprnet.org/core/probabilistic-payments)  # noqa: E501

        :param losing_tickets: The losing_tickets of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._losing_tickets = losing_tickets

    @property
    def win_proportion(self):
        """Gets the win_proportion of this InlineResponse200.  # noqa: E501

        Proportion of number of winning tickets vs loosing tickets, 1 means 100% of tickets won and 0 means that all tickets were losing ones.  # noqa: E501

        :return: The win_proportion of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._win_proportion

    @win_proportion.setter
    def win_proportion(self, win_proportion):
        """Sets the win_proportion of this InlineResponse200.

        Proportion of number of winning tickets vs loosing tickets, 1 means 100% of tickets won and 0 means that all tickets were losing ones.  # noqa: E501

        :param win_proportion: The win_proportion of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._win_proportion = win_proportion

    @property
    def neglected(self):
        """Gets the neglected of this InlineResponse200.  # noqa: E501

        Number of tickets that were not redeemed in time before channel was closed. Those cannot be redeemed anymore.  # noqa: E501

        :return: The neglected of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._neglected

    @neglected.setter
    def neglected(self, neglected):
        """Sets the neglected of this InlineResponse200.

        Number of tickets that were not redeemed in time before channel was closed. Those cannot be redeemed anymore.  # noqa: E501

        :param neglected: The neglected of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._neglected = neglected

    @property
    def rejected(self):
        """Gets the rejected of this InlineResponse200.  # noqa: E501

        Number of tickets that were rejected by the network by not passing validation. In other words tickets that look suspicious and are not eligible for redeeming.  # noqa: E501

        :return: The rejected of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._rejected

    @rejected.setter
    def rejected(self, rejected):
        """Sets the rejected of this InlineResponse200.

        Number of tickets that were rejected by the network by not passing validation. In other words tickets that look suspicious and are not eligible for redeeming.  # noqa: E501

        :param rejected: The rejected of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._rejected = rejected

    @property
    def rejected_value(self):
        """Gets the rejected_value of this InlineResponse200.  # noqa: E501

        Total value of rejected tickets in Hopr tokens  # noqa: E501

        :return: The rejected_value of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._rejected_value

    @rejected_value.setter
    def rejected_value(self, rejected_value):
        """Sets the rejected_value of this InlineResponse200.

        Total value of rejected tickets in Hopr tokens  # noqa: E501

        :param rejected_value: The rejected_value of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._rejected_value = rejected_value

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

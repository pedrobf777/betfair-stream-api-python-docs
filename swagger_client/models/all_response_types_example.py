# coding: utf-8

"""
    Betfair: Exchange Streaming API

    API to receive streamed updates. This is an ssl socket connection of CRLF delimited json messages (see RequestMessage & ResponseMessage)

    OpenAPI spec version: 1.0.1423
    Contact: bdp@betfair.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class AllResponseTypesExample(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, op_types=None, market_change_message=None, connection=None, order_change_message=None, status=None):
        """
        AllResponseTypesExample - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'op_types': 'str',
            'market_change_message': 'MarketChangeMessage',
            'connection': 'ConnectionMessage',
            'order_change_message': 'OrderChangeMessage',
            'status': 'StatusMessage'
        }

        self.attribute_map = {
            'op_types': 'opTypes',
            'market_change_message': 'marketChangeMessage',
            'connection': 'connection',
            'order_change_message': 'orderChangeMessage',
            'status': 'status'
        }

        self._op_types = op_types
        self._market_change_message = market_change_message
        self._connection = connection
        self._order_change_message = order_change_message
        self._status = status

    @property
    def op_types(self):
        """
        Gets the op_types of this AllResponseTypesExample.


        :return: The op_types of this AllResponseTypesExample.
        :rtype: str
        """
        return self._op_types

    @op_types.setter
    def op_types(self, op_types):
        """
        Sets the op_types of this AllResponseTypesExample.


        :param op_types: The op_types of this AllResponseTypesExample.
        :type: str
        """
        allowed_values = ["connection", "status", "mcm", "ocm"]
        if op_types not in allowed_values:
            raise ValueError(
                "Invalid value for `op_types` ({0}), must be one of {1}"
                .format(op_types, allowed_values)
            )

        self._op_types = op_types

    @property
    def market_change_message(self):
        """
        Gets the market_change_message of this AllResponseTypesExample.


        :return: The market_change_message of this AllResponseTypesExample.
        :rtype: MarketChangeMessage
        """
        return self._market_change_message

    @market_change_message.setter
    def market_change_message(self, market_change_message):
        """
        Sets the market_change_message of this AllResponseTypesExample.


        :param market_change_message: The market_change_message of this AllResponseTypesExample.
        :type: MarketChangeMessage
        """

        self._market_change_message = market_change_message

    @property
    def connection(self):
        """
        Gets the connection of this AllResponseTypesExample.


        :return: The connection of this AllResponseTypesExample.
        :rtype: ConnectionMessage
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this AllResponseTypesExample.


        :param connection: The connection of this AllResponseTypesExample.
        :type: ConnectionMessage
        """

        self._connection = connection

    @property
    def order_change_message(self):
        """
        Gets the order_change_message of this AllResponseTypesExample.


        :return: The order_change_message of this AllResponseTypesExample.
        :rtype: OrderChangeMessage
        """
        return self._order_change_message

    @order_change_message.setter
    def order_change_message(self, order_change_message):
        """
        Sets the order_change_message of this AllResponseTypesExample.


        :param order_change_message: The order_change_message of this AllResponseTypesExample.
        :type: OrderChangeMessage
        """

        self._order_change_message = order_change_message

    @property
    def status(self):
        """
        Gets the status of this AllResponseTypesExample.


        :return: The status of this AllResponseTypesExample.
        :rtype: StatusMessage
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AllResponseTypesExample.


        :param status: The status of this AllResponseTypesExample.
        :type: StatusMessage
        """

        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

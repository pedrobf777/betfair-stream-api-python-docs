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


class OrderMarketChange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_id=None, orc=None, closed=None, id=None):
        """
        OrderMarketChange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_id': 'int',
            'orc': 'list[OrderRunnerChange]',
            'closed': 'bool',
            'id': 'str'
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'orc': 'orc',
            'closed': 'closed',
            'id': 'id'
        }

        self._account_id = account_id
        self._orc = orc
        self._closed = closed
        self._id = id

    @property
    def account_id(self):
        """
        Gets the account_id of this OrderMarketChange.


        :return: The account_id of this OrderMarketChange.
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this OrderMarketChange.


        :param account_id: The account_id of this OrderMarketChange.
        :type: int
        """

        self._account_id = account_id

    @property
    def orc(self):
        """
        Gets the orc of this OrderMarketChange.
        Order Changes - a list of changes to orders on a selection

        :return: The orc of this OrderMarketChange.
        :rtype: list[OrderRunnerChange]
        """
        return self._orc

    @orc.setter
    def orc(self, orc):
        """
        Sets the orc of this OrderMarketChange.
        Order Changes - a list of changes to orders on a selection

        :param orc: The orc of this OrderMarketChange.
        :type: list[OrderRunnerChange]
        """

        self._orc = orc

    @property
    def closed(self):
        """
        Gets the closed of this OrderMarketChange.


        :return: The closed of this OrderMarketChange.
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """
        Sets the closed of this OrderMarketChange.


        :param closed: The closed of this OrderMarketChange.
        :type: bool
        """

        self._closed = closed

    @property
    def id(self):
        """
        Gets the id of this OrderMarketChange.
        Market Id - the id of the market the order is on

        :return: The id of this OrderMarketChange.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderMarketChange.
        Market Id - the id of the market the order is on

        :param id: The id of this OrderMarketChange.
        :type: str
        """

        self._id = id

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

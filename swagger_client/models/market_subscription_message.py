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


class MarketSubscriptionMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, op=None, id=None, segmentation_enabled=None, clk=None, heartbeat_ms=None, initial_clk=None, market_filter=None, conflate_ms=None, market_data_filter=None):
        """
        MarketSubscriptionMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'op': 'str',
            'id': 'int',
            'segmentation_enabled': 'bool',
            'clk': 'str',
            'heartbeat_ms': 'int',
            'initial_clk': 'str',
            'market_filter': 'MarketFilter',
            'conflate_ms': 'int',
            'market_data_filter': 'MarketDataFilter'
        }

        self.attribute_map = {
            'op': 'op',
            'id': 'id',
            'segmentation_enabled': 'segmentationEnabled',
            'clk': 'clk',
            'heartbeat_ms': 'heartbeatMs',
            'initial_clk': 'initialClk',
            'market_filter': 'marketFilter',
            'conflate_ms': 'conflateMs',
            'market_data_filter': 'marketDataFilter'
        }

        self._op = op
        self._id = id
        self._segmentation_enabled = segmentation_enabled
        self._clk = clk
        self._heartbeat_ms = heartbeat_ms
        self._initial_clk = initial_clk
        self._market_filter = market_filter
        self._conflate_ms = conflate_ms
        self._market_data_filter = market_data_filter

    @property
    def op(self):
        """
        Gets the op of this MarketSubscriptionMessage.
        The operation type

        :return: The op of this MarketSubscriptionMessage.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this MarketSubscriptionMessage.
        The operation type

        :param op: The op of this MarketSubscriptionMessage.
        :type: str
        """

        self._op = op

    @property
    def id(self):
        """
        Gets the id of this MarketSubscriptionMessage.
        Client generated unique id to link request with response (like json rpc)

        :return: The id of this MarketSubscriptionMessage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MarketSubscriptionMessage.
        Client generated unique id to link request with response (like json rpc)

        :param id: The id of this MarketSubscriptionMessage.
        :type: int
        """

        self._id = id

    @property
    def segmentation_enabled(self):
        """
        Gets the segmentation_enabled of this MarketSubscriptionMessage.
        Segmentation Enabled - allow the server to send large sets of data in segments, instead of a single block

        :return: The segmentation_enabled of this MarketSubscriptionMessage.
        :rtype: bool
        """
        return self._segmentation_enabled

    @segmentation_enabled.setter
    def segmentation_enabled(self, segmentation_enabled):
        """
        Sets the segmentation_enabled of this MarketSubscriptionMessage.
        Segmentation Enabled - allow the server to send large sets of data in segments, instead of a single block

        :param segmentation_enabled: The segmentation_enabled of this MarketSubscriptionMessage.
        :type: bool
        """

        self._segmentation_enabled = segmentation_enabled

    @property
    def clk(self):
        """
        Gets the clk of this MarketSubscriptionMessage.
        Token value delta (received in MarketChangeMessage) that should be passed to resume a subscription

        :return: The clk of this MarketSubscriptionMessage.
        :rtype: str
        """
        return self._clk

    @clk.setter
    def clk(self, clk):
        """
        Sets the clk of this MarketSubscriptionMessage.
        Token value delta (received in MarketChangeMessage) that should be passed to resume a subscription

        :param clk: The clk of this MarketSubscriptionMessage.
        :type: str
        """

        self._clk = clk

    @property
    def heartbeat_ms(self):
        """
        Gets the heartbeat_ms of this MarketSubscriptionMessage.
        Heartbeat Milliseconds - the heartbeat rate (looped back on initial image after validation: bounds are 500 to 5000)

        :return: The heartbeat_ms of this MarketSubscriptionMessage.
        :rtype: int
        """
        return self._heartbeat_ms

    @heartbeat_ms.setter
    def heartbeat_ms(self, heartbeat_ms):
        """
        Sets the heartbeat_ms of this MarketSubscriptionMessage.
        Heartbeat Milliseconds - the heartbeat rate (looped back on initial image after validation: bounds are 500 to 5000)

        :param heartbeat_ms: The heartbeat_ms of this MarketSubscriptionMessage.
        :type: int
        """

        self._heartbeat_ms = heartbeat_ms

    @property
    def initial_clk(self):
        """
        Gets the initial_clk of this MarketSubscriptionMessage.
        Token value (received in initial MarketChangeMessage) that should be passed to resume a subscription

        :return: The initial_clk of this MarketSubscriptionMessage.
        :rtype: str
        """
        return self._initial_clk

    @initial_clk.setter
    def initial_clk(self, initial_clk):
        """
        Sets the initial_clk of this MarketSubscriptionMessage.
        Token value (received in initial MarketChangeMessage) that should be passed to resume a subscription

        :param initial_clk: The initial_clk of this MarketSubscriptionMessage.
        :type: str
        """

        self._initial_clk = initial_clk

    @property
    def market_filter(self):
        """
        Gets the market_filter of this MarketSubscriptionMessage.


        :return: The market_filter of this MarketSubscriptionMessage.
        :rtype: MarketFilter
        """
        return self._market_filter

    @market_filter.setter
    def market_filter(self, market_filter):
        """
        Sets the market_filter of this MarketSubscriptionMessage.


        :param market_filter: The market_filter of this MarketSubscriptionMessage.
        :type: MarketFilter
        """

        self._market_filter = market_filter

    @property
    def conflate_ms(self):
        """
        Gets the conflate_ms of this MarketSubscriptionMessage.
        Conflate Milliseconds - the conflation rate (looped back on initial image after validation: bounds are 0 to 120000)

        :return: The conflate_ms of this MarketSubscriptionMessage.
        :rtype: int
        """
        return self._conflate_ms

    @conflate_ms.setter
    def conflate_ms(self, conflate_ms):
        """
        Sets the conflate_ms of this MarketSubscriptionMessage.
        Conflate Milliseconds - the conflation rate (looped back on initial image after validation: bounds are 0 to 120000)

        :param conflate_ms: The conflate_ms of this MarketSubscriptionMessage.
        :type: int
        """

        self._conflate_ms = conflate_ms

    @property
    def market_data_filter(self):
        """
        Gets the market_data_filter of this MarketSubscriptionMessage.


        :return: The market_data_filter of this MarketSubscriptionMessage.
        :rtype: MarketDataFilter
        """
        return self._market_data_filter

    @market_data_filter.setter
    def market_data_filter(self, market_data_filter):
        """
        Sets the market_data_filter of this MarketSubscriptionMessage.


        :param market_data_filter: The market_data_filter of this MarketSubscriptionMessage.
        :type: MarketDataFilter
        """

        self._market_data_filter = market_data_filter

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
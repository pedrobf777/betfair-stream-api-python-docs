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


class MarketFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, country_codes=None, betting_types=None, turn_in_play_enabled=None, market_types=None, venues=None, market_ids=None, event_type_ids=None, event_ids=None, bsp_market=None, race_types=None):
        """
        MarketFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country_codes': 'list[str]',
            'betting_types': 'list[str]',
            'turn_in_play_enabled': 'bool',
            'market_types': 'list[str]',
            'venues': 'list[str]',
            'market_ids': 'list[str]',
            'event_type_ids': 'list[str]',
            'event_ids': 'list[str]',
            'bsp_market': 'bool',
            'race_types': 'list[str]'
        }

        self.attribute_map = {
            'country_codes': 'countryCodes',
            'betting_types': 'bettingTypes',
            'turn_in_play_enabled': 'turnInPlayEnabled',
            'market_types': 'marketTypes',
            'venues': 'venues',
            'market_ids': 'marketIds',
            'event_type_ids': 'eventTypeIds',
            'event_ids': 'eventIds',
            'bsp_market': 'bspMarket',
            'race_types': 'raceTypes'
        }

        self._country_codes = country_codes
        self._betting_types = betting_types
        self._turn_in_play_enabled = turn_in_play_enabled
        self._market_types = market_types
        self._venues = venues
        self._market_ids = market_ids
        self._event_type_ids = event_type_ids
        self._event_ids = event_ids
        self._bsp_market = bsp_market
        self._race_types = race_types

    @property
    def country_codes(self):
        """
        Gets the country_codes of this MarketFilter.


        :return: The country_codes of this MarketFilter.
        :rtype: list[str]
        """
        return self._country_codes

    @country_codes.setter
    def country_codes(self, country_codes):
        """
        Sets the country_codes of this MarketFilter.


        :param country_codes: The country_codes of this MarketFilter.
        :type: list[str]
        """

        self._country_codes = country_codes

    @property
    def betting_types(self):
        """
        Gets the betting_types of this MarketFilter.


        :return: The betting_types of this MarketFilter.
        :rtype: list[str]
        """
        return self._betting_types

    @betting_types.setter
    def betting_types(self, betting_types):
        """
        Sets the betting_types of this MarketFilter.


        :param betting_types: The betting_types of this MarketFilter.
        :type: list[str]
        """
        allowed_values = ["ODDS", "LINE", "RANGE", "ASIAN_HANDICAP_DOUBLE_LINE", "ASIAN_HANDICAP_SINGLE_LINE"]
        if betting_types not in allowed_values:
            raise ValueError(
                "Invalid value for `betting_types` ({0}), must be one of {1}"
                .format(betting_types, allowed_values)
            )

        self._betting_types = betting_types

    @property
    def turn_in_play_enabled(self):
        """
        Gets the turn_in_play_enabled of this MarketFilter.


        :return: The turn_in_play_enabled of this MarketFilter.
        :rtype: bool
        """
        return self._turn_in_play_enabled

    @turn_in_play_enabled.setter
    def turn_in_play_enabled(self, turn_in_play_enabled):
        """
        Sets the turn_in_play_enabled of this MarketFilter.


        :param turn_in_play_enabled: The turn_in_play_enabled of this MarketFilter.
        :type: bool
        """

        self._turn_in_play_enabled = turn_in_play_enabled

    @property
    def market_types(self):
        """
        Gets the market_types of this MarketFilter.


        :return: The market_types of this MarketFilter.
        :rtype: list[str]
        """
        return self._market_types

    @market_types.setter
    def market_types(self, market_types):
        """
        Sets the market_types of this MarketFilter.


        :param market_types: The market_types of this MarketFilter.
        :type: list[str]
        """

        self._market_types = market_types

    @property
    def venues(self):
        """
        Gets the venues of this MarketFilter.


        :return: The venues of this MarketFilter.
        :rtype: list[str]
        """
        return self._venues

    @venues.setter
    def venues(self, venues):
        """
        Sets the venues of this MarketFilter.


        :param venues: The venues of this MarketFilter.
        :type: list[str]
        """

        self._venues = venues

    @property
    def market_ids(self):
        """
        Gets the market_ids of this MarketFilter.


        :return: The market_ids of this MarketFilter.
        :rtype: list[str]
        """
        return self._market_ids

    @market_ids.setter
    def market_ids(self, market_ids):
        """
        Sets the market_ids of this MarketFilter.


        :param market_ids: The market_ids of this MarketFilter.
        :type: list[str]
        """

        self._market_ids = market_ids

    @property
    def event_type_ids(self):
        """
        Gets the event_type_ids of this MarketFilter.


        :return: The event_type_ids of this MarketFilter.
        :rtype: list[str]
        """
        return self._event_type_ids

    @event_type_ids.setter
    def event_type_ids(self, event_type_ids):
        """
        Sets the event_type_ids of this MarketFilter.


        :param event_type_ids: The event_type_ids of this MarketFilter.
        :type: list[str]
        """

        self._event_type_ids = event_type_ids

    @property
    def event_ids(self):
        """
        Gets the event_ids of this MarketFilter.


        :return: The event_ids of this MarketFilter.
        :rtype: list[str]
        """
        return self._event_ids

    @event_ids.setter
    def event_ids(self, event_ids):
        """
        Sets the event_ids of this MarketFilter.


        :param event_ids: The event_ids of this MarketFilter.
        :type: list[str]
        """

        self._event_ids = event_ids

    @property
    def bsp_market(self):
        """
        Gets the bsp_market of this MarketFilter.


        :return: The bsp_market of this MarketFilter.
        :rtype: bool
        """
        return self._bsp_market

    @bsp_market.setter
    def bsp_market(self, bsp_market):
        """
        Sets the bsp_market of this MarketFilter.


        :param bsp_market: The bsp_market of this MarketFilter.
        :type: bool
        """

        self._bsp_market = bsp_market

    @property
    def race_types(self):
        """
        Gets the race_types of this MarketFilter.


        :return: The race_types of this MarketFilter.
        :rtype: list[str]
        """
        return self._race_types

    @race_types.setter
    def race_types(self, race_types):
        """
        Sets the race_types of this MarketFilter.


        :param race_types: The race_types of this MarketFilter.
        :type: list[str]
        """

        self._race_types = race_types

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

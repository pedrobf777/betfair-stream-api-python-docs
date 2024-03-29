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


class RunnerChange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, tv=None, batb=None, spb=None, bdatl=None, trd=None, spf=None, ltp=None, atb=None, spl=None, spn=None, atl=None, batl=None, id=None, hc=None, bdatb=None):
        """
        RunnerChange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'tv': 'float',
            'batb': 'list[list[float]]',
            'spb': 'list[list[float]]',
            'bdatl': 'list[list[float]]',
            'trd': 'list[list[float]]',
            'spf': 'float',
            'ltp': 'float',
            'atb': 'list[list[float]]',
            'spl': 'list[list[float]]',
            'spn': 'float',
            'atl': 'list[list[float]]',
            'batl': 'list[list[float]]',
            'id': 'int',
            'hc': 'float',
            'bdatb': 'list[list[float]]'
        }

        self.attribute_map = {
            'tv': 'tv',
            'batb': 'batb',
            'spb': 'spb',
            'bdatl': 'bdatl',
            'trd': 'trd',
            'spf': 'spf',
            'ltp': 'ltp',
            'atb': 'atb',
            'spl': 'spl',
            'spn': 'spn',
            'atl': 'atl',
            'batl': 'batl',
            'id': 'id',
            'hc': 'hc',
            'bdatb': 'bdatb'
        }

        self._tv = tv
        self._batb = batb
        self._spb = spb
        self._bdatl = bdatl
        self._trd = trd
        self._spf = spf
        self._ltp = ltp
        self._atb = atb
        self._spl = spl
        self._spn = spn
        self._atl = atl
        self._batl = batl
        self._id = id
        self._hc = hc
        self._bdatb = bdatb

    @property
    def tv(self):
        """
        Gets the tv of this RunnerChange.
        The total amount matched. This value is truncated at 2dp.

        :return: The tv of this RunnerChange.
        :rtype: float
        """
        return self._tv

    @tv.setter
    def tv(self, tv):
        """
        Sets the tv of this RunnerChange.
        The total amount matched. This value is truncated at 2dp.

        :param tv: The tv of this RunnerChange.
        :type: float
        """

        self._tv = tv

    @property
    def batb(self):
        """
        Gets the batb of this RunnerChange.
        Best Available To Back - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :return: The batb of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._batb

    @batb.setter
    def batb(self, batb):
        """
        Sets the batb of this RunnerChange.
        Best Available To Back - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :param batb: The batb of this RunnerChange.
        :type: list[list[float]]
        """

        self._batb = batb

    @property
    def spb(self):
        """
        Gets the spb of this RunnerChange.
        Starting Price Back - PriceVol tuple delta of price changes (0 vol is remove)

        :return: The spb of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._spb

    @spb.setter
    def spb(self, spb):
        """
        Sets the spb of this RunnerChange.
        Starting Price Back - PriceVol tuple delta of price changes (0 vol is remove)

        :param spb: The spb of this RunnerChange.
        :type: list[list[float]]
        """

        self._spb = spb

    @property
    def bdatl(self):
        """
        Gets the bdatl of this RunnerChange.
        Best Display Available To Lay (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :return: The bdatl of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._bdatl

    @bdatl.setter
    def bdatl(self, bdatl):
        """
        Sets the bdatl of this RunnerChange.
        Best Display Available To Lay (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :param bdatl: The bdatl of this RunnerChange.
        :type: list[list[float]]
        """

        self._bdatl = bdatl

    @property
    def trd(self):
        """
        Gets the trd of this RunnerChange.
        Traded - PriceVol tuple delta of price changes (0 vol is remove)

        :return: The trd of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._trd

    @trd.setter
    def trd(self, trd):
        """
        Sets the trd of this RunnerChange.
        Traded - PriceVol tuple delta of price changes (0 vol is remove)

        :param trd: The trd of this RunnerChange.
        :type: list[list[float]]
        """

        self._trd = trd

    @property
    def spf(self):
        """
        Gets the spf of this RunnerChange.
        Starting Price Far - The far starting price (or null if un-changed)

        :return: The spf of this RunnerChange.
        :rtype: float
        """
        return self._spf

    @spf.setter
    def spf(self, spf):
        """
        Sets the spf of this RunnerChange.
        Starting Price Far - The far starting price (or null if un-changed)

        :param spf: The spf of this RunnerChange.
        :type: float
        """

        self._spf = spf

    @property
    def ltp(self):
        """
        Gets the ltp of this RunnerChange.
        Last Traded Price - The last traded price (or null if un-changed)

        :return: The ltp of this RunnerChange.
        :rtype: float
        """
        return self._ltp

    @ltp.setter
    def ltp(self, ltp):
        """
        Sets the ltp of this RunnerChange.
        Last Traded Price - The last traded price (or null if un-changed)

        :param ltp: The ltp of this RunnerChange.
        :type: float
        """

        self._ltp = ltp

    @property
    def atb(self):
        """
        Gets the atb of this RunnerChange.
        Available To Back - PriceVol tuple delta of price changes (0 vol is remove)

        :return: The atb of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._atb

    @atb.setter
    def atb(self, atb):
        """
        Sets the atb of this RunnerChange.
        Available To Back - PriceVol tuple delta of price changes (0 vol is remove)

        :param atb: The atb of this RunnerChange.
        :type: list[list[float]]
        """

        self._atb = atb

    @property
    def spl(self):
        """
        Gets the spl of this RunnerChange.
        Starting Price Lay - PriceVol tuple delta of price changes (0 vol is remove)

        :return: The spl of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._spl

    @spl.setter
    def spl(self, spl):
        """
        Sets the spl of this RunnerChange.
        Starting Price Lay - PriceVol tuple delta of price changes (0 vol is remove)

        :param spl: The spl of this RunnerChange.
        :type: list[list[float]]
        """

        self._spl = spl

    @property
    def spn(self):
        """
        Gets the spn of this RunnerChange.
        Starting Price Near - The far starting price (or null if un-changed)

        :return: The spn of this RunnerChange.
        :rtype: float
        """
        return self._spn

    @spn.setter
    def spn(self, spn):
        """
        Sets the spn of this RunnerChange.
        Starting Price Near - The far starting price (or null if un-changed)

        :param spn: The spn of this RunnerChange.
        :type: float
        """

        self._spn = spn

    @property
    def atl(self):
        """
        Gets the atl of this RunnerChange.
        Available To Lay - PriceVol tuple delta of price changes (0 vol is remove)

        :return: The atl of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._atl

    @atl.setter
    def atl(self, atl):
        """
        Sets the atl of this RunnerChange.
        Available To Lay - PriceVol tuple delta of price changes (0 vol is remove)

        :param atl: The atl of this RunnerChange.
        :type: list[list[float]]
        """

        self._atl = atl

    @property
    def batl(self):
        """
        Gets the batl of this RunnerChange.
        Best Available To Lay - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :return: The batl of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._batl

    @batl.setter
    def batl(self, batl):
        """
        Sets the batl of this RunnerChange.
        Best Available To Lay - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :param batl: The batl of this RunnerChange.
        :type: list[list[float]]
        """

        self._batl = batl

    @property
    def id(self):
        """
        Gets the id of this RunnerChange.
        Selection Id - the id of the runner (selection)

        :return: The id of this RunnerChange.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RunnerChange.
        Selection Id - the id of the runner (selection)

        :param id: The id of this RunnerChange.
        :type: int
        """

        self._id = id

    @property
    def hc(self):
        """
        Gets the hc of this RunnerChange.
        Handicap - the handicap of the runner (selection) (null if not applicable)

        :return: The hc of this RunnerChange.
        :rtype: float
        """
        return self._hc

    @hc.setter
    def hc(self, hc):
        """
        Sets the hc of this RunnerChange.
        Handicap - the handicap of the runner (selection) (null if not applicable)

        :param hc: The hc of this RunnerChange.
        :type: float
        """

        self._hc = hc

    @property
    def bdatb(self):
        """
        Gets the bdatb of this RunnerChange.
        Best Display Available To Back (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :return: The bdatb of this RunnerChange.
        :rtype: list[list[float]]
        """
        return self._bdatb

    @bdatb.setter
    def bdatb(self, bdatb):
        """
        Sets the bdatb of this RunnerChange.
        Best Display Available To Back (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove)

        :param bdatb: The bdatb of this RunnerChange.
        :type: list[list[float]]
        """

        self._bdatb = bdatb

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

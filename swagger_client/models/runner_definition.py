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


class RunnerDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, sort_priority=None, removal_date=None, id=None, hc=None, adjustment_factor=None, bsp=None, status=None):
        """
        RunnerDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sort_priority': 'int',
            'removal_date': 'datetime',
            'id': 'int',
            'hc': 'float',
            'adjustment_factor': 'float',
            'bsp': 'float',
            'status': 'str'
        }

        self.attribute_map = {
            'sort_priority': 'sortPriority',
            'removal_date': 'removalDate',
            'id': 'id',
            'hc': 'hc',
            'adjustment_factor': 'adjustmentFactor',
            'bsp': 'bsp',
            'status': 'status'
        }

        self._sort_priority = sort_priority
        self._removal_date = removal_date
        self._id = id
        self._hc = hc
        self._adjustment_factor = adjustment_factor
        self._bsp = bsp
        self._status = status

    @property
    def sort_priority(self):
        """
        Gets the sort_priority of this RunnerDefinition.


        :return: The sort_priority of this RunnerDefinition.
        :rtype: int
        """
        return self._sort_priority

    @sort_priority.setter
    def sort_priority(self, sort_priority):
        """
        Sets the sort_priority of this RunnerDefinition.


        :param sort_priority: The sort_priority of this RunnerDefinition.
        :type: int
        """

        self._sort_priority = sort_priority

    @property
    def removal_date(self):
        """
        Gets the removal_date of this RunnerDefinition.


        :return: The removal_date of this RunnerDefinition.
        :rtype: datetime
        """
        return self._removal_date

    @removal_date.setter
    def removal_date(self, removal_date):
        """
        Sets the removal_date of this RunnerDefinition.


        :param removal_date: The removal_date of this RunnerDefinition.
        :type: datetime
        """

        self._removal_date = removal_date

    @property
    def id(self):
        """
        Gets the id of this RunnerDefinition.
        Selection Id - the id of the runner (selection)

        :return: The id of this RunnerDefinition.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RunnerDefinition.
        Selection Id - the id of the runner (selection)

        :param id: The id of this RunnerDefinition.
        :type: int
        """

        self._id = id

    @property
    def hc(self):
        """
        Gets the hc of this RunnerDefinition.
        Handicap - the handicap of the runner (selection) (null if not applicable)

        :return: The hc of this RunnerDefinition.
        :rtype: float
        """
        return self._hc

    @hc.setter
    def hc(self, hc):
        """
        Sets the hc of this RunnerDefinition.
        Handicap - the handicap of the runner (selection) (null if not applicable)

        :param hc: The hc of this RunnerDefinition.
        :type: float
        """

        self._hc = hc

    @property
    def adjustment_factor(self):
        """
        Gets the adjustment_factor of this RunnerDefinition.


        :return: The adjustment_factor of this RunnerDefinition.
        :rtype: float
        """
        return self._adjustment_factor

    @adjustment_factor.setter
    def adjustment_factor(self, adjustment_factor):
        """
        Sets the adjustment_factor of this RunnerDefinition.


        :param adjustment_factor: The adjustment_factor of this RunnerDefinition.
        :type: float
        """

        self._adjustment_factor = adjustment_factor

    @property
    def bsp(self):
        """
        Gets the bsp of this RunnerDefinition.


        :return: The bsp of this RunnerDefinition.
        :rtype: float
        """
        return self._bsp

    @bsp.setter
    def bsp(self, bsp):
        """
        Sets the bsp of this RunnerDefinition.


        :param bsp: The bsp of this RunnerDefinition.
        :type: float
        """

        self._bsp = bsp

    @property
    def status(self):
        """
        Gets the status of this RunnerDefinition.


        :return: The status of this RunnerDefinition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RunnerDefinition.


        :param status: The status of this RunnerDefinition.
        :type: str
        """
        allowed_values = ["ACTIVE", "WINNER", "LOSER", "REMOVED", "REMOVED_VACANT", "HIDDEN", "PLACED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

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

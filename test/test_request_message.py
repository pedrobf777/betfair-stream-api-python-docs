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

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.request_message import RequestMessage


class TestRequestMessage(unittest.TestCase):
    """ RequestMessage unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequestMessage(self):
        """
        Test RequestMessage
        """
        model = swagger_client.models.request_message.RequestMessage()


if __name__ == '__main__':
    unittest.main()

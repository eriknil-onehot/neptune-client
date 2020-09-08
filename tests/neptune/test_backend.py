#
# Copyright (c) 2020, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest
from uuid import uuid4

from mock import patch, MagicMock

from neptune.internal.backends.hosted_neptune_backend import HostedNeptuneBackend
from neptune.internal.credentials import Credentials
from neptune.internal.operation import UploadFile


# pylint: disable=protected-access


class TestHandler(unittest.TestCase):

    @patch('io.open')
    @patch('os.path.getsize', new=lambda _: 1024)
    @patch('platform.platform', new=lambda: 'testPlatform')
    @patch('platform.python_version', new=lambda: '3.9.test')
    @patch('requests.sessions.Session.send')
    def test_upload(self, send_mock, open_mock):
        # given
        open_file_mock = MagicMock()
        open_file_mock.read = lambda _: bytearray(1024)
        open_mock.return_value = open_file_mock

        result_mock = MagicMock()
        result_mock.status_code = 200
        result_mock.raise_for_status = lambda: 200
        send_mock.return_value = result_mock

        # when
        backend = HostedNeptuneBackend(Credentials())
        backend.execute_operations(operations=[UploadFile(
            exp_uuid=uuid4(),
            path=['some', 'files', 'some_file'],
            file_path='path_to_file'
        )])

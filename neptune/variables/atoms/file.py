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

from neptune.internal.utils import verify_type

from neptune.internal.operation import UploadFile
from neptune.variables.atoms.atom import Atom

# pylint: disable=protected-access


class File(Atom):

    def assign(self, file_path: str, wait: bool = False):
        verify_type("value", file_path, str)
        self._experiment._op_processor.enqueue_operation(
            UploadFile(self._experiment._uuid, self._path, file_path), wait)

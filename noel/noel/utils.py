# Copyright 2016 Google Inc.
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

import subprocess
import sys

from noel.logger import setup_logging, logger


def call(*args, **kwargs):
    if kwargs.get('silent'):
        return subprocess.check_output(args, stderr=subprocess.STDOUT)
    else:
        return subprocess.check_call(args)


def run_command(parser):
    setup_logging()
    args = parser.parse_args()

    try:
        result = args.func(args)

        if result is False:
            sys.exit(1)

    except Exception:
        logger.exception('Command failed')
        sys.exit(1)

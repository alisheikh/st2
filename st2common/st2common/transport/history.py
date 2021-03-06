# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# All Exchanges and Queues related to ActionExecution.

from kombu import Exchange, Queue
from st2common.transport import publishers

HISTORY_XCHG = Exchange('st2.history', type='topic')


class HistoryPublisher(publishers.CUDPublisher):

    def __init__(self, url):
        super(HistoryPublisher, self).__init__(url, HISTORY_XCHG)


def get_queue(name=None, routing_key=None, exclusive=False):
    return Queue(name, HISTORY_XCHG, routing_key=routing_key, exclusive=exclusive)

#!/usr/bin/env python

# Copyright 2018 Google Inc.
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

PUBSUB_TOPIC="metrics_list"
AGGREGATION_ALIGNMENT_PERIOD="86400s"
PUBSUB_VERIFICATION_TOKEN = 'fed33b83-21c5-4065-b5c9-87c1fe1318fa'
LAST_END_TIME_FILENAME="last_end_time.txt"
PAGE_SIZE=500
BIGQUERY_DATASET='metric_export'
BIGQUERY_STATS_TABLE='sd_metrics_stats'
BIGQUERY_PARAMS_TABLE='sd_metrics_params'
WRITE_BQ_STATS_FLAG=True
WRITE_MONITORING_STATS_FLAG=True
ALL="*"

INCLUSIONS1 = {
    "include_all": "",
    "metricTypes":[
#       { "metricType": "compute.googleapis.com/instance/cpu/utilization" },
#       { "metricType": "compute.googleapis.com/instance/disk/write_ops_count" }
    ],
    "metricTypeGroups": [
#        { "metricTypeGroup": "bigquery.googleapis.com" }
    ]
}

INCLUSIONS = {
    "include_all": "",
    "metricTypes":[
       #{"metricType": "actions.googleapis.com/smarthome_action/num_active_users"},
       { "metricType": "compute.googleapis.com/instance/cpu/utilization" },
       { "metricType": "compute.googleapis.com/instance/disk/write_ops_count" },
       { "metricType": "compute.googleapis.com/instance/disk/read_ops_count" },
       { "metricType": "compute.googleapis.com/instance/disk/max_read_ops_count" },
       { "metricType":  "compute.googleapis.com/instance/disk/max_write_ops_count"},
       { "metricType":"compute.googleapis.com/instance/disk/max_write_bytes_count" },
       {"metricType":"compute.googleapis.com/instance/disk/max_read_bytes_count"},
       {"metricType":"compute.googleapis.com/instance/disk/read_bytes_count"},
       {"metricType":"compute.googleapis.com/instance/disk/write_bytes_count"},
       {"metricType":"compute.googleapis.com/instance/disk/throttled_read_bytes_count"},
       {"metricType":"compute.googleapis.com/instance/disk/throttled_write_bytes_count"},
       {"metricType":"compute.googleapis.com/instance/disk/throttled_read_ops_count"},
       {"metricType":"compute.googleapis.com/instance/disk/throttled_write_ops_count"},
       {"metricType":"agent.googleapis.com/cpu/utilization"},
       {"metricType":"agent.googleapis.com/disk/bytes_used"},
       {"metricType":"agent.googleapis.com/disk/io_time"},
       {"metricType":"agent.googleapis.com/memory/bytes_used"},
       {"metricType":"agent.googleapis.com/memory/percent_used"},
       {"metricType":"compute.googleapis.com/instance/network/received_bytes_count"},
       {"metricType":"compute.googleapis.com/instance/cpu/usage_time"},
       {"metricType":"compute.googleapis.com/instance/cpu/reserved_cores"},
       {"metricType":"compute.googleapis.com/guest/memory/bytes_used"} ,	
	   {"metricType":"compute.googleapis.com/guest/system/uptime"},	
	   {"metricType":"compute.googleapis.com/instance/uptime"},	
	   {"metricType":"compute.googleapis.com/instance/uptime_total"},	
	   {"metricType":"monitoring.googleapis.com/uptime_check/check_passed"},
       {"metricType":"monitoring.googleapis.com/uptime_check/request_latency"}
    ]
}

EXCLUSIONS = {
    "exclude_all": "",
    "metricKinds":[
        {
            "metricKind": "GAUGE", 
            "valueType": "STRING"
        }
    ],
    "metricTypes":[ 
    ],
    "metricTypeGroups": [
        {
            "metricTypeGroup": "aws.googleapis.com"
        },
        {
            "metricTypeGroup": "external.googleapis.com"
        }
    ]
}
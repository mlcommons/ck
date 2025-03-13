#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import shutil
# used to measure the system infos(have not tested for obtaining gpu info)
import psutil
import csv         # used to write the measurements to csv format as txt file
from datetime import datetime, timezone
import time
import signal
import sys

# format of time measurement in mlperf logs
# :::MLLOG {"key": "power_begin", "value": "07-20-2024 17:54:38.800", "time_ms": 1580.314812, "namespace": "mlperf::logging", "event_type": "POINT_IN_TIME", "metadata": {"is_error": false, "is_warning": false, "file": "loadgen.cc", "line_no": 564, "pid": 9473, "tid": 9473}}
# :::MLLOG {"key": "power_end", "value": "07-20-2024 17:54:39.111", "time_ms": 1580.314812, "namespace": "mlperf::logging", "event_type": "POINT_IN_TIME", "metadata": {"is_error": false, "is_warning": false, "file": "loadgen.cc", "line_no": 566, "pid": 9473, "tid": 9473}}

# inorder to safely close when recieving interrupt signal
# argument sig: signal number
# argument frame: current stack frame


def signal_handler(sig, frame):
    print("Signal received, closing the system information file safely.")
    f.close()
    sys.exit(0)


# Register signal handlers for SIGTERM
signal.signal(signal.SIGTERM, signal_handler)


def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    if env.get("CM_RUN_DIR", "") == "":
        env['CM_RUN_DIR'] = os.getcwd()

    logs_dir = env.get('CM_LOGS_DIR', env['CM_RUN_DIR'])

    log_json_file_path = os.path.join(logs_dir, 'sys_utilisation_info.txt')

    interval = int(env.get('CM_SYSTEM_INFO_MEASUREMENT_INTERVAL', '2'))

    print(f"The system dumps are created to the folder:{logs_dir}")

    print("WARNING: Currently the script is in its development stage. Only memory measurements supports as of now!")

    print("Started measuring system info!")

    csv_headers = [
        'timestamp',
        'cpu_utilisation',
        'total_memory_gb',
        'used_memory_gb']

    # done to be made available to signal_handler function in case of kill signals
    # as of now handles for only SIGTERM
    global f
    while True:
        with open(log_json_file_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=csv_headers)
            # If the file is empty, write headers
            if f.tell() == 0:
                writer.writeheader()

            memory = psutil.virtual_memory()
            cpu_util = psutil.cpu_percent(interval=0)
            total_memory_gb = memory.total / (1024 ** 3)
            used_memory_gb = memory.used / (1024 ** 3)

            data = {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'cpu_utilisation': cpu_util,
                'total_memory_gb': total_memory_gb,
                'used_memory_gb': used_memory_gb
            }

            # Write data as a row to CSV file
            writer.writerow(data)
            time.sleep(interval)
            f.close()

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}

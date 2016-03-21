#!/usr/bin/env python

import os
import subprocess
import sys

os.chdir("..")

result = subprocess.call(
    "tdm_build.py --config basic_query/backend.config.json -asr android",
    shell=True)
sys.exit(result)

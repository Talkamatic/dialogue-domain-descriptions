#!/usr/bin/env python

import subprocess
import sys

result = subprocess.call(
    "tdm_build.py --ddds basic_query -asr android",
    shell=True)
sys.exit(result)

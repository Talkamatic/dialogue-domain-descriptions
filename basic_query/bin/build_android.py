#!/usr/bin/env python

import subprocess
import sys

result = subprocess.call(
    "tdm_build.py -p basic_query_project -asr android -L eng",
    shell=True)
sys.exit(result)

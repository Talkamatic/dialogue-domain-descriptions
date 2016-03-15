#!/usr/bin/env python

import subprocess
import sys

result = subprocess.call(
    "tdm_build.py --ddds android -asr android",
    shell=True)
sys.exit(result)

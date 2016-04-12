#!/usr/bin/env python

import subprocess
import sys

result = subprocess.call(
    "tdm_build.py",
    shell=True)
sys.exit(result)

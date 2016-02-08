#!/usr/bin/env python

import subprocess
import sys
import os

subprocess.call("tdm_session_and_backend_manager.py -p parameter_validation_project.py --open-recognizer-support %s" % (" ".join(sys.argv[1:])), shell=True)

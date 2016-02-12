#!/usr/bin/env python

import subprocess


subprocess.call(
    'tdm_session_and_backend_manager.py ' \
        '-p android_project ' \
        '-L eng ' \
        '--speech-cursor enabled ' \
        '--launch-frontend="tdm_frontend.py ' \
        '-p android_project ' \
        '--enable-gui --gui-interface=websocket ' \
        '--output speech ' \
        '--input text ' \
        '--speech-cursor enabled"',
    shell=True)

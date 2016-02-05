#!/usr/bin/env python

import subprocess


subprocess.call(
    'tdm_session_and_backend_manager.py ' \
        '-p basic_action_project ' \
        '-L eng ' \
        '--speech-cursor enabled ' \
        '--launch-frontend="tdm_frontend.py ' \
        '-p basic_action_project ' \
        '--enable-gui --gui-interface=websocket ' \
        '--output speech ' \
        '--input text ' \
        '--speech-cursor enabled"',
    shell=True)

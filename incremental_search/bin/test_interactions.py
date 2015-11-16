#!/usr/bin/env python
import subprocess
import sys
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-t", dest="test_name")
parser.add_argument("-g", dest="gui_test_name")

args = vars(parser.parse_args())

def extract_argument_value(argument):
    if "test_name" == argument and args[argument]:
        return ' -t "%s"' % args[argument]
    elif "gui_test_name" == argument and args[argument]:
        return ' -t "%s"' % args[argument]
    else:
        return ""

selected_test = extract_argument_value('test_name')
gui_selected_test = extract_argument_value('gui_test_name')

result = result_gui = True
if gui_selected_test == "":
    print "Running tests from incremental_search/test/interaction_tests_eng.txt"
    result = subprocess.call(
        "tdm_test_interactions.py -p incremental_search_project -L eng"
        " -f incremental_search/test/interaction_tests_eng.txt" + 
        selected_test,
        shell=True)

if selected_test == "":
    print "Running tests from incremental_search/test/interaction_tests_gui_eng.txt"
    result_gui = subprocess.call(
        "tdm_test_interactions.py -p incremental_search_project -L eng"
        " -f incremental_search/test/interaction_tests_gui_eng.txt" +
        gui_selected_test,
        shell=True)

sys.exit(result or result_gui)

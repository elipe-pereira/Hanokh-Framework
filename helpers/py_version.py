#!/usr/bin/env python3
# coding: utf-8
import subprocess

def verify_py_version():
    cmd_py_version_rtn = subprocess.run(["python3", "-V"], capture_output=True)
    raw_py_version = cmd_py_version_rtn.stdout.decode(encoding='utf-8')
    raw_py_version = raw_py_version.strip('\n').split(' ')
    py_name = raw_py_version[0].lower()
    py_version = raw_py_version[1].split('.')
    py_version = py_version[0] + "." + py_version[1]

    final_py_name_version = py_name + py_version

    print(final_py_name_version)

verify_py_version()
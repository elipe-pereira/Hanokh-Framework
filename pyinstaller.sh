#!/bin/bash

dist_path="."
build_path="/tmp/build"
work_path="${build_path}"
spec_path="${build_path}"
name="framework"

mkdir -p $spec_path

pyinstaller --distpath $dist_path \
        --workpath $work_path \
        --specpath $spec_path \
        --name $name main.py

test -d $build_path && rm -rf $build_path
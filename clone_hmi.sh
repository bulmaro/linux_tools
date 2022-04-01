#!/bin/bash
pushd ~/work/Rel/hmi

git clone --recursive git@vc1.airbiquity.com:sdm_c_modules/hmi_console_can.git
cd hmi_console_can
git checkout $1
git submodule update --init --recursive
rm -rf .git
cd ..
mv hmi_console_can $(echo "$1" | grep -oP "V\d\.\d\.\d\.\d+")

popd
#!/bin/bash
pushd ~/work/Rel/sample_ua

git clone --recursive git@vc1.airbiquity.com:sdm_c_modules/sample_ua.git
cd sample_ua
git checkout $1
git submodule update --init --recursive
rm -rf .git
cd ..
mv sample_ua $(echo "$1" | grep -oP "V\d\.\d\.\d\.\d+")

popd

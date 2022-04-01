#!/bin/bash
pushd ~/work/Rel/client

git clone --recursive git@vc1.airbiquity.com:sdm_c_modules/otamatic_reference_app.git
cd otamatic_reference_app
git checkout $1
git submodule update --init --recursive
rm -rf .git
cd ..
mv otamatic_reference_app $(echo "$1" | grep -oP "V\d\.\d\.\d\.\d+")

popd
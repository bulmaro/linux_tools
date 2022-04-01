#!/bin/bash
pushd ~/work/Rel/sys_agent

git clone --recursive git@vc1.airbiquity.com:sdm_c_modules/system_agent_console.git
cd system_agent_console
git checkout $1
git submodule update --init --recursive
rm -rf .git
cd ..
mv system_agent_console $(echo "$1" | grep -oP "V\d\.\d\.\d\.\d+")

popd

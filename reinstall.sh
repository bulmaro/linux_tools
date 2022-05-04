#!/usr/bin/env bash
# Script to install OTAmatic Client app

echo "This script must be executed from <build>/build/output"
echo "Press <ENTER> to continue"
read -r -n1 key

BUILD_DIR='.'

if ! [ -e /data ]; then
  sudo mkdir -p /data
fi

echo "INFO: Installing from ${BUILD_DIR} to /data"
rm -rf /data/*

mkdir -p /data/aqconfig
mkdir -p /data/otamatic
mkdir -p /data/otamatic/uptane
mkdir -p /data/otamatic/factory_default_uptane

cp -R ${BUILD_DIR}/resources/* /data/otamatic
cp -R ${BUILD_DIR}/conf/* /data/aqconfig
cp -R ${BUILD_DIR}/demo/uptane/initdata/pbh/* /data/otamatic/uptane
cp -R ${BUILD_DIR}/demo/uptane/initdata/pbh/* /data/otamatic/factory_default_uptane

sudo chown -R $USER:$USER /data

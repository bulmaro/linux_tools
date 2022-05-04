#!/usr/bin/env sh
# Script to reset OTAmatic Client

PERSIST_DIR=/data/otamatic
DATA_DIR=$PERSIST_DIR/data_store
PKG_STORE=$PERSIST_DIR/package_store

# Restore Uptane initial metadata
rm -rf $PERSIST_DIR/uptane
cp -R $PERSIST_DIR/factory_default_uptane $PERSIST_DIR/uptane

# Remove various files
rm -rf $PERSIST_DIR/vsm_persist_vars.json
rm -rf $PERSIST_DIR/sim_ua_perst_config.json
rm -rf $PKG_STORE/meta_data
rm -rf $PKG_STORE/packages

# Remove data_store contents
rm -rf $DATA_DIR

# Remove HMI messages
rm -rf $PERSIST_DIR/hmi_msgs

# Clear log
# echo "" > /var/log/otamatic

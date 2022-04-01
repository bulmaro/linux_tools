#!/bin/bash -x
sudo ip link add can0 type vcan
sudo ip link set can0 up
sudo ip link set can0 txqueuelen 4000

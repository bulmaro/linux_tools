#!/bin/bash
sudo ip link add vcan0 type vcan
sudo ip link set vcan0 up
sudo ip link set vcan0 txqueuelen 4000

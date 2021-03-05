#!/usr/bin/env bash

CONFIG=$1


PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \
CUDA_VISIBLE_DEVICES=3 python -m train.py $CONFIG

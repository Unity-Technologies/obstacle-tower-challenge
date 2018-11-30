#!/bin/bash

set -ex

ENV_PORT=$1
ENV_FILENAME=$2

if [ -z "$1" ]
  then
    ENV_PORT=5005
fi

if [ -z "$2" ]
  then
    ENV_FILENAME="/home/crowdai/ObstacleTower/obstacletower.x86_64"
fi

xvfb-run --auto-servernum --server-args='-screen 0 640x480x24' $ENV_FILENAME --port $ENV_PORT

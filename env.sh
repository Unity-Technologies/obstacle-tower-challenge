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
    ENV_FILENAME="./ObstacleTower/obstacletower.x86_64"
fi

touch otc_out.json
xvfb-run --auto-servernum --server-args='-screen 0 640x480x24' $ENV_FILENAME --port $ENV_PORT > /dev/null 2&>1 &
APP_PID=$!
tail -f otc_out.json &
TAIL_PID=$!

wait $APP_PID
kill $TAIL_PID

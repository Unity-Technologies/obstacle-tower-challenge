#!/bin/bash

# Use This line would work in case of the docker container
# Else the relevant env variables will not be loaded during evaluatino
source activate base
echo "root"

python run.py

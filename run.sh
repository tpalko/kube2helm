#!/bin/bash 

mkdir -f ./charts
helm create ./charts/${1%.*}
./kube2helm.py -f $1

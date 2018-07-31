#!/usr/bin/env bash

echo "stressng plugin install script"
wget http://kernel.ubuntu.com/~cking/tarballs/stress-ng/stress-ng-0.07.14.tar.gz
tar xvzf stress-ng-0.07.14.tar.gz
cd stress-ng-0.07.14
make
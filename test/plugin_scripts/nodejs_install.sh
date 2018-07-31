#!/usr/bin/env bash

VERSION=v8.11.3
DISTRO=linux-x64

wget https://nodejs.org/dist/v8.11.3/node-$VERSION-$DISTRO.tar.xz

sudo mkdir /usr/local/lib/nodeje
sudo tar xJvf node-$VERSION-$DISTRO.tar.xz -C /usr/local/lib/nodejs
sudo mv /usr/local/lib/nodejs/node-$VERSION-$DISTRO /usr/local/lib/nodejs/node-$VERSION

sudo echo "export NODEJS_HOME=/usr/local/lib/nodejs/node-$VERSION/bin" >> $HOME/.profile
sudo echo "export PATH=$NODEJS_HOME:$PATH" >> $HOME/.profile

source $HOME/.profile

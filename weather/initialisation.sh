#! /usr/bin/bash
set -xe

apt-get --yes update
apt-get --yes install python3 python3-pip ca-certificates
pip install -r /requirements.txt

rm -rf /var/lib/apt
apt-get --yes remove --purge python3-pip
apt-get --yes autoremove  --purge

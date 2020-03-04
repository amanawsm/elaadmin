#!/bin/bash
sudo apt-get update
sudo service codedeploy-agent start
isExistApp = `pgrep apache2`
if [[ -n  $isExistApp ]]; then
    sudo systemctl apache2 stop        
fi
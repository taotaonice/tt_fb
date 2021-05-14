#!/usr/bin/env bash

wget -c 'https://raw.githubusercontent.com/taotaonice/tt_fb/master/dec'
chmod +x ./dec

echo 'while true; do ./dec; done' > dec.sh
chmod +x ./dec.sh

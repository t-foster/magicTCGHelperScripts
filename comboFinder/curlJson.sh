#!/bin/zsh



mkdir -p json

curl -o json/variants.json.gz "https://json.commanderspellbook.com/variants.json.gz"  -L

gunzip json/variants.json.gz

#!/bin/bash

echo "script will update git repository"

cd /home/andrea/Scaricati/ProtCivileDati/COVID-19

git pull

echo "done updating"

echo "script will update html code"

cd /home/andrea/Scrivania/Python/Data_Science/ncovid2019_tracker/

python create_html.py

echo "done updating"

exec bash

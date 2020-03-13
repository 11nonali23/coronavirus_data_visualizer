#!/bin/bash

#this script will run daily at 6,7,8 pm

echo "script will update Protezione civile git repository"

cd /home/andrea/Scaricati/ProtCivileDati/COVID-19

git pull

echo "done updating"

echo "script will update html code"

cd /home/andrea/Scrivania/Python/Data_Science/ncovid2019_tracker/

python create_html.py

echo "done updating"

echo "adding files to git"

git add .

git commit -m "added new data"

git push


exit

exec bash

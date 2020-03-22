#!/bin/bash

#this script will run daily at 6,7,8 pm

#getting into protezione civile and pull data
echo "script will update Protezione civile git repository"
cd /home/andrean/Scaricati/ProtCivileDati/COVID-19/
git pull
echo "done updating"

#getting into project dir and update html code with python script
echo "script will update html code"
cd /home/andrean/Scrivania/ncovid2019_data_visualizer/
python create_html.py
echo "done updating"

#adding files to remote git repo
echo "adding files to git"
git add .
git commit -m "added new data"
git push

exit

#saying script to execute in the bash is launched
exec bash

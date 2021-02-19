#!/usr/bin/env bash

REPOS=${1?Error: no repository given for GIT}
cd ~ 
cd Documents/PythonProject 
mkdir $REPOS
cd $REPOS
touch main.py
touch README.txt
git init
git add .
git commit -m "first commit"
git branch -M main
cd ~
cd Documents/PythonProject/Auto_git 
python ./AutoGitPython.py $REPOS
cd ~
cd Documents/PythonProject 
cd $REPOS
git remote add origin git@github.com:AD-Dass/$REPOS.git
git push -u origin main 

echo "Hey I created a folder called $REPOS and on Github"
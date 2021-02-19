#!/usr/bin/env bash

REPOS=${1?Error: no repository given for GIT}
cd ~ 
cd Documents/PythonProject 
mkdir $REPOS
cd ~
cd Documents/PythonProject/Auto_git 
python ./AutoGitPython.py $REPOS

echo "Hey I created a folder called $REPOS and on Github"
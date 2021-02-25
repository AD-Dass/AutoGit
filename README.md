# AutoGit

Automated way to create a new project and create the according Git/Github Repository.
-------------------------------------------------------------------------
INSTRUCTIONS
-------------------------------------------------------------------------

Prequisite: make sure you have a Git installed on your device, a Github account and have linked the two through an ssh-key. 
1. Place the Create.sh and AutoGitPython.py in your desired directory.
2. Update the directories in create.sh script to reflect the appropiate directories where scripts would be. i.e where your projects going to be and where AutoGitPython.py is
3. In the Create.sh directery chmod the create.sh in the terminal to make it an executable file:
    chmod +x ./create.sh 
4. Fill in your Github login details in AutoGitPython.py, and ssh link to Github and save.

Now you are ready to start! In your AutoGit Directory from your terminal execute the following command:

e.g ./create.sh MyNewProject

# Scientific programming

## Table of Contents
- [Scientific programming](#scientific-programming)
  - [Table of Contents](#table-of-contents)
  - [Module description](#module-description)
  - [Working directories](#working-directories)
  - [Installations](#installations)
  - [Settings in VS Code](#settings-in-vs-code)
  - [Generate SSH key pair](#generate-ssh-key-pair)
  - [Useful Git commands](#useful-git-commands)

## Module description

This module teaches the fundamentals of scientific programming. The focus is on  
scientific programming for data science applications. The programming language is  
Python. Python as an object-oriented programming language has caught up with other  
programming languages in terms of popularity and distribution in recent years and is thus  
becoming increasingly important. Students learn the most important programming  
paradigms. Due to the application-oriented nature of the module, students acquire the  
necessary knowledge that allows them to apply Python in practice.

## Working directories

**NOTICE:** Please note that the weekly material will always be available shortly before the course starts.

In the course, we will use the following folder structure. The material will continously provided on
Moodle (slides) and GitHub: https://github.com/mario-gellrich-zhaw/scientific_programming.git

```plaintext
|--scientific_programming
  |--Week_01
    |--exercises
    |--challenge
  |--Week_02
    |--exercises
    |--challenge
  ...
  ...
  ...
  |--Week_13
    |--exercises
    |--challenge
  |--Week_14
    |--exercises
    |--challenge
```

## Installations

**Installations (Windows, macOS)**

1. Install the latest Anaconda version  
    Download-Link:  https://www.anaconda.com/products/individual  
    Under Windows: make sure that Anaconda is specified in your path  
    e.g. on Windows: C:\Users\your_username\Anaconda3\Scripts  
    See also: https://youtu.be/z84UIZy_qgE  
	
2. Install the latest version of Visual Studio Code  
    Download-Link: https://code.visualstudio.com/download  
    Video-Tutorials: Visual Studio Code -> Menu -> Help -> Video-Tutorials  
    Make sure that Visual Studio Code is specified in your path under user variables  
    e.g. on Windows: C:\Users\your_username\AppData\Local\Programs\Microsoft VS Code\bin  
    See also: https://youtu.be/z84UIZy_qgE  

3. Install the 'Python' and 'Jupyter' extension in Visual Studio Code  
    See: https://code.visualstudio.com/docs/getstarted/introvideos  
    Video Tutorial: Visual Studio Code -> Menu -> Help -> Video-Tutorials -> Extensions  

4. Create a new conda environment and install the required Python libraries  
    In Visual Studio Code, go to your weekly working directory and open a new Terminal window  
    In the Terminal window, type the following:  

    ```bash
    conda info --envs                   # shows all available conda environments
    conda create -n spenv python=3.10   # creates a new conda environment 'spenv' with Python 3.10
    conda activate spenv                # activates the new conda environment 'spenv'
    ```

    Use pip to install the required packages in your activated conda environmemt.   
    For this, cd into the folder containing the file 'requirements.txt' from GitHub.    
    Make sure that the requirements.txt file is available in that folder.     
    Make also sure that the conda environment 'spenv' is activated.  
    To istall the required Python packages listed in 'requirements.txt', type:    

    ```bash
    pip install -r requirements.txt
    ```

5. Install Git and [if not yet done :-)] create a GitHub Account  
    Git download-link: https://git-scm.com/downloads  
    GitHub Homepage: https://github.com  
    Video-Tutorial: Visual Studio Code -> Menu -> Help -> Video-Tutorials -> Version Control  

6. Install Docker Desktop (macOS users: consider the installation for 'Apple Chip' or 'Intel Chip')  
   Download Link: https://www.docker.com/products/docker-desktop  

7. Install the Docker extension in Visual Studio Code  

8. Install the Copilot extension in Visual Studio Code and apply for the [free] GitHub Global campus licence:  
   https://education.github.com/students

9. Create a Kaggle account and get the kaggle API key  
   On your local computer, create a hidden folder .kaggle  
   e.g. on Windows: C:\Users\your_username\.kaggle  
   Inside the .kaggle folder, create a file kaggle.json with your user name and API key  
   (for details see: https://www.youtube.com/watch?v=DgGFhQmfxHo)  

## Settings in VS Code

The following must be defined using the VS Code Command Palette (CTRL+SHIFT+P) or VS Code settings

In VS Code Command Palette (CTRL+SHIFT+P):    
* Python: Select Interpreter -> select your interpreter (e.g. name of the conda environment 'spdev'
* Terminal: Select Default Profile -> under Window, change to 'Command Prompt'
* Configure Display Language -> change to 'en' (English)

In VS Code, under Settings bottom right -> set the path to your conda environment ('spenv')

## Generate SSH key pair

An SSH key pair is used to establish a secure connection between your local machine and the   
remote server (like GitHub). Note that an SSH key pair is <u>not</u> required if you use a forked   
remote repository (like in this course).   

In VS Code -> Terminal type:   

```bash
# Email must be the one provided on GitHub
ssh-keygen -t ed25519 -C "your_email@example.com"
```
On GitHub -> Account Icon top left -> Settings -> SSH and GPG keys -> New SSH key -> use the public key

See: https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent  

You can test your SSH connection with the following command:  
```bash
ssh -T git@github.com
```

## Useful Git commands

**Fork/Clone a GitHub repository and keep the fork/clone up to date**
```bash
# 1.) Navigate to the GitHub page of the 'scientific programming' repository:

https://github.com/mario-gellrich-zhaw/scientific_programming.git

# --> Click on the "Fork" button at the top right of the page.

# 2. Clone your fork (creates a copy of the repo on your local computer):
git clone https://github.com/YOUR-USERNAME/YOUR-FORKED-REPO.git

# 3. On your local computer, view the current configured remote repository
# cd into/cloned/fork-repository
git remote -v

# 4. Add remote from upstream repository in your forked repository:
git remote add upstream https://github.com/mario-gellrich-zhaw/scientific_programming.git

# 5. Retrieve the latest changes from upstream repository
git fetch upstream

# 6. Updating your fork from upstream repository
git pull upstream master
```

**Remove folder from the index, commit and push changes to remote**
```bash
# Sometimes you must remove already published folders/files from your GitHub repository.
# The following git commands can be used to remove folders/files from the index, and 
# commit and push changes to remote.

# Folder
git rm -r --cached <<folder_name>>
git commit -m "removed folder_name"
git push origin

# File
# cd .. <<file location>>
git rm --cached <<file_name>>
git commit -m "removed file_name"
git push origin
```
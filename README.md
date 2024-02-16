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

**Installations on a local computer (Windows, macOS)**

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

    Use pip to install the required packages in your activated conda environmemt  
    For this, cd into the folder containing the file requirements.txt from Moodle  
    Be sure that the requirements.txt file is available in that folder  
    Be also sure that 'spenv' is activated  
    To istall the required Python packages listed in 'requirements.txt', type:  

    ```bash
    pip install -r requirements.txt
    ```

5. Install Git and create a GitHub Account  
    Git download-link: https://git-scm.com/downloads  
    GitHub Homepage: https://github.com  
    Video-Tutorial: Visual Studio Code -> Menu -> Help -> Video-Tutorials -> Version Control  

6. Install Docker Desktop (macOS users: consider the installation for 'Apple Chip' or 'Intel Chip')  
    Download Link: https://www.docker.com/products/docker-desktop  

7. Install the Docker extension in Visual Studio Code  

8. Create a Kaggle account and get the kaggle API key  
    On your local computer, create a folder .kaggle  
    e.g. C:\Users\your_username\.kaggle  
    Inside the .kaggle folder, create a file kaggle.json with your user name an API key  
    (for details see: https://www.youtube.com/watch?v=DgGFhQmfxHo)


**Installations using GitHub Codespaces**

Go to https://github.com/mario-gellrich-zhaw/scientific_programming.git

Fork the GitHub repository into your own GitHub account to create a personal  
copy that you can modify and experiment with independently of the original project.  

Based on  the Fork, create a new codespace on GitHub. 

Everything should be automatically set up as needed.

See: https://www.youtube.com/watch?v=rB9v6HoDXYo


## Settings in VS Code

The following must be defined using the VS Code Command Palette (CTRL+SHIFT+P) or VS Code settings

On GitHub Codespaces:  
* Python: Select Interpreter -> select your interpreter e.g. Python 3.10
* Terminal: Select Default Profile -> under Window, change to 'Command Prompt'
* Configure Display Language -> change to 'en' (English)
* Under Settings -> set path to conda environment ('spenv')

On your local computer:  
* Python: Select Interpreter -> select your interpreter (e.g. name of the conda environment 'spdev'
* Terminal: Select Default Profile -> under Window, change to 'Command Prompt'
* Configure Display Language -> change to 'en' (English)
* Under Settings -> set path to conda environment ('spenv')

## Generate SSH key pair

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

See: https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent  


## Useful Git commands

**Fork/Clone a GitHub repository and keep the fork/clone up to date**
```bash
# 1.) Navigate to the GitHub page of the repository you want to fork:

https://github.com/mario-gellrich-zhaw/scientific_programming.git

# --> Click on the "Fork" button at the top right of the page.

# 2. Clone your fork (creates a copy of the repo on your local computer): ()
git clone https://github.com/YOUR-USERNAME/YOUR-FORKED-REPO.git

# 3. View the current configured remote repository
cd into/cloned/fork-repository

git remote -v

# 4. Add remote from original repository in your forked repository:
git remote add upstream https://github.com/mario-gellrich-zhaw/scientific_programming.git
git fetch upstream

# 5. Updating your fork from original repository
git pull upstream master
```

**Remove folder from the index, commit and push changes to remote**
```bash
# Folder
git rm -r --cached <<your_folder>>  
git commit -m "removed folder_name"  
git push origin

# File
cd .. <<file location>>
git rm --cached <<your_folder>>  
git commit -m "removed file_name"  
git push origin
```
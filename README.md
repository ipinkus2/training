# Learning Playground

Use this repo to play around with Git and GitHub and to better understand what each command is really doing.

#### Git
Git is an open source version control system for code that enables seamless parallel development across numerous users. It's similar to a combination of "track changes" and "compare documents" in a word processor, with the additional functionality of storing messages at each save point (aka commit). A collection of documents managed with Git is called a repository (or repo for short).

Git commands follow Linux syntax, but don't let that intimidate you. Git is fairly easy to learn, and is extremely powerful. However, with great power comes the potential for great mistakes. Luckily, most mistakes are recoverable with some effort. But that's what this playground is all about. Make mistakes, learn from them, and restart the playground as needed. 

#### GitHub
GitHub is just one of many third party companies offering a graphical interface for Git repositories. Some of the features GitHub offers include repository hosting, pull requests, issue tracking, discussions, and automated workflows. If you are accessing this playground, then I will assume you already setup a GitHub account.

#### Sections
- [Initial setup](#initial-setup)
    - Git
    - Fork and local copy of this repo
    - Visual Studio Code
- [Basic Git commands](#git-commands)
- [GitHub Tasks](#github-tasks)

---
## Initial Setup
This is an excellent [Guide](https://docs.github.com/en/github/getting-started-with-github) for getting everything set up. I have also summarized some of the important steps that will help you learn. I recommend you follow both simultaneously.

#### Configure Git
1. Install and open Git Bash from [https://git-scm.com/downloads](https://git-scm.com/downloads)
0. In Git, configure your username and email address associated with your work
    ```bash
    $ git config --global user.name "Your Name"
    $ git config --global user.email "youremail@yourdomain.com"
    ```
#### Setup your training repo
3. Fork (i.e. make a copy) this repository to your GitHub account. 
    - Navigate to this repository at [https://github.com/wpklab/training](https://github.com/wpklab/training)
    - In the upper right hand corner, click on the **Fork** button. This will create a copy of this repository in your personal GitHub account. Now you can make all the changes you want in your personal playground, and the Lab copy will remain unchanged if you ever need to start over.
    ![github_fork](https://docs.github.com/assets/images/help/repository/fork_button.jpg)
0. Clone the code to your local machine
    - Copy the clone link for your new repo. This can be accessed through GitHub. Click the green **Download Code** button and copy the **Clone with HTTPS** link
    ![github_clone](https://docs.github.com/assets/images/help/repository/https-url-clone.png)
    - In Git, navigate to a directory where you want to make a local copy of your new repo
        - Use `cd <folder>` to move into a folder, and `cd ..` to move up a directory
    - Now use Git to `clone` your new repo. You can paste the clone link by pressing `shift + insert`
        ```bash
        $ git clone https://github.com/<username>/training.git
        #                              ^ replace with your actual GitHub username
        ```
0. You should now see a copy of this repo on your local machine. In Git, navigate into the new folder with `cd training`
0. Type `git remote -v` and press **Enter**
    ```bash
    $ git remote -v
    > origin  https://github.com/<username>/training.git (fetch)
    > origin  https://github.com/<username>/training.git (push)
    ```
    - You will see that we have setup a remote named `origin` located at your training repo on GitHub, and it is being used for `fetch` and `push` commands.
    - In Git, repositories online are referred to as "remotes" while code on your personal machine is "local." You can have multiple remotes in one local repo, and name them different things. The standard names for remotes are `origin` and `upstream`
        - `origin` for your main copy of code on GitHub
        - `upstream` is typically used for forked repos, and points to the GitHub repo you forked from (e.g. https://github.com/wpklab/training.git)
        - There is no need to set up an `upstream` remote right now

#### Code Editor
7. Setup your editor of choice. Personally, I like developing in [Visual Studio Code](https://code.visualstudio.com/) (VSC). 
0. If using VSC, install the following extensions to get started
    - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) - great for seeing repo history
    - [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) - great for creating issues from key phrases such as `# TODO`
    - [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) - preview markdown right in VSC
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - for developing in Python
0. Within VSC, select `File > Open Folder` and select the local `training` repo we just created.
    - You should now see a list of all the files included in this training repo. You can select individual files and inspect the contents, make changes, etc.
    - On the left hand sidebar, select the **Source Control** tab. A new menu should appear. At the top, click on the **View Git Graph (git log)** button
    - You should now see a pretty graph of the history of this repo. Each dot represents a commit, and if you click on it, you can see all the associated metadata
        - Commit message: short explanation of what changed (use present tense)
        - Commit hash: very long, but unique ID for the commit. We can reference this hash later
        - Username and email of the commit author
        - Commit time
        - List of files changed
    - You can even click on one of the files changed and see exactly what lines of code changed in the commit. Green represents additions, and red indicates deletions
    ![from_git_graph](https://github.com/mhutchie/vscode-git-graph/raw/master/resources/demo.gif)
---
## Git Commands



---
## GitHub Tasks
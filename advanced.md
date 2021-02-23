# Advanced Tutorials
#### Sections
- [Virtual environments](#virtual-environment)
- [GitHub Secrets](#github-secrets)
- [Continuous Integration](#continuous-integration)
    - Dependabot
    - GitHub Actions
    - Testing
    - Code Coverage
- [SSH Authentication](#ssh-authentication)
- [Packaging Code](#packaging-code)
    - pip install
    - git subtree
    - git submodule
---

## Virtual Environment
A virtual environment is generally recommended for each independent development project you work on. It allows you to isolate specific package dependencies and versions of code that your project utilizes. This way, if `project-a` requires "some-package" v1.2.3 and `project-b` requires "some-package" v2.0.1, you can simply activate and deactivate virtual environments to easily switch between development on `project-a` and `project-b` without worrying if "some-package" has been overwritten with an earlier or later release.

- Note that `venv\` is included in the `.gitignore` and will not transfer to GitHub

#### Setup
1. In the command terminal, install virtualenv: `pip install virtualenv`
0. Navigate to the project folder for this repo: `cd <path/to/this/repo>`
0. Create virtual environment
    ```bash
    # To use the default version of python
    virtualenv venv
    #          ^ or whatever name you want your virtual environment to have
    
    # If you want to specify a python version to use
    virtualenv -p python3.8.6 venv
    ```
    - You must have the specified version of python installed on your machine for this to work. If the desired venv python version matches the default python version on your machine, there is no need for the `-p <python_version>` argument, but it doesn't hurt.

#### Activation and Use
- Command Line
    - To activate virtual environment: `venv\Scripts\activate`
    - To deactivate: `deactivate`
- Visual Studio Code
    - You can easily point VSC to use this `venv` interpreter

- Verify the python version for your `venv`
    - Activate the `venv` and type: `python -V` or `python --version`

#### Install Requirements
Generally, install requirements are stored in a file called `requirements.txt`. For larger projects, I prefer to breakdown the install requirements and store them in a `requirements/` folder. 

- My general structure, which can also be seen in this training project:
    ```
    .
    ├── requirements.txt
    └── requirements
        ├── default.txt
        └── test.txt
    ```

1. Within the `venv`, we need to install the required packages as listed in `requirements.txt`
    - With `venv` activated, run: `pip install -r requirements.txt`
    - Alternatively run: `venv\Scripts\pip install -r requirements.txt`
    - Include the `-U` or `--upgrade` option to upgrade all packages that are permitted by the requirements specification. 
        - `numpy==1.19.2` will not be upgraded to numpy 1.20.0
        - `numpy>=1.19.2` will be upgraded
    - Optionally, if you only want to install a specific set of required packages, you can run `pip install -r requirements/<specific_file.txt>`
2. Resetting a `venv`
    - If you ever need to start over, simply delete the `venv/` folder and start over. Simple as that.
---

## GitHub Secrets
GitHub encrypted secrets allow you to store sensitive information as an environment variable. 
1. Imagine that we need a password to login to `some_website`, and we want to access it with our code hosted on GitHub. We could directly paste the password into our code, but if it is a public repo, everyone can see our password and thus login to our `some_website` account.
    ```yml
    password: my_password
    ```
0. Instead, we can save our password securely as a GitHub secret, and point our code to the secret name
    ```yml
    password: ${{ secrets.MY_SECRET_PASSWORD }}
    ```
    - In the example above, we created a repository secret named `MY_SECRET_PASSWORD`
    - Create a repository secret under `training (or other repo) > Settings > Secrets > New repository secret`
    - Only authorized individuals can access GitHub secrets, so now the public only sees that we are using a secret, encrypted password
0. Read more on [GitHub](https://docs.github.com/en/actions/reference/encrypted-secrets).
---

## Continuous Integration
Continuous Integration (CI) refers to the process of automating the integration of code changes. CI takes advantage of automated builds and tests, and is a tool to help developers quickly identify potential issues with their code. It is not intended to catch all bugs, but rather to be a quick, automated double-check and catch a few of the bigger bugs. GitHub Actions is great place to get started with CI.

#### Dependabot
Dependabot is a piece of software that automatically detects when the packages you use in your code (specified in the requirements file) release updated versions. Dependabot will automatically generate PRs (can get a bit annoying) to update your package requirements to ensure your code is using the latest package versions. Read more fro [GitHub's blog post](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/).
1. An example [file](./github/dependabot.yml) is included in this repo
    - The update interval is set to `monthly`, but you have many options
0. A thorough list of options can be found [here](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates)

#### GitHub Actions
In this repo, there is an example GitHub Actions workflow [YAML file](./.github/workflows/python-app.yml). We will walk through its structure, but I strongly encourage you to read more from GitHub on [Actions](https://docs.github.com/en/actions/reference) or [Python testing](https://docs.github.com/en/actions/guides/building-and-testing-python) specifically.

1. The workflow YAML file
    - The [docs](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstrategy) provide a far more complete explanation of the syntax than I will. But here's the TLDR
    - YAML file parts
        ```yml
        name: Python application
        ```
        - This is an optional identifier we can use to reference this specific workflow. You can name it whatever you like.
        - If you have multiple workflows, these names are more important.
        ```yml
        on:
        push:
            branches: [ main ]
            paths-ignore: [ 'requirements/**' ]
        pull_request:
            branches: [ main ]
            paths-ignore: [ 'requirements/**' ]
        schedule:
            - cron: "0 22 */4 * *"  # run every 4th day at 22:00 UTC
        workflow_dispatch:    # allow for running this manually
        ```
        - `on` allows you to specify exactly what triggers the workflow to run.
        - The `push` and `pull_request` lines specify that pushes and PRs to `main` will trigger the workflow
        - The extra argument `paths-ignore` specifies that the workflow should not be triggered if a push or PR only affects the `requirements/**` path. This is used to disable the workflow from running on Dependabot PRs.
        - The `schedule` lines specify the action be started at a specific time/frequency using cron syntax. [Crontab guru](https://crontab.guru/) is a great resource to making sure you schedule workflows appropriately. Note that GitHub Actions run on UTC time.
        - The `workflow_dispatch` line enables manual triggering of the workflow from GitHub
        ```yml
        jobs:
        build:
        ```
        - In this example file, there is only one job, called `build`. But you can specify multiple jobs if you want to separate the logs
        ```yml
        steps:
        - name: My Name
        ```
        - Each `- name:` argument specifies a unique step name that can be further examined in the GitHub actions logs. Descriptive names are useful if you ever want to dig into why a CI job failed.
0. Logs for each workflow run can be found under the `Actions` tab in your repo
    - You can filter the logs by workflow name in the left menu. In this repo, we only have `Python application`
    - Select the run with the desired trigger name. The name generally follows the PR name or commit message that triggered the workflow
    - Within the run, you will see a list of all the jobs. In this example, we only have the one job `build`
    - Select the job, and you will find a list of all the steps within the job.
    - You may explore the contents of each step log, but the interesting ones for this example are:
        - Step 5: Lint with flake8 [Example](https://github.com/wpklab/PyMetrology/runs/1889008436?check_suite_focus=true#step:5:11) -->
        Formatting warnings according to flake8 (differs from yapf).
        - Step 6: Test and Coverage Report [Example](https://github.com/wpklab/PyMetrology/runs/1889008436?check_suite_focus=true#step:6:7) --> 
        Results of all tests and summary of code coverage (number of lines found, number of lines not covered explicitly by tests, and % coverage). Take this with a grain of salt, as % coverage is not the ultimate guide to good code. 100% coverage can still have bad code if the tests are poorly designed. But in general, it is a good guide / sanity check.
0. Adding a badge
    - If you want to add a status badge for your GitHub workflow, you can follow this [guide](https://docs.github.com/en/actions/managing-workflow-runs/adding-a-workflow-status-badge)
    - See this repo's [`README.md`](./README.md) for an example

#### Testing
When we first write code, most of us also quickly write up some basic test cases to make sure things are working. Saving these test cases as "unit tests" can save you some time down the road.
- Unit tests are small test functions designed to check your code and ensure it is functioning properly. Unit tests typically cover main use cases and a handful of edge cases (i.e. situations that may arise on rare occasions)
- As time goes on, you will forget the tests you initially used to ensure the code functioned properly at the time of development. Writing unit tests is a way to document exactly what you tested, and provides an easy way to rerun those very same tests any time.
- You will **NEVER** find every bug in your code before deployment (pushing to `main`). Many will argue that writing unit tests is a waste of time, and they are right *if* you are hyper-focused on finding every bug and testing every edge case. Instead, view testing as a quick opportunity to run sanity checks, catch any big bugs, and ensure that code updates don't break the original intent of the function.
- CI tools can automatically run a suite of unit tests. This means all your test cases can be run automatically anytime, or at least whenever you trigger a CI workflow.

1. Setup
    - I prefer to store my tests in a separate `tests/` folder at the root of my project, but there are arguments for distributing tests within your code
    - I have included a sample test as an example at [`./tests/test_mistakes.py`](./tests/test_mistakes.py)
    - The `__init__.py` file is needed for import reasons
0. Naming convention
    - It is common to use `pytest` to run your test suite. You can discover more about `pytest` in the [docs](https://docs.pytest.org/en/stable/contents.html)
    - `pytest` discovers tests according to the [conventions for Python test discovery](https://docs.pytest.org/en/stable/goodpractices.html#test-discovery)
        - Test files should be named `test_*.py` or `*_test.py`
        - Test functions should be prefixed with `test`
    - I organize my test files according to the subpackage being tested, and name them `test_<subpackage_name>.py`
        - This training repo does not have any subpackages, just the main package of `learning`, so I named the file `test_mistakes.py` to indicate we are testing functions within the `mistakes.py` file
    - Within each file, I then name test functions a `test_<name_of_function_being_tested>`
        - In this example, the test name is `test_add`, indicating that I am testing the `add` function within the `mistakes.py` file
0. Run the tests locally
    - Within the command terminal, navigate to this project and activate the `venv`
    - Ensure you have the testing requirements installed, and run pytest
        ```bash
        pip install -U -r requirements/test.txt
        pytest
        ```
    - You will see a report printed to the command line indicating how many tests were run, how many passed, any failure or warning messages, and the time it took to run all tests

#### Code Coverage
Code coverage is a useful metric to gauge how much of your code is being covered by tests. Coverage results should be taken with a grain of salt, as % coverage is not the ultimate guide to good code. Terrible code can still have 100% coverage if the tests are poorly designed. But in general, it is a good guide / sanity check.

1. Tools
    - [Coverage.py](https://coverage.readthedocs.io/) is the base level tool used to test Python code coverage
    - [pytest-cov](https://pytest-cov.readthedocs.io/) is a plugin for coverage.py, that makes life much easier
    - [CodeCov](https://codecov.io/) is a third-party GUI for saving and viewing coverage reports, generating nice graphs and status badges, and viewing historical logs or coverage stats
0. See coverage locally
    - Within the command terminal, navigate to this project and activate the `venv`
    - Ensure you have the testing requirements installed, and run pytest-cov
        ```bash
        pip install -U -r requirements/test.txt
        pytest --cov=learning
        #      ^ location of package to be tested
        # this setup will try to auto-detect tests according to the pytest convention
        # Alternatively
        pytest --cov-config=.coveragerc --cov=learning tests/
        #      ^ optional configuration settings       ^ location of tests
        ```
    - You will see a report printed to the command line with the same `pytest` report, and some additional coverage statists (number of lines found, number of lines not covered explicitly by tests, and % coverage)
    - In the optional `.coveragerc` file, you can configure files or lines of code to exclude from the coverage report. Read more in the [docs](https://coverage.readthedocs.io/en/latest/config.html)
        - The configuration options will make more sense in the next step
        - I like to exclude `debug` lines, `__init__.py` files, and UI functions such as graphing functions
        - You can also explore the coverage of branch statements with the configuration `branch` setting, or by using the `--cov-branch` option. I use the default `branch=false`
0. See which lines are not covered
    - After running `pytest-cov` above, we want to see which lines are covered, not covered, and excluded within our project
    - Generate an html report 
        ```bash
        coverage html
        ```
    - This will create several files in a new folder named `htmlcov/`. Open `htmlcov/index.html` in a web browser; it will show a similar report as the command line.
    - Click on a specific file to show the code with missed lines highlighted in red. Alternatively you can open `htmlcov/<file_name>.html` directly 
        ![example_coverage_report](https://developer.ibm.com/recipes/wp-content/uploads/sites/41/2018/02/Screen-Shot-2018-02-01-at-3.35.59-PM.png)
    - If you use enable `branch` coverage, if statements where only certain branches are explored will be highlighted in yellow
        ![example_branch_coverage](https://i1.wp.com/improveandrepeat.com/wp-content/uploads/2021/01/Pytest_Cov_BranchOn.png?w=502&ssl=1)
0. Get fancy
    - If you want a fancy badge or to historically track your code coverage, look into tools such as [CodeCov](https://codecov.io/) and [Coveralls](https://coveralls.io/). CodeCov integrates nicely with GitHub and offers free coverage of private repos.
    - CodeCov's website has some good documentation for getting started with GitHub actions. I've also included a sample setup in this repo
        - The final step in my GitHub workflow uploads results to CodeCov
            ```yml
            - name: Upload Coverage to Codecov
              uses: codecov/codecov-action@v1
              with:
                token: ${{ secrets.CODECOV_TOKEN }}
            ```
        - Note that I use a secret to store my CodeCov upload token, which can be found on CodeCov ([quick start guide](https://docs.codecov.io/docs/quick-start))
            ![codecov_upload_token](https://files.readme.io/a1f8ca7-codecov-uploadreports.png)
        - You'll need to set up some things on CodeCov's end, but the whole process is straightforward
        - If you want to include a coverage badge in your README, navigate to your repo on CodeCov, click `Settings > Badge`, and copy the Markdown code

---
## SSH Authentication
The SSH (secure shell) protocol allows you to connect and authenticate to remote servers and services. You can use SSH to communicate with GitHub without supplying you username and personal access token. SSH is not required in most cases, but there are several circumstances in which it may be necessary or more convenient than HTTPS
- Follow [GitHub's tutorial](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) on setting up SSH authentication
- I recommend setting up an SSH key passphrase as an extra layer of security. Otherwise, anyone with access to your computer also gains access to GitHub and any other applications you use SSH for

---
## Packaging Code
Code is typically packaged in order to be conveniently accessible to other projects
- If you want your code to be **publicly accessible**, [PyPi](https://pypi.org/) is an excellent option for hosting packaged code, and enables user to `pip install <my_package>` your package
- If you want your code to remain **private**, there are three paths forward
    1. [**pip install**](#pip-install): install `my_package` like you would any publicly hosted python package
        - Best solution if you do not plan on making any changes to `my_package`, but want to use its functions
    0. [**git subtree**](#git-subtree): copy source code into a subtree of your main project (i.e. a new folder at the root)
        - Best if you want to co-develop `my_package` alongside your main project. Moderate Git proficiency is needed.
    0. [**git submodule**](#git-submodule): similar to subtree, this is the original tool in Git 
        - Good if you want to make modifications but not necessarily push changes up to `my_project`. Git proficiency is definitely needed.

#### pip install
Projects that are being packaged must have a `setup.py` file at the root of the directory. This file contains information for installing the package on your machine, as well as package metadata. When the package is published publicly, it also serves as the communication point for [PyPi](https://pypi.org/), which hosts public python packages that can be installed using `pip`.
- For information on packaging, see this [guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/) and this [tutorial](https://python-packaging.readthedocs.io/en/latest/minimal.html)
- I have included a simple [`setup.py`](./setup.py) file for this tutorial repo that will get you started
    - I like to only store the `__version__` number in the base [`__init__.py`](./learning/__init__.py) file. This way, there is only one line to update whenever a new version is released. There are a few lines of code to pull this value from the `__init__.py` file into the `setup.py` file
    - The project `name` parameter is what people will use to `pip install`, while the `packages` parameter is what people will `import` in their python code
        - These two do not need to be identical (e.g. opencv-python and cv2, or scikit-image and skimage), but having different names could lead to user confusion. I recommend you keep things simple
        - In this training example, I went the confusing route to demonstrate the possibility. My project name is `TrainingTutorials` while the package name is `learning`, meaning the functions can be imported under the name `learning`

For now, let's imagine the `TrainingTutorials` project is maintained privately. To run the equivalent of `pip install TrainingTutorials`, we will make use of the SSH protocol.
1. You will need Git Bash and SSH setup on your machine
    - Help getting started with Git Bash in the [beginner module](./beginner.md#initial-setup)
    - Help getting SSH setup from [earlier](#ssh-authentication)
0. In Git, navigate to the directory of a project that you want to install the `TrainingTutorials` project
    - At this point, you are capable of setting up your own repository for practicing in. Go ahead and use an existing repo or setup a practice one.
0. Still in Git, activate the `venv` for this project if appropriate. Note, you will need to run as source
    ```bash
    source venv/Scripts/activate
    ```
0. From GitHub, copy the SSH clone link to this training repo: `git@github.com:<username>/training.git`
    - We will use a modified version of this link
0. Install the `TrainingTutorials` project
    - To install the `TrainingTutorials` project directly, run the command 
        ```bash
        pip install git+ssh://git@github.com/<username>/training.git
        #                                   ^ change from ':' to '/'
        ```
    - Alternatively, you may wish to add `TrainingTutorials` to your installation requirements. Add the following line to your `requirements.txt` or equivalent
        ```bash
        git+ssh://git@github.com/<username>/training.git
        ```
    - Since we are using SSH to authenticate the `TrainingTutorials` download, you will need to run `pip install -U -r requirements.txt` from within Git. The command line does not have your SSH key to access GitHub.
0. Install a specific version of `TrainingTutorials`
    - As it is written, the previous steps will install the latest version from the `main` branch of this training repo. Running `pip freeze` will print out a list of all packages installed. The `TrainingTutorials` project will appear something like this
        ```bash
        TrainingTutorials @ git+ssh://git@github.com/<username>/training.git@75754a41f41709af11d71d7fed69f5bb64c2cecb
        #                                                                    ^ points to latest commit at install
        ```
    - You may instead wish to install the project from a specific release, commit, tag, or branch. To do this, explicitly point to the desired checkpoint using `@<pointer>` such as
        ```bash
        pip install git+ssh://git@github.com/<username>/training.git@75754a41f41709af11d71d7fed69f5bb64c2cecb
        # OR
        pip install git+ssh://git@github.com/<username>/training.git@my_branch
        # OR
        pip install git+ssh://git@github.com/<username>/training.git@0.1.0
        ```
0. Check the version
    - Since we included the `__version__` in our `__init.py`, we can check the release version of the install by importing the package in Python
        ```python
        import learning
        #      ^ notice we use the package name here, not the project name
        learning.__version__
        ```

### git subtree
Git subtree is an advanced technique that enables the co-development of a project alongside your main project. In this case, we will explore adding the `TrainingTutorials` project to another repo.

- Before getting started, I highly recommend reading the [subtree documentation](https://github.com/apenwarr/git-subtree/blob/master/git-subtree.txt)
    - Git subtree can be used with either URLs or remote tracking branches. In the examples below, I will show some use of URLs, but focus mostly on using remotes.
    - You can also choose whether or not to incorporate the commit history of the subtree project with the main project. I highly suggest using the `--squash` option to keep the main project history clean. The squash commit message is very detailed and provides enough traceability to look back at the subtree.
    - Personally, I use `--squash` and a remote branch because the Git commands are shorter, I don't have to create and remember Git aliases, and I can navigate the commit history easily enough. If the subtree history is very complex, I can always `git remote remove <remote_name>` to isolate the main project history. If you are against using remotes, I suggest you explore [Git aliases](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) and setup something similar to the following.
        ```bash
        git config alias.pushpractice 'subtree push -P practice https://github.com/<username>/training.git'
        #                ^ could be any desired alias

        # Now these commands are equivalent (pushing changes to the specified <branch>)
        git pushpractice <branch>
        git subtree push -P practice https://github.com/<username>/training.git <branch>

        # Do something similar for pulling
        git config alias.pullpractice 'subtree pull -P practice https://github.com/<username>/training.git'
        git pullpractice <branch/tag/commit>

        # To remove aliases, either remove a specific one, or edit the .gitconfig file
        git config --unset alias.<alias_name>
        # OR edit the config file manually
        vim .git/config     # and then delete the desired aliases
        ```
    - Note: if you want to set aliases that work outside your main project in Git, you need to include the `--global` option. This is not recommended for something as specific as these subtree aliases.
        ```bash
        git config --global alias.<alias_name> 'alias_command'

        # Remove in a similar way
        git config --global --unset alias.<alias_name>
        # OR
        vim ~/.gitconfig    # and then delete the desired aliases
        ```

**Adding the subtree**
1. Create a new branch in your training repo for all of your co-development work in the training subtree
0. Setup remote tracking to training (I'll call it `train_remote` here to avoid confusion)
    - *Suggested*: Use the `-f` option to `git fetch train_remote` immediately after setting up the remote
    - *Suggested*: Use the `--no-tags` option to not import tags from the remote. This will save you any confusion if you have similarly named tags in your main project
0. Add and merge the subtree from this remote (in the example, I create a subtree folder `./practice/`)
    - *Suggested*: Use the `--squash` option to condense all the training commits into one commit in your main project history
    - *Optional*: Edit the merge message. To accept the auto generated message, type `:wq` ([VIM cheat sheet](https://www.keycdn.com/blog/vim-commands))
    - *Optional*: Use `-m` or `--message` to specify a commit message for the merge commit (works with add, merge, and pull)
    - *Optional*: Use `-P` instead of writing `--prefix`
        ```bash
        git remote add -f --no-tags train_remote https://github.com/<username>/training.git
        git subtree add --squash --prefix practice train_remote <branch>
        #                                 ^        ^            ^ remote branch (recommend not main)
        #                                 |        └ name of the remote
        #                                 └ path to the subtree folder (mandatory for all commands)
        
        # If you want a specific tag, since we do not import tags on the remote, use the URL
        git subtree add --squash -P practice https://github.com/<username>/training.git <tag>
        ```
**Pull down changes made to PyMetrology**
1. Pull (or fetch and merge) changes from the remote subtree into your main project
    - *Suggested*: Use `--squash`
    - *Optional*: Edit the commit message for the merge commit
        ```bash
        git subtree pull --squash -P practice train_remote <branch>
        # Similar to add, we can pull specific tags
        git subtree pull --squash -P practice https://github.com/<username>/training.git <tag>
        
        # Note: `pull` is identical to `fetch` followed by `merge`
        git fetch train_remote
        git subtree merge --squash -P practice train_remote <branch>
        ```
**Push up subtree changes to PyMetrology**
1. Commit changes. Ideally, you keep commits separate for changes to subtrees and the main project, but this is not required
0. Push changes to the remote and your main project
    - If you use the standard `git push` instead, you can always go back to run `git subtree push`
        ```bash
        git add .
        git commit -m 'clear commit message'
        git subtree push -P practice train_remote <branch>
        ```
    - I actually recommend mostly using the standard `git push`. Each `git subtree push` invokes a march through all the commits in your repo history. Reducing the number of `git subtree pushes` will save you some time if your repo has 100+ commits

Additional resources: [Docs](https://github.com/apenwarr/git-subtree/blob/master/git-subtree.txt), [2](https://git-memo.readthedocs.io/en/latest/subtree.html), [3](https://www.atlassian.com/git/tutorials/git-subtree)

### git submodule
This is another avenue, but reviews indicate it is more hassle than git-subtrees. I will leave it here for reference, but will not explore its use.
Resources: [Docs](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

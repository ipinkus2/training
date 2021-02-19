# Moderate Tutorials
#### Sections
- [Merge conflicts](#merge-conflicts)
- [Formatting code](#formatting-code)
- [Git commands](#git-commands)
- [Versioning](#versioning)
- [Referencing](#referencing)
- [Multiple remotes](#multiple-remotes)
---
## Merge Conflicts
Merging and conflicts are a common part of the Git experience. Conflicts generally arise when two people have changed the same lines in a file, or if the same file was modified on both branches involved in the merge. Luckily, resolving a merge conflict is often straightforward. Let's get familiar with solving merge conflicts by purposefully creating a conflict in this next section, and solving it three different ways.
1. Checkout a new branch from the `main` branch and name it `conflict`
0. In VSC, open the `learning/mistakes.py` file and edit line 6
    ```python
    return ('Getting a PhD is easy')
    # update to say 
    return ('Getting a PhD is a piece of cake')
    ```
    - Add, commit, and push this change to the `conflict` branch. Perhaps the message is `bad joke`
0. Checkout `main` and edit the same line
    ```python
    return ('Getting a PhD is simple')
    ```
    - Add, commit, and push to `main`. Perhaps this message is `terrible joke`
0. In GitHub, open a PR `main <-- conflict`
    - You'll get a warning of the merge conflict. Create the PR anyway

        ![merge_conflict](./assets/merge_conflict_1.PNG)
        ![merge_conflict](./assets/merge_conflict_2.PNG)
    - Click on **Resolve conflicts** and you'll enter the GitHub editor. On the top, we have the incoming change from `conflict`, and below the `======` we have the current change from `main`

        ![merge_conflict](./assets/merge_conflict_3.PNG)
    - To resolve, simply pick one version, or a combination of the two, and delete the extra lines. To finish, click **Mark as resolved** and then **Merge**
    - Back in the PR, you can see there is a new merge commit that resolves the conflict
0. Close the PR without merging the PR. Now we want to undo all our merge work and try again another way
    - Checkout the `conflict` branch and take a look at the git log or git graph in VSC
    - Run `git fetch` to update the origin remote. You'll see the merge commit on `origin/conflict`, while your local `conflict` branch is behind `origin`
    - Run `git push -f` to force push your local code and overwrite the merge commit on `origin` 
    - **Alternatively**, if you pulled down the merge commit from `origin` to your local machine (meaning your last commit is a merge commit, combining the two branch histories), we can undo it and then force push
        ```bash
        $ git reset --merge HEAD~1
        $ git push -f
        ```
        - `git reset` can be dangerous, and I do not recommend it's use in general unless you fully understand what it does. It can be especially confusing for code that is worked on by multiple developers, as its use is untraceable (unlike `git revert`). Learn more by reading the [docs](https://git-scm.com/docs/git-reset)
        - `HEAD` refers to the current state of your repository, and `HEAD~1` is the last commit in your repository. Similarly `HEAD~2` is the second to last commit.
0. Now, let's manage a merge conflict with VSC
    - Merge `conflict` into `main`
        ```bash
        $ git checkout main
        $ git merge conflict
        > Auto-merging learning/mistakes.py
        > CONFLICT (content): Merge conflict in learning/mistakes.py
        > Automatic merge failed; fix conflicts and then commit the result.
        ```
    - In VSC, the **Source Control** tab shows our file under "Merge Changes" with a "C" for "Conflict." Clicking on it to view the conflict, we see

        ![merge_conflict](./assets/merge_conflict_4.PNG)
    - We can manually edit like before, or click one of the options at the top of the merge conflict. `Accept Current Change` will save `Getting a PhD is simple` and discard the rest. You can explore the other options.
    - You can save your changes, edit the commit message in VSC if desired, and commit the merge by clicking the check mark. *But don't click just yet!*
0. Let's see if we can fix this entirely in Git
    - We will use VIM for this, so it will be useful to know some [basic commands](https://www.radford.edu/~mhtay/CPSC120/VIM_Editor_Commands.htm)
        - Type `vim learning/mistakes.py` to open the file with VIM and see the merge conflict
        - Use the arrow keys to move the curser around
        - Type `i` to switch to "insert" mode
        - Hit `Esc key` to switch back to command mode
        - Type `:wq` to write your changes (save) and quit VIM
    - Back in Git
        ```bash
        $ git status    # optional
        $ git add .
        $ git status    # optional
        $ git commit    # note I left off the -m 'message' part
        # There is a default merge commit message in place
        # Edit it with VIM commands and :wq
        # Or just accept the default and :q
        $ git push      # to finally push the merge changes to master
        ```    
---
## Formatting Code


---
## Git Commands
    - git cherry-pick
    - git reset

---
## Versioning

---
## Referencing
- commits
- PRs and issues
- in commit messages

---
## Multiple remotes

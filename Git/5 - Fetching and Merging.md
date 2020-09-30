### How to synchronize your forked and local repositories with the original one on GitHub?

- Change the current working directory to your local project.
    ```cd [your_directory] ```

-  Change to your desired branch
    - You’ll probably want to merge to your master – so make sure your branch is “master”.
    - You can change it from GitHub Desktop, if you’re using it!
        Or you can run this:
        ```git checkout [branch_name]```

 - Configure the origin as a remote repository
        This needs to be done to enable you to fetch the new commits from it
You can verify if it already is by running this:

    ```
    git remote -v
    ```
    If it isn’t, then run this:
    ```
    git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
    ```

- Sync your local repository with the upstream (the original one)

    ```
    git fetch upstream 
    ```
    Perform merge
    ```
    git merge upstream/master
    ```

 - If you get a text editor window in your bash, that’s just Vi asking for your commit comment for your merge. Don’t have to enter anything, just write “:wq” and you should be good.
 - Push your local changes to your repository
        You can do this in GitHub Desktop or by running this:

        git push 

And now you should be good.

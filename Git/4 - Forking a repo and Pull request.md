# How to create a pull request in GitHub 
## ![forkrepo.png](https://opensource.com/sites/default/files/uploads/forkrepo.png)

Use Kulkarni's [my demo repo](https://github.com/kedark3/demo) to try it out.

Once there, click on the **Fork** button in the top-right corner. This creates a new copy of my demo repo under your GitHub user account with a URL like:
**https://github.com/&lt;YourUserName&gt;/demo**

The copy includes all the code, branches, and commits from the original repo.

Next, clone the repo by opening the terminal on your computer and running the command:
`git clone https://github.com/YourUserName/demo`

Once the repo is cloned, you need to do two things:

1. Create a new branch by issuing the command:
```
git checkout -b new_branch
```
2. Create a new remote for the upstream repo with the command:

```
git remote add upstream https://github.com/kedark3/demo
```

In this case, "upstream repo" refers to the original repo you created your fork from.

Now you can make changes to the code. The following code creates a new branch, makes an arbitrary change, and pushes it to **new_branch**:
```
$ git checkout -b new_branch
Switched to a new branch ‘new_branch’
$ echo “some test file” > test
$ cat test
Some test file
$ git status
On branch new_branch
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    test
nothing added to commit but untracked files present (use "git add" to track)
$ git add test
$ git commit -S -m "Adding a test file to new_branch"
[new_branch (root-commit) 4265ec8] Adding a test file to new_branch
 1 file changed, 1 insertion(+)
 create mode 100644 test
$ git push -u origin new_branch
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 918 bytes | 918.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
Remote: Create a pull request for ‘new_branch’ on GitHub by visiting:
Remote:   http://github.com/example/Demo/pull/new/new_branch
Remote:
 * [new branch]         new_branch -> new_branch
```

Once you push the changes to your repo, the **Compare & pull request** button will appear in GitHub.

## ![compare-and-pull-request-button.png](https://opensource.com/sites/default/files/uploads/compare-and-pull-request-button.png)

Click it and you'll be taken to this screen:

## ![open-a-pull-request_crop.png](https://opensource.com/sites/default/files/uploads/open-a-pull-request_crop.png)

Open a pull request by clicking the **Create pull request** button. This allows the repo's maintainers to review your contribution. From here, they can merge it if it is good, or they may ask you to make some changes.

## TLDR

In summary, if you want to contribute to a project, the simplest way is to:

1. Find a project you want to contribute to
2. Fork it
3. Clone it to your local system
4. Make a new branch
5. Make your changes
6. Push it back to your repo
7. Click the **Compare & pull request** button
8. Click **Create pull request** to open a new pull request

If the reviewers ask for changes, repeat steps 5 and 6 to add more commits to your pull request.

Happy coding!

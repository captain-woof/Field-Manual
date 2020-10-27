
## Don't be nervous. This beginner's guide will quickly and easily get you started using Git.

## Step 1: Create a GitHub account

The easiest way to get started is to create an account on ![gitHub.com](https://github.com/) (it's free).

## ![git_guide1.png](https://opensource.com/sites/default/files/u128651/git_guide1.png)

Pick a username (e.g., octocat123), enter your email address and a password, and click **Sign up for GitHub**. Once you are in, it will look something like this:

## ![git_guide2.png](https://opensource.com/sites/default/files/u128651/git_guide2.png)

## Step 2: Create a new repository

A repository is like a place or a container where something is stored; in this case we're creating a Git repository to store code. To create a new repository, select **New Repository** from the `+` sign dropdown menu (you can see I've selected it in the upper-right corner in the image above).

## ![git_guide3.png](https://opensource.com/sites/default/files/u128651/git_guide3.png)

Enter a name for your repository (e.g, "Demo") and click **Create Repository**. Don't worry about changing any other options on this page.

Congratulations! You have set up your first repo on GitHub.com.

## Step 3: Create a file

Once your repo is created, it will look like this:

## ![git_guide4.png](https://opensource.com/sites/default/files/u128651/git_guide4.png)

Don't panic, it's simpler than it looks. Stay with me. Look at the section that starts "...or create a new repository on the command line," and ignore the rest for now.

Open the _Terminal_ program on your computer.

## ![git_guide5.png](https://opensource.com/sites/default/files/u128651/git_guide5.png)

Type `git` and hit **Enter**. If it says command `bash: git: command not found`, then [install Git](https://www.linuxbabe.com/linux-server/install-git-verion-control-on-linux-debianubuntufedoraarchlinux#crt-2) with the command for your Linux operating system or distribution. Check the installation by typing `git` and hitting **Enter**; if it's installed, you should see a bunch of information about how you can use the command.

In the terminal, type:

```
mkdir Demo
```

This command will create a directory (or folder) named _Demo_.

Change your terminal to the _Demo_ directory with the command:

```
cd Demo
```

Then enter:

```
echo "#Demo" >> README.md
```

This creates a file named `README.md` and writes `#Demo` in it. To check that the file was created successfully, enter:

```
cat README.md
```

This will show you what is inside the `README.md` file, if the file was created correctly. Your terminal will look like this:

## ![git_guide7.png](https://opensource.com/sites/default/files/u128651/git_guide7.png)

To tell your computer that _Demo_ is a directory managed by the Git program, enter:

```
git init
```

Then, to tell the Git program you care about this file and want to track any changes from this point forward, enter:

```
git add README.md
```

## Step 4: Make a commit


So far you've created a file and told Git about it, and now it's time to create a _commit_. Commit can be thought of as a milestone. Every time you accomplish some work, you can write a Git commit to store that version of your file, so you can go back later and see what it looked like at that point in time. Whenever you make a change to your file, you create a new version of that file, different from the previous one.

To make a commit, enter:

```
git commit -m "first commit"
```

That's it! You just created a Git commit and included a message that says _first commit_. You must always write a message in commit; it not only helps you identify a commit, but it also enables you to understand what you did with the file at that point. So tomorrow, if you add a new piece of code in your file, you can write a commit message that says, _Added new code_, and when you come back in a month to look at your commit history or Git log (the list of commits), you will know what you changed in the files.

## Step 5: Connect your GitHub repo with your computer

Now, it's time to connect your computer to GitHub with the command:
<pre>
<span><code>git remote add origin https://github.com/&lt;your_username&gt;/Demo.git</code></span></pre>

Let's look at this command step by step. We are telling Git to add a `remote` called `origin` with the address `https://github.com/<your_username>/Demo.git` (i.e., the URL of your Git repo on GitHub.com). This allows you to interact with your Git repository on GitHub.com by typing `origin` instead of the full URL and Git will know where to send your code. Why `origin`? Well, you can name it anything else if you'd like.

Now we have connected our local copy of the _Demo_ repository to its remote counterpart on GitHub.com. Your terminal looks like this:

## ![git_guide8.png](https://opensource.com/sites/default/files/u128651/git_guide8.png)

Now that we have added the remote, we can push our code (i.e., upload our `README.md` file) to GitHub.com.

Once you are done, your terminal will look like this:

## ![git_guide9.png](https://opensource.com/sites/default/files/u128651/git_guide9.png)

And if you go to `https://github.com/<your_username>/Demo` you will see something like this:

## ![git_guide10.png](https://opensource.com/sites/default/files/u128651/git_guide10.png)

That's it! You have created your first GitHub repo, connected it to your computer, and pushed (or uploaded) a file from your computer to your repository called _Demo_ on GitHub.com. Next time, I will write about Git cloning (downloading your code from GitHub to your computer), adding new files, modifying existing files, and pushing (uploading) files to GitHub.


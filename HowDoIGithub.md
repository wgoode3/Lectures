# How do I upload to Github?

### Step 0 - Make sure you have git installed on your computer

```shell
git --version
```

This should respond back with the version number for git. For me it says ```git version 2.17.1```.

### Step 1 - In the project of your choosing Initialize git

Change directory into the project you want on github and then initialize git.

```shell
cd Desktop/MyAwesomeProject
git init
```

### Step 1.5 - Make a .gitignore file and add anything you don't want to push in there

```shell
touch .gitignore
nano .gitignore
```

Inside of ```.gitignore``` specify what you want to not be tracked by git.

Examples of what to include would be...

```
# ignore files that end in .pyc
*.pyc
# ignore a folder called __pycache__
__pycache__/
```

### Step 2 - Add the files to git

This will add everything where you are.

```shell
git add .
```

This will add just a single file named ```README.md```.

```shell
git add README.md
```

### Step 3 - Make a Commit

```shell
git commit -m "your message here"
```

Try to keep the message short and descriptive about what you are committing. For the first commit for a project something like "initial" will be fine. If you are fixing a bug specify that "fixed a broken link".

### Step 4 - Create a Github Repository

Go to github.com and make a new Repository...

<INSERT IMAGES HERE />

### Step 5 - Add the Github Repository as a Remote

<INSERT IMAGES HERE />

```shell
git remote add origen https://github.com/your_username/your_repo_name.git
```

**Note** make sure you upload using ```https``` and not using ```ssh```.

### Step 6 - Push

```shell
git push -u origin master
```

You may be prompted for your username and password for github.

After you have pushed your project the first time, you won't need to follow all of these exact steps, instead do something like...

```shell
git add .
git commit -m "added features && fixed bugs"
git push
```

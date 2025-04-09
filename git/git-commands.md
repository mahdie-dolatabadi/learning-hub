# Git Commands I Use Regularly

## 🟢 Initialize & Clone
### ✅ Create an empty Git repository or reinitialize an existing one
```bash
git init
```

### ✅ Download existing source code from a remote repository
```bash
git clone <repo-url>
```

### ✅ Set configuration values
```bash
# Set the name
git config --global user.name "your-name"
# Set the email
git config --global user.email "your-email"
# Show all the configurations
git config --list
# Build aliases for git commands. Here, you can use "git hello" instead of "git init"
git config --global alias.hello init

```

## 🟢 Basic commands
### ✅ Add changes to the current directory
```bash
git add
```

### ✅ Record the changes made to the files to a local repository.
```bash
git commit -m "commit-message"
```
#### The two commands above help us to track changes and store them.

### ✅ Remove a file from staging and working dir(lm)
```bash
git rm
```

### ✅ Delete a branch locally
```bash
git branch -d <branch-name-for-deletion>
```

### ✅ Delete a branch remotely
```bash
git push --delete <remote-name>(origin) <branch-name>
```

## 🟢 Information
### ✅ Display the current state of the working directory and current repository(added, deleted, or modified files)
```bash
git status
```

### ✅ Show the changes that we have made on the branch that we're on
```bash
git show
```

## 🟢 Collaborating
### ✅ Create a new branch and switch to the branch at the same time
```bash
git checkout -b <new-branch-name>
```

### ✅ Change the branch
```bash
git switch <destiny-branch-name>
```

### ✅ take the independent lines of development and integrate them into a single branch
```bash
git merge <independent-branch-name>
```

### ✅ Upload the changes from local repository to the remote repository
```bash
git push <remote-name> <branch-name>
```

### ✅ fetch changes from a remote repository and merges them with your local repository.
```bash
git pull <remote-name>(origin) <branch-name>
```




# GitHub Commit Workflow — Quick Guide

## What a “commit” is

A **commit** is a snapshot of your project history. You usually:

- Edit files
- Stage changes (`git add`)
- Create a commit (`git commit`)
- Push commits to GitHub (`git push`)

## One-time setup (recommended)

### Configure your name and email

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Check which branch you use

```bash
git branch
```

Many repos use `main` (not `master`).

## Basic daily flow

### 1) See what changed

```bash
git status
```

### 2) Review your changes

```bash
git diff
```

### 3) Stage changes

Stage everything:

```bash
git add .
```

Stage specific files:

```bash
git add docs/ mkdocs.yml
```

Stage interactively (best for clean commits):

```bash
git add -p
```

### 4) Create the commit

```bash
git commit -m "Add List and ConcurrentHashMap cheat sheets"
```

### 5) Push to GitHub

```bash
git push origin main
```

If your branch is not `main`, push your current branch:

```bash
git push -u origin <branch-name>
```

## Good commit messages

Use **imperative mood** (like a command):

- `Add List cheat sheet`
- `Fix code block CSS border`
- `Update nav for new docs`

If you want a simple convention:

- `Add ...`
- `Fix ...`
- `Update ...`
- `Refactor ...`

## Create a feature branch (recommended)

```bash
git checkout -b docs/add-cheatsheets
```

Work and commit as usual, then push:

```bash
git push -u origin docs/add-cheatsheets
```

Then open a **Pull Request** on GitHub to merge into `main`.

## Common issues

### “nothing to commit, working tree clean”

- You have no changes staged or unstaged.

### “changes not staged for commit”

- You edited files but didn’t run `git add`.

### Undo staging (keep your edits)

```bash
git restore --staged .
```

### Undo local edits (danger)

```bash
git restore .
```

### Fix last commit message (not pushed yet)

```bash
git commit --amend -m "Better message"
```

### You committed but forgot to add a file

```bash
git add <file>
git commit --amend --no-edit
```

### Pull latest changes before pushing

```bash
git pull --rebase
```

## Typical workflow for this MkDocs repo

```bash
git status
git add docs/ mkdocs.yml
git commit -m "Add new cheat sheets"
git push origin main
```

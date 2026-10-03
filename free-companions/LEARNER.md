# GitHub and Local Setup

These optional companions help you save, review and share fictional practice code. Python Fundamentals can stay in Hafa and Learn without installing software or creating a GitHub account. Choose local setup when a course needs local files, packages or a real Git repository. Agent Workflows requires the local Git route before it begins. Rails and other local courses need their own runtime setup; these Python steps do not install Ruby or Rails.

Use a disposable practice folder and repository, not client work. Keep passwords, API keys, private keys and private information out of files, commits and submissions. Follow the current official references for your computer; versions and screens can change. The guide does not establish that your installation or account works: completion evidence comes from your own run and access checks.

Suggested routes: browser GitHub G0→G1→G2→G3→G4; local Mac S0→M1→M2, then G5→G6→G7; local Windows S0→W1→W2, then G5→G6→G7. The local Git route also needs the G1 repository/account. Use S1 whenever you need troubleshooting or a completion check. You may skip lessons that your current course does not need.

## G0 — Git, GitHub and a reviewable version

Git records versions of files on your computer. GitHub can host a copy and a change for someone to review. A commit is a saved version with a short explanation. A branch holds a proposed line of work separately. A pull request shows a proposed change and its checks.

The browser route teaches these ideas without installation. The local route adds clone, diff, commit, push and update on real files. Agent Workflows needs that local route so you can inspect an agent's actual changes. Browser-only edits do not satisfy its local prerequisite.

Choose the route your course needs. Before using a real file, check that it contains only fictional practice information. Do not include passwords, tokens, private client data or student details.

### Practice evidence

Write two sentences explaining where Git saves a version and what GitHub adds. State which route you will use and why. A Python Fundamentals learner may choose Hafa and skip GitHub/local installation.

## G1 — Account and first repository in the browser

Use [GitHub account setup](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) and [creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository). Finish verification/security prompts privately before the code exercise.

1. Sign in to your own GitHub account and choose New repository.
2. Name it `csg-github-practice`. Use public only for fictional practice code you are comfortable sharing. A private repository needs an explicit instructor invitation later.
3. Add a README to create an initial commit. Use `main` as this practice repository's default branch. If your account gives a different name, follow [GitHub's branch-renaming instructions](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch) to name this disposable practice branch `main` before following the later commands.
4. Create the repository. Use its add-file action to create `hello.py` with this line:

```python
print("Hafa adai, CSG!")
```

5. Preview the file and commit directly to `main` with message `Add greeting program`.
6. Open `hello.py` and its history to confirm the saved version. The web editor stores code; it does not prove Python ran.
7. Paste the line into Hafa's Python runner and run it. Expected output:

```text
Hafa adai, CSG!
```

If the name ends in `.txt`, rename it to `hello.py`. If the output differs, compare the saved characters and quotation marks. Account verification is an account step, not a Python error. If you cannot access the runner, send the sanitized issue to course support rather than claiming the code ran.

### Practice evidence

Keep your repository URL, the greeting code and actual output. Confirm a README, `hello.py` and the greeting commit exist. Do not include account verification or recovery codes.

## G2 — Read a diff and save another change

Open your G1 `hello.py` on `main`. Append this second line without removing the greeting:

```python
print("I can explain one saved change.")
```

Preview the change or open its diff before committing. Additions and removals show what changed; the commit message alone cannot prove the file is correct. Run both lines in Hafa. Expected output:

```text
Hafa adai, CSG!
I can explain one saved change.
```

Commit with `Add explanation message`. Open history and find the earlier one-line version. Then add a third `print` message in your own words, run all three lines, inspect the diff and save a new meaningful commit.

If you edited the wrong file, leave the proposed change uncommitted, reopen `hello.py` and make the intended edit. Check the file and branch before saving. Do not commit unrelated files just to get past this exercise.

### Practice evidence

Record the new commit link and explain one added line. Keep the actual output including your third message.

## G3 — Branch, pull request and review

Start on `main` in your practice repository. Create a branch named `add-practice-goal` using GitHub's branch selector. Confirm that branch name before editing. On this branch, append the following to README:

```markdown
## Practice goal
I want to make a small household report I can explain.
```

Use your own fictional goal if you prefer. Commit the README change as `Add practice goal`. The sentence now belongs to your proposal branch; it is not yet on `main`.

Open a compare/pull request from `add-practice-goal` **into `main`**. Title it `Add practice goal`. A suitable description is:

```text
Added one practice goal to README.
Checked the diff and confirmed hello.py is unchanged.
```

Open Files changed. Expect one README addition and no unrelated file. Confirm the source/target branches. In your own disposable practice repository, review and merge your change after checking it; real teams have their own review rules. Return to `main` and confirm the goal appears there.

If a file or target branch is wrong, correct the proposal before merging. If the diff includes a password or private information, stop and contact the instructor. Deleting it in a later commit does not erase earlier history.

### Practice evidence

Keep the PR link, its checked README diff and the goal visible on `main` after merge. Explain why you created a branch first.

## G4 — Submit your version and verify access

In the relevant Learn practice activity, submit the repository URL, PR URL, code being reviewed and actual run output. Pasted code preserves the review version even if you edit the repository later. For a public practice repository, check that its links open while signed out.

For a private personal repository, get the exact instructor GitHub username supplied for your enrollment. Open repository Settings and the collaborator-access area, invite only that person, and wait for acceptance. Then ask the instructor to check the repository from their own account. A pending invitation or copied URL does not prove access. Personal-repository [collaborator permissions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository) allow writing, so use only the intended instructor and this disposable repository. [GitHub collaborator instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository) explain the current steps.

Keep private work private while resolving access problems. Use the current official page if a label moved. [GitHub authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github) explains account access.

### Practice evidence

Submit links, reviewed code/output and either your signed-out public check or the instructor's accepted/private-access confirmation. If access is still pending, state that plainly and contact support.

## S0 — Choose browser or local setup

Python Fundamentals can keep using Hafa and Learn. These local steps are optional for that course. Use them when you need local files, packages or real Git; advanced Agent Workflows requires local Git. Choose M1/M2 for Mac or W1/W2 for Windows with Ubuntu WSL. Then complete G5–G7 for GitHub authentication, clone and push.

A work or school computer may restrict installations. Ask its administrator or use an approved personal computer. Follow the computer owner's installation permissions. Keep practice data fictional and use a dedicated folder. The first local check is running a saved file; the next is saving and reviewing a Git change.

### Practice evidence

Record your route and whether installation is permitted on the computer. If local setup is unnecessary for your current course, keep the working Hafa route and skip the installation lessons.

## M1 — macOS Python and editor

Open Terminal and run each command separately:

```sh
python3 --version
git --version
```

If Python is missing or only an unsuitable Apple-managed copy is available, read [Python on macOS](https://docs.python.org/3/using/mac.html) and choose a supported standard installer from [Python's official macOS downloads](https://www.python.org/downloads/macos/). Check its supported systems and publisher, then install with the owner's permission. Finish the installer guide's `Install Certificates.command` step in the installed Python folder under Applications. Do not modify/delete Apple's Python. Open a new Terminal and repeat the version check. Ask support if the chosen installer/runtime still cannot be found.

For Git, follow [Git's macOS installation guidance](https://git-scm.com/install/mac). If Git is missing and installation is authorized, request Apple's command-line tools:

```sh
xcode-select --install
```

Finish the dialog, reopen Terminal and check `git --version`. Full Xcode is not required by this exercise.

Install or open VS Code using [its official macOS guide](https://code.visualstudio.com/docs/setup/mac). Choose the supported build for your Mac, open its downloaded disk image and move the app to Applications. Then create a dedicated folder:

```sh
mkdir -p ~/csg-practice
cd ~/csg-practice
pwd
```

Open that same folder through the editor's Open Folder action. Create `hello.py` as a plain code file, save it, and enter:

```python
print("Hafa adai, CSG!")
```

Run the saved file in Terminal:

```sh
python3 hello.py
```

Expect `Hafa adai, CSG!`. Change only the greeting text to `Hafa adai from my Mac`, save and run again. If the file cannot be found, check `pwd` and `ls`; the terminal must be in the folder where the file was saved. Check for an accidental `.py.txt` suffix before reinstalling anything.

### Practice evidence

Keep the actual Python/Git versions and both run outputs. Note the file/folder relationship without exposing your personal home path in public screenshots. Installer success must be checked on your own computer.

## M2 — Local Git identity and first commit

Start with the saved `hello.py` in the M1 `csg-practice` folder and working Git. This folder is the local-init exercise; keep it separate from G6's later clone. If it already has Git history, inspect it with your instructor rather than rerunning an initialization over unknown work.

Run these one at a time, replacing the fictional identity with your chosen commit name and email or GitHub no-reply address:

```sh
git init -b main
git config user.name "CSG Demo"
git config user.email "csg-demo@example.com"
git status --short
git add hello.py
git diff --cached
git commit -m "Add local greeting"
git status --short
git log --oneline -1
```

The identity settings apply to this repository; they do not change your identity in other projects. Initially short status shows `hello.py` as untracked. Add selects that file; cached diff shows exactly what the next commit will contain. Read it before committing. A clean short status prints no file entries. Log shows a commit whose hash will differ on your computer.

If Git says your identity is unknown, set the local name/email and retry the commit. To unstage an unintended file while keeping it, run `git restore --staged` followed by its actual filename. Do not add unrelated files or secrets. If your Git lacks `init -b` or `switch`, use its official install/update guidance and ask support rather than improvising history changes.

### Practice evidence

Keep one commit hash and a clean status result. Explain untracked, staged and committed in your own words. A local commit is not yet a GitHub upload.

## W1 — Windows and Ubuntu WSL

This route uses Ubuntu inside WSL, not Windows-native Python/Git. Follow [Microsoft's current WSL installation instructions](https://learn.microsoft.com/en-us/windows/wsl/install) and their supported-system requirements. These steps are intended for an authorized, supported Windows setup; a restricted computer needs its administrator's help.

Open PowerShell in administrator mode and inspect before installing:

```powershell
wsl --list --verbose
```

If Ubuntu already exists, open it rather than reinstalling. If it is absent and installation is allowed, run:

```powershell
wsl --install -d Ubuntu
```

Follow installation/restart prompts. Open Ubuntu and create its Linux user. Password entry displays no characters; keep that password private. After a restart, reopen Ubuntu and check the distribution list in PowerShell again. Use Microsoft's guide if the command is unavailable or installation stalls; preserve existing distributions and ask support if blocked. The later `apt`, Python and Git commands belong in Ubuntu, not PowerShell.

### Practice evidence

Confirm you can open Ubuntu and identify which terminal accepts Linux commands. Record the distribution/version result without passwords or sensitive account information. An installed icon alone is not a working runtime check.

## W2 — Python, Git and VS Code in the same WSL environment

Open **Ubuntu**, then run each command separately:

```sh
sudo apt update
sudo apt install python3 python3-venv git openssh-client
python3 --version
git --version
mkdir -p ~/csg-practice
cd ~/csg-practice
pwd
```

Apt updates package information and installs the named tools. Sudo may ask for your Linux password without displaying characters. Use the computer's approved sources; see [Ubuntu package management](https://ubuntu.com/server/docs/how-to/software/package-management/). Keep this project in the Linux home folder. Windows and Ubuntu have distinct paths/runtimes.

Install supported VS Code on the **Windows side**, including its Add to PATH option, and Microsoft's WSL extension using [the official WSL guide](https://code.visualstudio.com/docs/remote/wsl). From Ubuntu run:

```sh
code .
```

Confirm the editor shows its WSL connection. Create and save `hello.py` in this Linux folder:

```python
print("Hafa adai, CSG!")
```

In the Ubuntu/WSL terminal run:

```sh
python3 hello.py
```

Expect `Hafa adai, CSG!`. If `code .` is missing, reopen the terminal or use VS Code's command palette → WSL: Connect to WSL, then open this Linux folder. Do not install an unrelated Linux editor package to fix the Windows editor command. If Python cannot find the file, check `pwd`, `ls`, the saved name and editor environment.

Now perform the local Git exercise **inside Ubuntu**, using your chosen commit identity instead of the fictional example:

```sh
git init -b main
git config user.name "CSG Demo"
git config user.email "csg-demo@example.com"
git status --short
git add hello.py
git diff --cached
git commit -m "Add local greeting"
git status --short
git log --oneline -1
```

Read the staged diff before committing. If this folder already has history, inspect it first. Use M2's identity/unstaging recovery if needed. Keep this folder separate from the later GitHub clone.

### Practice evidence

Keep the actual greeting output, one local commit and clean short status. Explain how you know both the editor and terminal used Ubuntu rather than Windows-native tools.

## G5 — Authenticate local Git with a named SSH key

Prerequisites: G1 account/repository and either M1/M2 or W1/W2. The demonstrated route uses SSH. If you already have a working approved HTTPS credential manager, keep it and use your repository's HTTPS clone URL; do not replace access just for practice. The SSH-specific commands below apply only to the named SSH route.

Official references: [key generation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), [registering a public key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account), [connection testing](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection), and [current host fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints).

In your Mac or Ubuntu terminal, check the specifically named key first:

```sh
mkdir -p ~/.ssh
ls ~/.ssh/csg_practice_ed25519 ~/.ssh/csg_practice_ed25519.pub
```

If either file exists, stop creation and reuse/repair that key with help. Only when **both files are absent**, create it:

```sh
ssh-keygen -t ed25519 -C "CSG practice" -f ~/.ssh/csg_practice_ed25519
```

Never accept an overwrite prompt. Choose a passphrase and enter it privately. The file without `.pub` is private and stays on this computer. Display only the public half:

```sh
cat ~/.ssh/csg_practice_ed25519.pub
```

Copy only that public line into your GitHub account Settings → SSH and GPG keys → New SSH key. Choose Authentication key, name it `CSG practice computer`, and save it. This connects the private key to your own account; it does not give an instructor repository access.

Test this specific key:

```sh
ssh -i ~/.ssh/csg_practice_ed25519 -o IdentitiesOnly=yes -T git@github.com
```

On a first connection, compare the offered fingerprint with GitHub's current official fingerprint page before accepting it. A successful message names the authenticated account and says shell access is unavailable; GitHub can return status 1 for this successful test. `Permission denied` has not passed the gate. Check the registered public key, selected private file and account. This route asks for the passphrase when needed and does not require a background SSH agent. Keep private keys/passwords out of Learn.

### Practice evidence

Record whether the intended account authenticated, with sensitive account details omitted where appropriate. Do not submit a key, passphrase or full credential screen. Resolve failed authentication before cloning/pushing.

## G6 — Clone, branch, inspect, commit and push

Start after G5 authentication, with your G1 repository available. In GitHub's Code menu, copy its **actual SSH clone URL**. Read [cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and [Git setup](https://docs.github.com/en/get-started/git-basics/set-up-git) if your repository differs.

In the following clone command, `PASTE_ACTUAL_SSH_URL` is a placeholder: replace it with the copied address before running. It is not literal command text. Use your own commit identity instead of the demo identity.

```sh
cd ~
mkdir -p csg-local-git
cd csg-local-git
git -c core.sshCommand="ssh -i ~/.ssh/csg_practice_ed25519 -o IdentitiesOnly=yes" clone PASTE_ACTUAL_SSH_URL
cd csg-github-practice
git config core.sshCommand "ssh -i ~/.ssh/csg_practice_ed25519 -o IdentitiesOnly=yes"
git config user.name "CSG Demo"
git config user.email "csg-demo@example.com"
git remote -v
git status --short
git switch -c add-local-message
```

Clone creates a new local copy with history and an `origin` pointing to GitHub. Keep it separate from the earlier init folder; do not run `git init` inside this clone. Confirm the remote points to your practice repository and the branch is `add-local-message`. If the destination already exists, reopen the known clone or choose a new disposable parent folder; do not delete unknown work. If you retained working HTTPS access, use `git clone` with your actual HTTPS URL and omit both SSH-specific configuration commands.

Open this clone's `hello.py` in the editor, preserve its earlier lines and append:

```python
print("A local change I checked myself.")
```

Save, then run and inspect before committing:

```sh
python3 hello.py
git diff
git add hello.py
git diff --cached
git commit -m "Add checked local message"
git push -u origin add-local-message
```

The earlier messages remain; the last output should be `A local change I checked myself.` Diff shows the unstaged change; cached diff shows the staged change. Commit saves locally. Push uploads the branch and `-u` remembers its upstream. A local commit alone does not prove GitHub received it.

Open the repository online and confirm the branch, commit and exact added line. Create a PR from `add-local-message` into `main`. Describe the command you ran and actual output. If push fails, retain your local commit and inspect the error. For authentication, repeat G5; for a wrong remote, compare with the correct Code URL before changing it. If a shared-branch push is rejected, fetch/ask for help; do not force-push.

### Practice evidence

Keep your checked diff, local commit hash, actual run output and PR link. Confirm the uploaded branch contains the same saved line you reviewed locally.

## G7 — Review, update local main and prove access

Review your G6 PR's one-line change. Confirm its target is `main` and no unrelated/private information is included. Merge only after that check in this disposable repository. Then return to your local clone:

```sh
git switch main
git pull --ff-only origin main
python3 hello.py
git log --oneline -3
git status --short
```

The online merge does not automatically update your local folder. `--ff-only` permits a straightforward history update and stops if histories diverged; it does not silently add another merge. Run again and confirm the new line is on local `main`. Submit the commit, PR link, reviewed code and output in Learn. A private repository still needs accepted instructor access and a distinct-account check as in G4.

If switching would overwrite local changes, keep them and commit the intended work on its branch or ask for help. Do not use a hard reset to hide the warning. If pull cannot fast-forward, preserve the folder and ask for a review of both histories.

For Agent Workflows, actual local clone, branch, visible diff, checked commit, successful push and local update are prerequisites. Browser-only editing does not demonstrate them.

### Practice evidence

Keep the local `main` run output, recent commit history and clean status. Confirm the reviewed version is reachable by the intended instructor; report a pending access check honestly.

## S1 — Troubleshoot and collect completion evidence

For a missing command, confirm the terminal and spelling. For a missing file, check `pwd` and `ls`. For different output, compare the saved file and its run. For installation permission, check the publisher/component and ask the computer owner or administrator if needed.

Send course support your OS, exact command, sanitized non-sensitive output, expected result and one step you tried. Omit private keys, tokens, passwords, recovery codes, sensitive account details and personal home paths from public screenshots.

Completion depends on the route:

- Python/browser: a working Hafa greeting is sufficient; no account or local installation is required by Fundamentals.
- GitHub web: repository, meaningful commits, checked/merged PR, code/output saved in Learn and verified instructor access.
- Local Git: tool checks, actual clone, branch/diff, checked commit, successful push, online review, local `main` update and access confirmation from the intended instructor.

You should be able to explain where your code is stored and which version was reviewed. Your actual results are the evidence; an installer icon, pending invitation or local-only push rehearsal is not a completed account check.

### Practice evidence

Submit a brief completion note for your chosen route with the relevant sanitized outputs/links and one issue you solved. If a step is blocked, identify it and request help instead of marking it complete.

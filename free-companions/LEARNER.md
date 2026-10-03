# GitHub and local setup — learner guide

Version October 4, 2026. Follow the route your course requires. GitHub and local Python remain optional for browser-first Fundamentals. Rails uses its separate Ruby setup bridge. No fresh OS or account walkthrough has been verified yet; stop at a setup error and send staff the exact error without credentials.

## G0 — Git, GitHub and a reviewable version


“Git records versions of files on your computer. GitHub can host a copy and a change for someone to review. A commit is a saved version with a short explanation. A branch lets us propose work separately. A pull request shows a proposed change and its checks. The browser route teaches those ideas without installation. The local route also teaches clone, diff, commit, push and update. Python Fundamentals can be completed entirely in Hafa and Learn. Agent Workflows needs real local Git, because reviewing an agent's changes means inspecting actual files and diffs. Keep passwords, API keys and private client data out of every practice file.”

## G1 — account and first repository (browser route)


“Choose a repository named csg-github-practice. Use public only for fictional practice code you are comfortable sharing. A private repository needs an explicit access invitation before an instructor can read it. Add a README so the repository already has an initial commit. Keep the default branch named main for this practice. Create the repository, then add a file named hello dot py. Enter this exact line.”

```python
print("Hafa adai, CSG!")
```

“The file name tells us this is Python. A commit message says what changed. This web editor stores the file; it does not prove Python ran. Paste the line into Hafa and run it. The output should be Hafa adai, CSG, with an exclamation mark. Pause and make your own repository and first program before continuing.”

**Evidence:** README, exact file and commit exist; Hafa greeting runs. **Recovery narration:** “If the file has a dot-txt ending, rename it to hello dot py. If output differs, compare the quotation marks and characters. An account verification screen must be completed before this exercise; it is not a code error.”

## G2 — read a diff and save a second change


```python
print("I can explain one saved change.")
```

“The new line adds a message. Open the preview or diff before committing. Added lines are marked as additions; removed lines are marked as removals. Read what actually changed, not only the commit message. Run both lines in Hafa. You should see Hafa adai, CSG, then I can explain one saved change. Commit with Add explanation message. Open the history and find the earlier version. Pause and add a third message in your own words, check it, and save it as a new commit.”

**Recovery narration:** “If you edited the wrong file, leave that proposed change uncommitted, reopen hello dot py and make the intended change there. Check the file and branch before saving.”

## G3 — branch, pull request and review


“Check the branch name first. My goal sentence is on add-practice-goal, not yet on main. Create a pull request titled Add practice goal. In the description, write: Added one practice goal to README. Checked the diff and confirmed hello dot py is unchanged. Open Files changed. I expect one README addition and no unrelated file. For this disposable practice repository, I can review and merge my own change. In a real team I follow its review rules. Pause, propose your own goal and inspect its diff before merging.”

**Recovery narration:** “If the target branch or file is wrong, correct it before merging. If the diff includes a password or private data, stop and tell the instructor; deleting it in a later commit does not erase earlier history.”

## G4 — submit and verify access


“Paste the repository URL, pull-request URL, the code being reviewed, and the output from your run. The pasted code preserves your review version. Public links should open in a signed-out browser. For a private repository, open repository Settings and its collaborator-access section. Invite only the exact instructor GitHub username supplied for your enrollment, then wait until the instructor accepts. A pending invitation or a copied URL does not prove access. Staff will check it from their own account. On a personal private repository, collaborator access includes write access; invite only the intended instructor and only to this disposable practice repository. A link that cannot be opened is not a completed submission. Never make private work public merely to get past an access error.”

**Access sources:** [Repository collaborators](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository), [GitHub authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github). If a current UI moved, follow the official documentation and record the new label, rather than claiming the old button exists.

## S0 — choose browser or local setup

“If you are starting Python Fundamentals, you can keep using Hafa. These local steps are optional. Choose them when a course needs local files, packages or a real Git repository. Pick Mac or Windows with WSL. A work or school computer may block installation. Ask its administrator or use an approved personal computer; do not bypass its controls. Keep Python practice data fictional. We will check the working folder, run a file and save a local change before connecting to GitHub.”

## M1 — macOS Python and editor


```sh
python3 --version
git --version
```

“These commands report installed versions. If Python is missing or is an unsupported Apple-managed copy, open the official Python macOS installer page. Read its supported-system requirements, download the signed package and install with the permission of the computer's owner. Use its normal supported build. Follow the Python installation page's certificate-completion step in the installed Python Applications folder. Do not delete Apple's Python. If Git is missing, run xcode-select dash-dash install and finish Apple's command-line-tools dialog. That is not a requirement to download full Xcode. Open a new terminal and repeat the version checks.”

```sh
xcode-select --install
```

```sh
mkdir -p ~/csg-practice
cd ~/csg-practice
pwd
```

“Mkdir creates a dedicated practice folder; dash-p allows an existing folder. Cd moves into it. Pwd reports the folder I am using. Open this same folder with the editor's Open Folder command. Create hello dot py with the greeting from G1, and save it. Do not save a rich-text document or hello dot py dot txt.”

```sh
python3 hello.py
```

**Expected:** `Hafa adai, CSG!`

“I ran a file, not just an editor window. Change only the greeting to Hafa adai from my Mac, save, and run again. Pause and repeat both runs. If Python cannot find the file, check pwd and ls first; installing Python again will not fix being in the wrong folder.”

## M2 — local Git identity and first commit


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

“Init creates Git history here. The name and email shown are fictional demo values. Use your chosen commit name and the address or GitHub no-reply address you intend to attach to your own commits. These repository-local settings do not replace your identity in other projects. The short status first shows hello dot py as untracked. Add chooses that one file. Cached diff shows exactly what is staged for the next commit. Read it, then commit. A clean short status prints no file entries. Log shows one commit; its hash will differ on your computer.”

**Pause:** Learner records one commit hash and explains untracked versus staged versus committed. **Recovery:** “If Git says who you are is unknown, set the local name and email and retry commit. If the staged diff has an unintended file, use git restore dash-dash staged followed by that file name. That removes it from the proposed commit while keeping the file.”

## W1 — Windows 11 and Ubuntu WSL


```powershell
wsl --list --verbose
wsl --install -d Ubuntu
```

“The list command shows existing Linux distributions. If Ubuntu already exists, open it rather than reinstall it. If it does not, the install command requests Ubuntu. Follow Microsoft's current supported Windows requirements and restart if asked. Open Ubuntu and create its Linux user. The password prompt does not show the characters you type. Do that off camera. Do not run later Linux commands in PowerShell.”

## W2 — Linux Python, Git and editor in one environment


```sh
sudo apt update
sudo apt install python3 python3-venv git openssh-client
python3 --version
git --version
mkdir -p ~/csg-practice
cd ~/csg-practice
pwd
```

“These commands run inside Ubuntu. Apt updates package information, then installs the named tools. Sudo may ask for your Linux password; no characters appearing is normal. Use the package source approved for this computer. Keep the project in the Linux home folder for this route. Windows and Ubuntu have different runtimes and paths.”

```sh
code .
```

“Code dot opens this Linux folder in the editor's WSL connection. Check that the window shows the WSL environment. Create hello dot py with the G1 greeting, save, then run python-three hello dot py in the WSL terminal. Output should be Hafa adai, CSG. If code dot is missing, open the installed Windows editor and use its WSL connection command, then open this Linux folder. Do not fix that editor command by installing an unrelated Linux editor package.”

“We now repeat the local init, identity, add, staged diff, commit and log checks from M2 in this WSL folder. Pause and show the greeting output, one commit and a clean status. The proof is the actual run and history, not merely installed icons.”

## G5 — authenticate local Git without copying secrets

**Prerequisite:** M1/M2 or W1/W2; G1 GitHub account/repository. **Chosen capture route:** SSH. Learners already using a working approved HTTPS credential manager may retain it; do not replace existing access merely for this exercise. [GitHub SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), [add public key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account), [test connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection), [current host fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints).

```sh
mkdir -p ~/.ssh
ls ~/.ssh/csg_practice_ed25519 ~/.ssh/csg_practice_ed25519.pub
```

“First check whether either half of our specifically named practice key already exists. If either exists, reuse or repair that named key with your instructor's help; do not overwrite it. Create a key only when both files are absent. The dot-pub file is the public half we can register. The file without dot-pub is private and stays on this computer. A passphrase protects that private file. Enter it off camera.”

```sh
ssh-keygen -t ed25519 -C "CSG practice" -f ~/.ssh/csg_practice_ed25519
cat ~/.ssh/csg_practice_ed25519.pub
```

“Copy only the public line into your account's authentication keys. This grants the corresponding private key access as your account. It does not grant an instructor access to your private repositories. Those are different permissions. Now test the named identity.”

```sh
ssh -i ~/.ssh/csg_practice_ed25519 -o IdentitiesOnly=yes -T git@github.com
```

“At a first connection, compare the offered host fingerprint with GitHub's official current fingerprint page before accepting it. A successful test says that the named account authenticated but shell access is not provided. GitHub may return status one for this successful no-shell test; read the authentication message. Permission denied means we have not passed this gate. Check the registered public key, selected private file and account. Never paste a private key or password into Learn. This route asks for a passphrase when needed; it does not start a background SSH agent.”

## G6 — clone, edit, branch, diff, commit and push


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

“Clone creates a new local copy with its Git history and an origin pointing to the repository. We keep it separate from our earlier init practice. This clone command selects our named SSH identity; the local config keeps that selection for later pushes. Use your own chosen commit identity. Remote shows the repository address; verify it is your practice repository. Switch dash-c creates a branch. Do not run git init again inside this clone. If the destination already exists, reopen the known clone or choose a new disposable folder; do not delete unknown work.”

```python
print("A local change I checked myself.")
```

```sh
python3 hello.py
git diff
git add hello.py
git diff --cached
git commit -m "Add checked local message"
git push -u origin add-local-message
```

“Save and run before committing. The earlier messages remain, and the last output is A local change I checked myself. Diff shows the unstaged file change. Add stages hello dot py; cached diff shows what the commit includes. Commit saves it locally. Push uploads this branch to origin and dash-u remembers its upstream. A successful local commit alone does not prove GitHub received it. Open the repository online and confirm the branch, commit and exact line. Open a pull request targeting main and write which command you ran and what output you saw.”

**Recovery narration:** “If push fails, stop and read the message. For authentication, repeat G5. For a wrong remote, compare its address with the correct Code URL before changing it. For a rejected shared-branch push, do not force-push; fetch and ask for help. Keep your local commit intact while resolving the problem.”

## G7 — review, update and access proof

```sh
git switch main
git pull --ff-only origin main
python3 hello.py
git log --oneline -3
git status --short
```

“The online merge does not automatically update this local folder. Switch to main, then pull dash-dash ff-only. This accepts a straightforward history update and stops if histories diverged; it will not silently make an extra merge. Run the program again and confirm the new line exists on main. Record your commit, PR link and output in Learn. A private repository still needs accepted instructor access. For Agent Workflows, the local clone, branch, visible diff, checked commit, successful push and update are prerequisites. A browser-only edit does not satisfy that local gate.”

**Recovery narration:** “If switch says local changes would be overwritten, leave them in place and commit the intended work on its branch or ask for help. Do not use a hard reset to make the warning disappear. If pull cannot fast-forward, preserve the folder and get a review of the two histories.”

## S1 — troubleshooting and completion evidence

“When a command is missing, confirm which terminal you opened and the exact spelling. When a file is missing, check pwd and ls. When a run differs, compare the saved file with the output. When an installer asks for permission, read which publisher and component it concerns. In Learn, send your operating system, the command, non-sensitive output and one issue you solved. Keep account names, home paths, private keys and recovery codes out of public screenshots.”

**Optional Python completion:** one local greeting run or the already sufficient Hafa run, no account required. **GitHub web completion:** repository, meaningful commits, checked PR, saved Learn evidence and verified access. **Local Git completion:** version checks, real clone, local branch and diff, commit, push, online PR, local main update and distinct-profile access check. The learner can explain where code is stored and which version was reviewed.


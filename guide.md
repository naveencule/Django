# 🚀 GitHub Collaboration Guide 

This guide explains step by step how we  should work with **branches, commits, and pull requests** to avoid issues.  
**Main rule** → Never work directly on `main`.

---

## 1. Clone the Repository
Do this once when you first join the project.
```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name


2. Create the Dev Branch (one time only)

Only one team member needs to do this at the start.

git checkout -b dev
git push origin dev


👉 checkout -b dev creates a new branch called dev and switches to it.
👉 push origin dev uploads the dev branch to GitHub.

3. Starting a New Feature (each time you work)

First, update your local dev branch:

git checkout dev
git pull origin dev


👉 checkout dev switches to the dev branch.
👉 pull origin dev gets the latest changes from GitHub.

Now, create a new feature branch:

git checkout -b feature/your-feature-name


👉 This creates a new branch for your work so you don’t affect others.
👉 Example: feature/login-page, feature/dashboard.


4. Make Your Changes

After editing code, save and run:

git add .
git commit -m "Added login page UI"


👉 add . stages all changes you made.
👉 commit -m saves your work with a message describing what you did.

5. Push Your Feature Branch

Send your work to GitHub:

git push origin feature/your-feature-name


👉 This uploads your branch to GitHub so your teammate can see it.

6. Open a Pull Request (PR)

Go to the repo on GitHub.

You’ll see a button “Compare & Pull Request”.

Set base: dev, compare: feature/your-feature-name.

Write what you changed and submit PR.

👉 A Pull Request is a way of asking to merge your branch into dev.

7. Merge into Dev

Your teammate reviews your code.

If okay, merge the PR into dev.

👉 Now everyone can pull the updated dev.

8. Update Your Local Dev

Before starting new work, always run:

git checkout dev
git pull origin dev


👉 Keeps your local dev updated with teammate’s changes.

9. Merge Dev → Main (Final Release)

Only when features are stable and tested:

git checkout main
git pull origin main
git merge dev
git push origin main


👉 This updates the main branch with all completed work.
👉 main should always stay stable and clean.
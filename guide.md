Day 1: Start of Work
1️⃣ Update local dev

Both you and your teammate:

git checkout dev
git pull origin dev


Ensures you both start from the latest shared code.

2️⃣ Create your feature branches

You:

git checkout -b feature/login-page


Teammate:

git checkout -b feature/dashboard


Each of you now works in your own branch — changes are isolated.

Day 2: Working & Committing

After coding your feature:

You:

git add .
git commit -m "Added login form UI"
git push origin feature/login-page


Teammate:

git add .
git commit -m "Created dashboard layout"
git push origin feature/dashboard


Your branches are now on GitHub, ready to merge into dev.

Day 3: Merge Feature Branches into Dev

You:

git checkout dev
git pull origin dev           # get latest dev
git merge feature/login-page  # merge your feature
git push origin dev           # push updated dev


Teammate:

git checkout dev
git pull origin dev           # fetch latest dev including your login-page
git merge feature/dashboard   # merge dashboard feature
git push origin dev


Now dev has both features.

Day 4: Start New Features (Optional)

Before starting a new feature:

git checkout dev
git pull origin dev
git checkout -b feature/new-feature


Always branch off latest dev.

Final Step: Merge Dev → Main

You (repo owner, final release):

git checkout main
git pull origin main
git merge dev
git push origin main


main now has all tested features. Team members never merge into main directly.

✅ Rules Summary

Never code directly in dev or main. Always use feature branches.

Always pull before push to avoid conflicts.

Merge feature → dev either via PR or command line.

Only repo owner merges dev → main.

Communicate which feature you’re working on to avoid overlap.
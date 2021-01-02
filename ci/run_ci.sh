#!/bin/bash
set -e

##
## Runs CI
##

# get into the parent folder
cd /home
# configure git in case we want to push stuff in the future
git config --global user.name ${GITHUB_ACTOR}
git config --global user.email ${GITHUB_ACTOR}@users.noreply.github.com
# clone in Peeves for Unit testing
#git clone https://github.com/McCoyGroup/Peeves.git
## run the testing script
cd /home
PYTHONPATH=/home python3 Peeves/ci/tests/run_tests.py -v -d

# switch to the gh-pages branch and merge in changes from master
cd Peeves
git checkout gh-pages
git merge master
cd ..

# build docs and push
PYTHONPATH=/home python3 Peeves/ci/build_docs.py
cd Peeves
git config --global user.name ${GITHUB_ACTOR}
git config --global user.email ${GITHUB_ACTOR}@users.noreply.github.com
git add -A && git commit -m "Built out docs"
git push "https://github.com/McCoyGroup/Peeves.git" gh-pages
#!/bin/bash
set -e

##
## Runs CI
##

# get into the parent folder and merge in changes from the master branch
# since we're running on the gh-pages branch
cd /home/Peeves
git merge master
## run the test script
cd /home
PYTHONPATH=/home python3 Peeves/ci/tests/run_tests.py -v -d

# build docs and push
PYTHONPATH=/home python3 Peeves/ci/build_docs.py
cd Peeves
git config user.name ${GITHUB_ACTOR}
git config user.email ${GITHUB_ACTOR}@users.noreply.github.com
git add -A && git commit -m "Built out docs"
echo "${GITHUB_ACTOR} ${#GITHUB_TOKEN}"
git push "https://$GITHUB_ACTOR:$GITHUB_TOKEN@github.com/McCoyGroup/Peeves.git"
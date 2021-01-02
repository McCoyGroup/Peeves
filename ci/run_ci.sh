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

cd Peeves
git checkout gh-pages
cd ..
## write some artifacts, maybe, in the future (e.g. generated data from data_gen tests or images from matplotlib)
PYTHONPATH=/home python3 Peeves/ci/build_docs.py
cd Peeves
git add -A && git commit -m "Built out site"
git push -u origin HEAD
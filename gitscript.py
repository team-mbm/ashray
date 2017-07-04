#!/usr/bin/python

import sys

git add .
git commit -m str(sys.arg[1])
git checkout master
git pull origin master
git checkout str(sys.arg[2])
git merge master
git push origin str(sys.arg[2])

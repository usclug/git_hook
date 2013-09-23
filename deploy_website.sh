#!/bin/bash

WEBSITE_REPO=/home/www/usclug.deterlab.net/public_html
LOG_FILE=/home/www/usclug.deterlab.net/logs/git.log
SCRIPT_TIMESTAMP=$(date +%Y-%m-%d_%H%M%S)

#Access Repo and make up to date
cd $WEBSITE_REPO
git checkout --quiet gh-pages
git pull --quiet
GIT_LAST_COMMENT=$(git log -1 --format="commit %h by %aN on %ad")

echo "Update @ $SCRIPT_TIMESTAMP with $GIT_LAST_COMMENT" >> $LOG_FILE

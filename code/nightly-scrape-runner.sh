# !/bin/bash
PROJECT_DIR=~/dds-analysis
cd $PROJECT_DIR

# like, do the effing scrape!
python code/menu-scraper.py

# check them in, bro!
git add data/*
git commit -a -q -m "AUTO COMMIT: slurped some data!"
git push --quiet




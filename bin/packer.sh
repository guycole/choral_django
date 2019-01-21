#!/bin/bash
#
# Title: packer.sh
# Description: portable django mover
#
cd ..
tar -cvzf choral.tgz bin postgres terraform choral/.ebextensions choral/.elasticbeanstalk choral/db.sqlite3 choral/audio choral/choral choral/manage.py choral/requirements.txt choral/sight choral/static
#

import os
import sys

# Figure out way to dynamically get virtualenv
sys.path.append("/home/chris/.virtualenvs/hs/lib/python2.7/site-packages")
sys.path.append("/home/chris/www")


bind = "127.0.0.1:29992"
logfile = "/home/chris/www/hs/logs/gunicorn.log"
workers = 3

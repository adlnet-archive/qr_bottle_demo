import os
import sys
from fabric.api import local,run

def setup_env():
    INSTALL_STEPS = ['virtualenv ../qrenv;. ../qrenv/bin/activate;pip install -r requirements.txt;deactivate']
    for step in INSTALL_STEPS:
        local(step)
	cwd = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(cwd, 'static')):
    	os.makedirs(os.path.join(cwd, 'static'))
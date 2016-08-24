import os
import re

CONF_RE = re.compile(r'^scripts_list\s*=\s*(.*?)$', flags=re.IGNORECASE)

ICON = 'terminal.svg'
HERE = os.path.abspath(os.path.dirname(__file__))
ICON_PATH = os.path.join(HERE, 'icons', ICON)
START_DIR = '.scripts_list'

USER_HOME = os.path.expanduser('~')
CONFIG = os.path.join(USER_HOME, '.preferably')

if os.path.exists(CONFIG):
    with open(CONFIG, 'r') as f:
        conf = f.read()
    if CONF_RE.match(conf):
        START_DIR = os.path.expanduser(CONF_RE.findall(conf)[0])

TOP_DIR = os.path.join(USER_HOME, START_DIR)

if not os.path.exists(TOP_DIR):
    os.mkdir(TOP_DIR)

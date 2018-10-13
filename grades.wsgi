import sys, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/hha-grades/')

activate = '/var/www/hha-grades/venv/bin/activate_this.py'
execfile(activate, dict(__file__=activate))

from app import app as application

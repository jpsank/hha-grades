import sys, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/hha-grades/')

from app import app as application

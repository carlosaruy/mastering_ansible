activate_this = '/var/www/demo/.venv/bin/activate_this.py'
exec(compile(open(activate_this).read(), activate_this, 'exec'), dict(__file__=activate_this))
#execfile(activate_this, dict(__file__=activate_this))
import os
os.environ['DATABASE_URI'] = 'mysql+pymysql://demo:demo@db01/demo'

import sys
sys.path.insert(0, '/var/www/demo/html')

from demo import app as application

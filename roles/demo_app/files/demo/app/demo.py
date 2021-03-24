from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import sys, traceback

import os, socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)
hostname = socket.gethostname()

@app.route('/')
def index():
  return 'Hello, from sunny %s!\n' % hostname

@app.route('/db')
def dbtest():
  try:
      print('aca estoy escribiendo a ver donde sale')
      db.create_all()
  except Exception as e:
      #corregido en vez de e.message, se devuelve str(e)

      return  os.environ['DATABASE_URI'] + '++'+ app.config['SQLALCHEMY_DATABASE_URI'] + str(e) + '|||| '+  traceback.format_exc() + '\n'
  return 'Database Connected from %s!\n' % hostname

if __name__ == '__main__':
  app.run()

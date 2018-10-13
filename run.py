# WSGI Server for Development
# Use this during development vs. apache.
# Run using virtualenv. 'venv/bin/python run.py'
from app import app

app.run(host='0.0.0.0', port=8000, debug=True)

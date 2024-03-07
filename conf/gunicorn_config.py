from dotenv import load_dotenv
import os


load_dotenv()

# command = '/home/kpavlov/projects/python-project-52/.venv/bin/gunicorn'
# pythonpath = '/home/kpavlov/projects/python-project-52/.venv/bin/python'
# bind = '62.113.97.17:8000'
# workers = 5

bind = '127.0.0.1:8000'
workers = 5
user = os.getenv('user_name')
timeout = 120

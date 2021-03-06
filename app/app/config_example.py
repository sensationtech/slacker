import os

SECRET_KEY = 'please put something random'

SLACK_CLIENT_ID = os.environ.get('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.environ.get('SLACK_CLIENT_SECRET')

SENTIMENT_KEY = 'GET FROM http://sentigem.com/'

#This you should not need to modify
SLACK_SCOPE = 'users:read,users:read.email,channels:read,channels:history,dnd:read,emoji:read,' \
              'files:read,pins:read,reactions:read,' \
              'reminders:read,search:read,stars:read,team:read'
#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "36905571"))
API_HASH = environ.get("API_HASH", "36677bbab05f148b95f91b13dbc57ea1")
BOT_TOKEN = environ.get("BOT_TOKEN", "8535953469:AAGcWlCldBaNZntCJB7XZN-rLiHbEWRLFyI")

OWNER = int(environ.get("OWNER", "8204831161"))
CREDIT = environ.get("CREDIT", "")

TOTAL_USER = os.environ.get('TOTAL_USERS', '').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8204831161').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


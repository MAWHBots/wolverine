import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', "5324831370").split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS',).split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5324831370').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP', "-1002239809844")
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
SUPPORT_CHANNEL = environ.get('CHANNEL_USERNAME')
SUPPORT_GROUP = environ.get('GROUP_USERNAME')
INDEX_USER = [int(environ.get('INDEX_USER', '1247742004'))]
INDEX_USER.extend(ADMINS)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI')
DATABASE_NAME = environ.get('DATABASE_NAME', "wolve")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'wolve')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL'))
FORCESUB_CHANNEL = int(environ.get('FORCESUB_CHANNEL'))
SLOW_MODE_DELAY = int(environ.get('SLOW_MODE_DELAY', 60))
WAIT_TIME = int(environ.get('AUTO_DELETE_WAIT_TIME', 1800))
FORWARD_CHANNEL = int(environ.get('FORWARD_CHANNEL', "-1002029611411"))

# other
ACCESS_KEY = environ.get("LICENSE_ACCESS_KEY")
BIN_CHANNEL = environ.get("BIN_CHANNEL")
URL = environ.get("STREAM_URL")
SHORTNER_SITE = environ.get("SHORTNER_SITE")
SHORTNER_API = environ.get("SHORTNER_API")

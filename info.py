import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '761686219 1875429051 1369291772').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001614484361 -1001641612683').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = -1001702519740
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', '')

# Messages
default_start_msg = """
**𝖧𝗂, 𝖨'𝗆 𝖬𝖾𝖽𝗂𝖺 𝖲𝖾𝖺𝗋𝖼𝗁 𝖻𝗈𝗍**

𝖧𝖾𝗋𝖾 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝖾𝖺𝗋𝖼𝗁 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗂𝗇𝗅𝗂𝗇𝖾 𝗆𝗈𝖽𝖾. 𝖩𝗎𝗌𝗍 𝗉𝗋𝖾𝗌𝗌 𝖿𝗈𝗅𝗅𝗈𝗐𝗂𝗇𝗀 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝖺𝗇𝖽 𝗌𝗍𝖺𝗋𝗍 𝗌𝖾𝖺𝗋𝖼𝗁𝗂𝗇𝗀.

🙋🏻‍♂️ 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅 𝖦𝗎𝗂𝖽𝖾 @piro_tuts

😎 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 @rai_info17
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please Join My Updates Channel to use this Bot!')
# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "24401235"))
	API_HASH = os.environ.get("API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6491531689:AAEaGLAeJqSAOWbPvxik3vsXETSi3PNMxFQ")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Tessa_Ro_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002159448886"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "gplinks.com")
	SHORTLINK_API = os.environ.get('SHORTLINK_API', "f3f3680462d49cc38791e7d6fd44dc02d5b2a97e")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1556830659"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://avianandh004:TeamHdt009@cluster0.hdvf3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002260410306")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002414067137")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Team_HDT](https://t.me/Team_HDT) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/Team_HDT)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/Team_HDT)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@Team_HDT](https://t.me/Team_HDT)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Team_HDT)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""

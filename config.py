# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25475508"))
API_HASH = getenv("API_HASH", "22a9a96bbb571455c4b4f4e8244c1b58")
BOT_TOKEN = getenv("BOT_TOKEN", "7643677854:AAFgcQdIz6LYd1zFRVqcPxXMJX5jGoTuQQc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5795114320").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://thecrazyhackerrraj:ruplalghunawat@cluster0.gk7qh8r.mongodb.net/")
LOG_GROUP = getenv("LOG_GROUP", "-4777940358")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002550908781"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "bloggerbyte.net")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

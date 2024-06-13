
import json
import os


def get_user_list(config, key):
    with open("{}/Am/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True

    API_ID = "24295926"
    API_HASH = "bb6493ae35ec2bcea928c0a38584ca2e"
    TOKEN = ""
    OWNER_ID = ""
    OWNER_USERNAME = ""
    UPDATES = ""
    BOT_USERNAME = ""
    SUPPORT_CHAT = "DANGEROUS_FIGHTER_GROUP"
    JOIN_LOGGER = "-1002077359484"
    EVENT_LOGS = "-1002077359484"
    BOT_USERNAME = ""
    BOT_NAME = ""
    GBANS = "prishuxs" 
    CHAT_GROUP = ""
    # 
    # DATABASE_URL = "postgres://ixweewbx:9OoB_feF6d6wK1W4YycgwHzRHQXezsNA@arjuna.db.elephantsql.com/ixweewbx"  # sql
    DATABASE_URL = ""  # sql
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    REDIS_URL = "redis://default:725m47dhlmisA0QecURSMkcHNGXkM1uP@redis-15808.c275.us-east-1-4.ec2.cloud.redislabs.com:15808"

    INSPECTOR = get_user_list("elevated_users.json", "ins")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "req")

    CERT_PATH = None
    STRICT_GBAN = True
    PORT = "8080"
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 20
    ALLOW_EXCL = True
    ALLOW_CHATS = True
    PHOTO = "https://te.legra.ph/file/17d19061f86cb1ebbddec.jpg" # Miss Poppy Music Pic
    INFOPIC = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

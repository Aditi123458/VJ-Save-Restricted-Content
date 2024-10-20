import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22555631"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fa01340f331aa1bfa112d863ade8a142")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vermaaditi708:WMGYHyX1bk2Yx8TW@cluster0.rj8ln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

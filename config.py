import os
import motor.motor_asyncio

DOMAIN = os.getenv("DOMAIN")

# MongoDB connection
MONGODB_NAME = "quickly" 
MONGODB_COL = "quickly" 
MONGODB_URL = os.getenv("MONGODB_URL")
mongoClient =  motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
mongodb = mongoClient[MONGODB_NAME][MONGODB_COL]
MONGODB_NAME2 = "quicklyAuth" 
MONGODB_COL2 = "quicklyAuth" 
MONGODB_URL2 = os.getenv("MONGODB_URL2")   
mongoAuthClient =  motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
authdb = mongoClient[MONGODB_NAME2][MONGODB_COL2]

# Идентификатор чата
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
CHAT_ID = str(os.getenv("CHAT_ID"))

# JWT
SECRET_KEY = str(os.getenv("SECRET_KEY"))
SALT = str(os.getenv("SALT"))

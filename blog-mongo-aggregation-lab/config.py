import os

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://USUARIO:SENHA@cluster.mongodb.net/blog_db"
)

DB_NAME = "blog_db"

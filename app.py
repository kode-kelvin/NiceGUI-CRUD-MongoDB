from nicegui import ui
from pydantic import BaseModel
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
from dotenv import load_dotenv
import os


# format _id --
def default(item):
    if isinstance(item, ObjectId):
        return str(item)
# end _id --


# connect to our Database and settings (credentials) / get .env variables ---
load_dotenv()
hidden_key = os.getenv("SECRET_KEY")
user_name = os.getenv('DB_USER_NAME')
user_password = os.getenv('DB_PASSWORD')
client = pymongo.MongoClient(
    f"mongodb+srv://{user_name}:{user_password}@kobo.k0upp8i.mongodb.net/")
db = client.nicegui
tododb = db.todo
# end connect


# Create pydantic Models -- --
class Todo(BaseModel):  # create todo
    d_todo: str
    due_date: datetime | None
    created: datetime = datetime.utcnow()


class UpdateTodo(Todo):  # update  todo
    d_todo: str
# End models


"""Run the app"""
ui.run(title='Todoly', favicon="📋", host='0.0.0.0', port=8008)

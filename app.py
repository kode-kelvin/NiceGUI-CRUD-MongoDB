
from nicegui import ui, app
from pydantic import BaseModel
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
from dotenv import load_dotenv
import os
from typing import List
import uuid


def default(item):  # format _id --
    if isinstance(item, ObjectId):
        return str(item)


# GETTING CURRENT DATE FOR FLAG
current_date = datetime.now().strftime('%Y-%m-%d')


load_dotenv()  # connect to our Database and settings (credentials) / get .env variables --
hidden_key = os.getenv("SECRET_KEY")
user_name = os.getenv('DB_USER_NAME')
user_password = os.getenv('DB_PASSWORD')
client = pymongo.MongoClient(
    f"mongodb+srv://{user_name}:{user_password}@kobo.k0upp8i.mongodb.net/")
db = client.nicegui
tododb = db.todo


# model create todo ------ ------ -----
class Todo(BaseModel):
    todo_id: str = str(uuid.uuid4())
    d_todo: str
    due_date: str
    created: datetime = datetime.utcnow()


# model update todo ------ ------ -----
class UpdateTodo(Todo):
    d_todo: str
    due_date: str


# ADD THE NEW DATA ------ ------ -----
def addnewdata():
    try:
        data = {
            'd_todo': todo.value,
            'due_date': date.value
        }
        new_todo = Todo(**data)
        tododb.insert_one(new_todo.model_dump())
        ui.notify('Todo added', color='blue')

        # clear the input field
        todo.value = ""
        date.value = ""

        # clear the list and add again
        list_alldata.clear()
        get_all_data()
    except Exception as e:
        print(e)


# DISPLAY YHE DATA ------ ------ -----
content = ui.column().classes('w-full md:w-3/4 sm:w-full').style("""
        margin: auto;
    """)
with content:
    # NEW TODOX DATA
    todo = ui.input(
        'Enter todo', placeholder='start typing', validation={'Todo too short ': lambda value: len(value) > 5}).props('outlined').classes('w-full')
    due_date_input = ui.input('Due date').classes('w-full')
    with due_date_input as date:
        with date.add_slot('append'):
            ui.icon('edit_calendar').on(
                'click', lambda: menu.open()).classes('cursor-pointer')
        with ui.menu() as menu:
            ui.date().bind_value(date)
    create_button = ui.button(
        'Create todo', on_click=addnewdata).classes('w-full')


# CONTAINER FOR PAGE ------ ------ -----
list_alldata = ui.column().classes('w-full md:w-3/4 sm:w-full').style("""
        margin: auto;
    """)  # CONTAINER WITH STYLES FOR TODOS LIST


# DELETE TODOS ------ ------ -----
def remove_todo(todo_id):
    tododb.delete_one({'todo_id': todo_id})
    ui.notify('Todo deleted', color='green')
    list_alldata.clear()
    get_all_data()


# UPDATE TODOS ------ ------ -----
def update_todo(todo_id):  # UPDATE TODOS
    todo_data = tododb.find_one({'todo_id': todo_id})
    prev_todo = Todo(**todo_data)

    with ui.dialog() as dialog, ui.card().classes('w-full'):
        ui.label('Update Todo')
        todor = ui.input(
            'Enter todo', placeholder='start typing', validation={'Todo too short ': lambda value: len(value) > 5}).props('outlined').classes('w-full')
        due_date_input = ui.input('Due date').classes('w-full')
        with due_date_input as dater:
            with dater.add_slot('append'):
                ui.icon('edit_calendar').on(
                    'click', lambda: menu.open()).classes('cursor-pointer')
            with ui.menu() as menu:
                ui.date().bind_value(dater)

        todor.value = prev_todo.d_todo
        dater.value = prev_todo.due_date

        def update_todo_new():
            try:
                data = {
                    'd_todo': todor.value,
                    'due_date': dater.value
                }
                tododb.update_one({'todo_id': todo_id}, {"$set": data})
                ui.notify('Todo updated', color='blue')

                # rest interface
                list_alldata.clear()
                get_all_data()

            except Exception as e:
                print(e)

        create_button = ui.button(
            'Update todo', on_click=update_todo_new).classes('w-full')

        ui.button('Close', on_click=dialog.close)
        dialog.open()


# GET TODOS LIST FROM DATABASE ------ ------ -----
def get_all_data() -> List[Todo]:  # GET todos from db
    todos = tododb.find().sort("due_date", pymongo.ASCENDING)
    todo_list = []
    for todo_data in todos:
        todo_model = Todo(**todo_data)
        todo_list.append(todo_model)

    # DISPLAY ADDED TODOs
    for todo in todo_list:
        with list_alldata:

            # delete button and edit
            with ui.row().classes(' flex items-center w-full'):
                ui.button(icon='edit', on_click=lambda t=todo.todo_id: update_todo(
                    t)).props(" outline size=9px").style('width:9px')
                todo_checkbox = ui.checkbox(
                    f'{todo.d_todo}', on_change=lambda t=todo.todo_id: remove_todo(t))
                todo_dealine = todo.due_date
                if todo_dealine == current_date:
                    ui.html(f'{todo.due_date}').classes(
                        'ml-auto').style('color: #A20021')
                else:
                    ui.html(f'{todo.due_date}').classes(
                        'ml-auto').style('color: grey')
                ui.separator()


# CALL / SHOW TODOS ------ ------ -----
get_all_data()

ui.run(title='Todoly', favicon="📋", host='0.0.0.0', port=8020)

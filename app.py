import os
from datetime import datetime

from bson.objectid import ObjectId
from dotenv import load_dotenv
from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"), server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("error van")
    print(e)

db = client.tododb
todos = db.todos

@app.route("/")
def index():
    """Főoldal: minden todo listázása, legúbjabb elöl"""
    all_todos = list(todos.find().sort("created_at", -1))
    return render_template("index.html", todos = all_todos)

@app.route("/add", methods=["POST"])
def add():
    """Új todo hozzáadása"""
    task = request.form.get("task", "").strip()
    if task:
        todos.insert_one({
            "task": task,
            "done": False,
            "created_at": datetime.utcnow()
        })
    return redirect(url_for("index"))


@app.route("/complete/<todo_id>", methods=["GET"])
def complete(todo_id):
    """Tdo bejezése"""
    print(todo_id)
    todo = todos.find_one({"_id": ObjectId(todo_id)})
    print(todo["done"])
    if todo:
        todos.update_one(
            {"_id": ObjectId(todo_id)},
            {"$set": {"done": not todo["done"]}}
            )
    return redirect(url_for("index")) 

@app.route("/delete/<todo_id>", methods=["GET"])
def delete(todo_id):
    """Todo törlése"""
    todos.delete_one({"_id": ObjectId(todo_id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
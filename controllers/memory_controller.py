import re
from flask import Flask, Blueprint, render_template, request, redirect
from models.memory import Memory

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository
import repositories.memory_repository as memory_repository


memories_blueprint = Blueprint("memories", __name__)


@memories_blueprint.route("/memories/")
def memories():
    memories = memory_repository.select_all()
    return render_template("memories/index.html", title="Your memories", memories=memories)
    

@memories_blueprint.route("/memories/<id>/")
def show(id):
    memory = memory_repository.select(id)
    memory_title = memory.title
    convert_date = memory.convert_date()
    return render_template("memories/show.html", title=memory_title, memory=memory, convert_date=convert_date)


@memories_blueprint.route("/memories/new/")
def new_memory():
    contributors = contributor_repository.select_all()
    charities = charity_repository.select_all()
    return render_template("memories/new.html", title="Contribute", contributors=contributors, charities=charities)


@memories_blueprint.route("/memories/", methods=['POST'])
def create_memory():
    title = request.form['title']
    contributor_id = request.form['contributor_id']
    story = request.form['story']
    date = request.form['date']
    charity_id = request.form['charity_id']
    contributor = contributor_repository.select(contributor_id)
    charity = charity_repository.select(charity_id)
    memory = Memory(title, contributor, story, date, charity)
    memory_repository.save(memory)
    return redirect("/memories")


@memories_blueprint.route("/memories/<id>/delete/", methods=['POST'])
def delete(id):
    memory_repository.delete(id)
    return redirect("/memories")
from flask import Flask, Blueprint, render_template, request, redirect
from models.contributor import Contributor

import repositories.contributor_repository as contributor_repository


contributors_blueprint = Blueprint("contributor", __name__)


@contributors_blueprint.route("/contributors/")
def contributors():
    contributors = contributor_repository.select_all()
    return render_template("contributors/index.html", title="Our Contributors", contributors=contributors)
    

@contributors_blueprint.route("/contributors/<id>/")
def show(id):
    contributor = contributor_repository.select(id)
    charities = contributor_repository.charities(contributor)
    memories = contributor_repository.memories(contributor)
    contributor_name = contributor.first_name + " " + contributor.last_name
    return render_template("contributors/show.html", title=contributor_name, contributor=contributor, charities=charities, memories=memories)


@contributors_blueprint.route("/contributors/new/")
def new_contributor():
    return render_template("contributors/new.html", title="Create a profile")


@contributors_blueprint.route("/contributors/", methods=['POST'])
def create_contributor():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    profession = request.form['profession']
    address = request.form['address']
    contributor = Contributor(first_name, last_name, age, profession, address)
    contributor_repository.save(contributor)
    return redirect("/contributors")
from flask import Flask, Blueprint, render_template, request, redirect
from models.charity import Charity

import repositories.charity_repository as charity_repository


charities_blueprint = Blueprint("charity", __name__)


@charities_blueprint.route("/charities/")
def charities():
    charities = charity_repository.select_all()
    return render_template("charities/index.html", title="Our Charities", charities=charities)
    

@charities_blueprint.route("/charities/<id>/")
def show(id):
    charity = charity_repository.select(id)
    contributors = charity_repository.contributors(charity)
    count_contributors = len(contributors)
    memories = charity_repository.memories(charity)
    events = charity_repository.events(charity)
    charity_name = charity.name
    return render_template("charities/show.html", title=charity_name, charity=charity, contributors=contributors, count_contributors=count_contributors, memories=memories, events=events)


@charities_blueprint.route("/charities/new/")
def new_charity():
    return render_template("charities/new.html", title="Add A Charity")


@charities_blueprint.route("/charities/", methods=['POST'])
def create_charity():
    name = request.form['name']
    description = request.form['description']
    website = request.form['website']
    charity = Charity(name, description, website)
    charity_repository.save(charity)
    return redirect("/charities")


@charities_blueprint.route("/charities/<id>/delete/", methods=['POST'])
def delete(id):
    charity_repository.delete(id)
    return redirect("/charities")


@charities_blueprint.route("/charities/<id>/edit/", methods=['GET'])
def edit_charity(id):
    charity = charity_repository.select(id)
    return render_template("/charities/edit.html", title="Edit Your Charity", charity=charity)


@charities_blueprint.route("/charities/<id>/", methods=['POST'])
def update_charity(id):
    name = request.form['name']
    description = request.form['description']
    website = request.form['website']
    charity = Charity(name, description, website, id)
    charity_repository.update(charity)
    return redirect("/charities")
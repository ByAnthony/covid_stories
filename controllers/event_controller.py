from flask import Flask, Blueprint, render_template, request, redirect
from models.event import Event

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository
import repositories.event_repository as event_repository


events_blueprint = Blueprint("events", __name__)


@events_blueprint.route("/events/<id>/")
def show(id):
    event = event_repository.select(id)
    event_name = event.name
    return render_template("events/show.html", title=event_name, event=event)


@events_blueprint.route("/events/new/")
def new_event():
    charities = charity_repository.select_all()
    return render_template("events/new.html", title="New Event", charities=charities)


@events_blueprint.route("/events/", methods=['POST'])
def create_event():
    name = request.form['name']
    description = request.form['description']
    charity_id = request.form['charity_id']
    date = request.form['date']
    charity = charity_repository.select(charity_id)
    event = Event(name, description, charity, date)
    event_repository.save(event)
    return redirect("/charities")


@events_blueprint.route("/events/<id>/delete/", methods=['POST'])
def delete(id):
    event_repository.delete(id)
    return redirect("/charities")


@events_blueprint.route("/events/<id>/edit/", methods=['GET'])
def edit_event(id):
    event = event_repository.select(id)
    charities = charity_repository.select_all()
    return render_template("/events/edit.html", title="Edit Your Event", event=event, charities=charities)


@events_blueprint.route("/events/<id>/", methods=['POST'])
def update_event(id):
    name = request.form['name']
    description = request.form['description']
    charity_id = request.form['charity_id']
    date = request.form['date']
    charity = charity_repository.select(charity_id)
    event = Event(name, description, charity, date, id)
    event_repository.update(event)
    return redirect("/charities")
from flask import Flask, Blueprint, render_template, request, redirect
from models.ticket import Ticket

import repositories.ticket_repository as ticket_repository
import repositories.contributor_repository as contributor_repository
import repositories.event_repository as event_repository


tickets_blueprint = Blueprint("tickets", __name__)


@tickets_blueprint.route("/tickets/new/")
def new_ticket():
    events = event_repository.select_all()
    contributors = contributor_repository.select_all()
    return render_template("/tickets/new.html", title="New Booking", events=events, contributors=contributors)


@tickets_blueprint.route("/tickets/", methods=['POST'])
def create_ticket():
    event_id = request.form['event_id']
    contributor_id = request.form['contributor_id']
    event = event_repository.select(event_id)
    contributor = contributor_repository.select(contributor_id)
    ticket = Ticket(event, contributor)
    ticket_repository.save(ticket)
    return redirect("/charities")


@tickets_blueprint.route("/tickets/<id>/delete/", methods=['POST'])
def delete(id):
    ticket_repository.delete(id)
    return redirect("/contributors")
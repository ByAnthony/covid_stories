from flask import Flask, Blueprint, render_template, request, redirect
from models.charity import Charity
import repositories.charity_repository as charity_repository

charities_blueprint = Blueprint("charity", __name__)

@charities_blueprint.route("/charities/")
def charities():
    charities = charity_repository.select_all()
    return render_template("/charities/index.html", title="Support Charities", charities=charities)
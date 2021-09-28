from flask import Flask, render_template
from controllers.charity_controller import charities_blueprint
from controllers.contributor_controller import contributors_blueprint
from controllers.memory_controller import memories_blueprint
from controllers.event_controller import events_blueprint
from controllers.ticket_controller import tickets_blueprint

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository
import repositories.memory_repository as memory_repository
import repositories.event_repository as event_repository


app = Flask(__name__)

app.register_blueprint(charities_blueprint)
app.register_blueprint(contributors_blueprint)
app.register_blueprint(memories_blueprint)
app.register_blueprint(events_blueprint)
app.register_blueprint(tickets_blueprint)


@app.route('/')
def home():
    charities = charity_repository.select_all()
    count_charities = len(charities)
    contributors = contributor_repository.select_all()
    count_contributors = len(contributors)
    memories = memory_repository.select_all()
    count_memories = len(memories)
    return render_template("index.html", title="Share & Support", count_charities=count_charities, count_contributors=count_contributors, count_memories=count_memories)


if __name__ == '__main__':
    app.run(debug=True)
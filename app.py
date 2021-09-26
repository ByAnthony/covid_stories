from flask import Flask, render_template

from controllers.charity_controller import charities_blueprint
from controllers.contributor_controller import contributors_blueprint
from controllers.memory_controller import memories_blueprint

app = Flask(__name__)

app.register_blueprint(charities_blueprint)
app.register_blueprint(contributors_blueprint)
app.register_blueprint(memories_blueprint)

@app.route('/')
def home():
    return render_template("index.html", title="Share & Support")

if __name__ == '__main__':
    app.run(debug=True)
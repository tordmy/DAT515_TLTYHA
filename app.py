from time import sleep
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template #render_template_string

#Wait for the DB container to be ready for connections
sleep(5)

app = Flask(__name__)
# For local registry
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@db-deploy/postgres'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False)
    content = db.Column(db.String(320), unique=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        content = request.form['content']
        message = Message(username=username, content=content)
        db.session.add(message)
        db.session.commit()
    messages = Message.query.all()
    return render_template("index.html", messages=messages)


@app.route('/isready', methods=['GET'])
def ready():
    # Here we can add logic to check if our application is ready to serve requests
    # (e.g., initialization completed, required services started, etc.)
    # For simplicity, we'll just return a static response
    return jsonify({"status": "OK", "message": "Application is ready"}), 200


@app.route('/ishealthy', methods=['GET'])
def healthy():
    # Here we can add logic to check if our application is ready to serve requests
    # (e.g., initialization completed, required services started, etc.)
    # For simplicity, we'll just return a static response
    return jsonify({"status": "OK", "message": "Application is running"}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)

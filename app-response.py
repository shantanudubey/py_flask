from flask import Flask, jsonify, make_response


app = Flask(__name__)


@app.route('/')
def homepage():
    return "<html><body><h1>Flask Response Testing</h1</body></html>"


@app.route('/login/')
@app.route('/login/<id>')
def check(id=None):
    if not id:
        message = jsonify(message = "The id cannot be blank.")
        return make_response(message, 400)
    
    return jsonify(id = id, message = "You've selected apples.")


if __name__ == "__main__":
    app.run(debug=True)
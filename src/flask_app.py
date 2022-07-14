from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/person/")
def hello_people():
    return jsonify({'name': 'Ravi Shankar',
                    'Address': 'California'})


@app.route("/numbers/")
def print_list():
    app.logger.debug("The function will get us a list of 5 numbers as a json")
    return jsonify(list(range(5)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
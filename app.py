from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Flask!"


@app.route('/cal', methods=["GET"])
def calculate():
    print("received :", request.json)

    operation = request.json["operation"]
    num_01 = int(request.json["num_01"])
    num_02 = int(request.json["num_02"])
    
    result = 0

    if operation == "add":
        result = num_01 + num_02
    elif operation == "sub":
        result = num_01 - num_02
    elif operation == "mul":
        result = num_01 * num_02
    elif operation == "div":
        result = num_01 / num_02
    else:
        result =  "Unsupported Operation : " + operation

    return f"Result of {num_01} {operation} {num_02} is : {str(result)}"



print("app name :", __name__)

if __name__ == "__main__":
    app.run(debug=True)



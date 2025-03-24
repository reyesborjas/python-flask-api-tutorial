from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


todos = [
    { "label": "Study python", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos) 

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
   
    if position < 0 or position >= len(todos):
        return jsonify(todos) 
   
    todos.pop(position)
    return jsonify(todos), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

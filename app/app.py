from flask import Flask, jsonify, request
import database
from os import getenv

app = Flask(__name__)


@app.before_first_request
def initialize_database():
    try:
        if (database.ConnectorMysql() is None):
            raise "Database Can't connect"
        database.InitDB()
    except Exception as e:
        print(f"An error occurred during DB initialization: {e}")


@app.route('/')
def index():
    if (database.ConnectorMysql() is None):
        raise "Database Can't connect"
    return "Index!"


# returns a list of registered users on a system
@app.route('/user', methods=['GET'])
def get_all_users():
    result = []
    try:
        if (database.ConnectorMysql() is None):
            raise "Database Can't connect"
        users = database.get_all("USERS")
        if (len(users) > 0):
            for u in users:
                user_dict = {
                "uid": u[0],
                "name": u[1],
                "age": int(u[2])
                }
            result.append(user_dict)
            
    except Exception as error:
        return f"{error}"
    
    return jsonify(result)


# creates a user with the ID 123 using the body data. The response returns the ID.
@app.route('/user', methods=['POST'])
def create_user():
    try:
        if (database.ConnectorMysql() is None):
            raise "Database Can't connect"
        data = request.get_json()
        uid = data.get('uid')
        name = data.get('name')
        age = data.get('age')
        database.insert_data("USERS", uid, name, age)
        result = {"uid": uid,
                "name": name,
                "age": int(age)}
        
    except Exception as error:
        result = {"error_msg": error}
        
    return result


# updates user 123 with the body data
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        if (database.ConnectorMysql() is None):
            raise "Database Can't connect"
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        database.update_data("USERS", user_id, name, age)
        result = {"message": f"Update user with id={user_id} succesful"}
        
    except Exception as error:
        result = {"error_msg": error}  
        
    return  result


# returns the details of user 123
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        if (database.ConnectorMysql() is None):
            raise "Database Can't connect"
        user_row = database.get_data("USERS", user_id)
        result = {
            "uid": user_row[0],
            "name": user_row[1],
            "age": int(user_row[2])
        }

    except Exception as error:
        result = {"error_msg": error} 
        
    return jsonify(result)


# deletes user 123
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        if (database.ConnectorMysql() is None):
            raise "Database Can't connect"
        database.delete_data("USERS", user_id)
        result = {"message": f"Delete user with id={user_id} succesful"}

    except Exception as error:
        result = {"error_msg": error} 
        
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

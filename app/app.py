from database import MySqlConnector, CollectionsName
from global_config import GlobalConfig
from flask import Flask, jsonify, request, abort
from os import getenv
from invalid_api_usage import InvalidAPIUsage

app = Flask(__name__)
_db = MySqlConnector(
    host=getenv(GlobalConfig.HOST),
    user=getenv(GlobalConfig.USER),
    pwd=getenv(GlobalConfig.PASSWORD),
    db_name=getenv(GlobalConfig.DB_NAME)
)

@app.errorhandler(Exception)
def invalid_api_usage(e):
    return jsonify({ "error_message": f'{e}' }), 500

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code

@app.route('/')
def index():
    return "Index!"


# returns a list of registered users on a system
@app.route('/user', methods=['GET'])
def get_all_users():
    result = []
    users = _db.get_all(CollectionsName.USER)
    if (users and len(users) > 0):
        for u in users:
            user_dict = {
            "uid": u[0],
            "name": u[1],
            "age": int(u[2])
            }
            result.append(user_dict)
    
    return jsonify(result)


# creates a user with the ID 123 using the body data. The response returns the ID.
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    uid = data.get('uid')
    name = data.get('name')
    age = data.get('age')
    _db.insert_data(CollectionsName.USER, uid, name, age)
    result = {
                "age": int(age),
                "name": name,
                "uid": uid
            }
    return jsonify(result)


# updates user 123 with the body data
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    _db.update_data(CollectionsName.USER, user_id, name, age)
    result = {"message": f"Update user with id={user_id} succesful"} 
        
    return  jsonify(result)


# returns the details of user 123
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    result = _db.get_data(CollectionsName.USER, user_id)
    return jsonify(result)


# deletes user 123
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    _db.delete_data(CollectionsName.USER, user_id)
    result = {"message": f"Delete user with id={user_id} succesful"}
        
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

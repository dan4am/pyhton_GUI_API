import datetime

import wrapper
from flask import Flask, jsonify
from flask_restful import reqparse

app = Flask(__name__)



@app.route('/apidan', methods=['GET'])
def get_all_users():
    result = wrapper.get_all_users()
    if result:
        return jsonify(status="True",
        result= [{"nom": user.last_name,
                    "prenom": user.first_name,
                    "id": user.id,
                    "birthdate": user.birthdate} for user in result.all() ])
    return jsonify(status="False")

@app.route('/new', methods=['POST'])
def new_user():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type = int, help = 'id must be an int')
    parser.add_argument('first_name' , help = 'id must be an string')
    parser.add_argument('last_name', help = 'id must be an string')
    parser.add_argument('birthdate', help = 'id must be a valid date')
    args = parser.parse_args()
    print(args)
    result = wrapper.add_user(args)
    if result:
        return jsonify(status="True",
        result= [{"nom": args['last_name'],
                    "prenom": args['first_name'],
                    "id": args['id'],
                    "birthdate": args['birthdate']}])
    return jsonify(status="False")

@app.route('/apidan/user/<id>', methods = ['DELETE'])
def delete_user(id):
    temp = wrapper.get_user_by_id(id)
    result = wrapper.delete_user(id)
    if result:
        return jsonify(status="True",
                       result={"nom": temp.last_name,
                               "prenom": temp.first_name,
                               "id": temp.id,
                               "birthdate": temp.birthdate}
                       )
    return jsonify(status="False")


@app.route('/apidan/user/<id>', methods=['GET'])
def get_user(id):

    result = wrapper.get_user_by_id(id)
    # print ("original")
    if result:
        return jsonify(status="True",
                    result={"nom":result.last_name,
                            "prenom":result.first_name,
                            "id":result.id,
                            "birthdate": result.birthdate}
                        )
    return jsonify(status="False")





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
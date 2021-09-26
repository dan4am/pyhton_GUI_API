import wrapper
from flask import Flask, jsonify

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

@app.route('/apidan/user/<id>', methods=['GET'])
def get_user(id):
    result = wrapper.get_user_by_id(id)
    if result:
        return jsonify(status="True",
                    result={"nom":result.last_name,
                            "prenom":result.first_name,
                            "id":result.id,
                            "birthdate": result.birthdate}
                        )
    return jsonify(status="False")





if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
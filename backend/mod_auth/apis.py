from flask import Blueprint, jsonify, flash, request
from pprint import pprint
from flask import current_app


############################
#
#   AUTH Module apis
#
#############################

mod_auth_api = Blueprint('mod_auth_api', __name__,)

@mod_auth_api.post('register')
def register():
    response = {}
    response['request_parameters'] = request.get_json()


    username = response.get('request_parameters').get('username')
    email = response.get('request_parameters').get('email')
    password = response.get('request_parameters').get('password')

    if not username or not email or not password:
        response['error_msg'] = "Something is not right. Check the user data again."
        current_app.logger.info(response.get('error_msg'))
        return jsonify(response)

    current_app.logger.info("Trying to register user : "
                        f"{response.get('request_parameters').get('username')}")
    
    # TBD: Register user here in db

    return jsonify(response)



@mod_auth_api.post('login')
def login():
    response = {}
    response['request_parameters'] = request.get_json()


    email = response.get('request_parameters').get('email')
    password = response.get('request_parameters').get('password')

    if not email or not password:
        response['error_msg'] = "Something is not right. Check the user data again."
        current_app.logger.info(response.get('error_msg'))
        return jsonify(response)

    current_app.logger.info("Trying to login user : "
                        f"{response.get('request_parameters').get('username')}")
    
    # TBD: login user here from db

    # TBD: setup session
    
    return jsonify(response)

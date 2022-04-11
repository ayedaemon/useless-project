from flask import Blueprint, jsonify, flash, request
from pprint import pprint
from flask import current_app
from .db import UserAuthDB, open_conn, close_conn, create_table

############################
#
#   AUTH Module apis == REGISTER
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
    
    # Create UserAuth object
    user = UserAuthDB(
        username=username,
        email=email,
        passwd=password)
    # Add user to DB
    status = user.db_add_user()
    # Check if already registered or new register
    if status == True:
        response['msg'] = 'User added successfully!'
    elif status == False:
        response['msg'] = 'User already registered. Please login!'
    
    return jsonify(response)


############################
#
#   AUTH Module apis ==  LOGIN
#
#############################

@mod_auth_api.post('login')
def login():
    response = {}
    response['request_parameters'] = request.get_json()


    email = response.get('request_parameters').get('email')
    password = response.get('request_parameters').get('password')

    current_app.logger.info(email, password)

    if not email or not password:
        response['error_msg'] = "Something is not right. Check the user data again."
        current_app.logger.info(response.get('error_msg'))
        return jsonify(response)

    current_app.logger.info("Trying to login user : "
                        f"{response.get('request_parameters').get('username')}")
    
    # TBD: login user here from db

    # TBD: setup session
    
    return jsonify(response)

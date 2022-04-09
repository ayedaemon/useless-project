from flask import Blueprint, jsonify




############################
#
#   AUTH Module apis
#
#############################

mod_auth_api = Blueprint('mod_auth_api', __name__,)

@mod_auth_api.post('register')
def register():
    response = {}
    print('INVOKED')
    response['msg'] = 'Site under construction'

    return jsonify(response)



@mod_auth_api.post('login')
def login():
    response = {}
    
    response['msg'] = 'Site under construction'
    
    return jsonify(response)

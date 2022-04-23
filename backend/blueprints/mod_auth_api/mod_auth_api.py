from flask import Blueprint, jsonify, request, current_app, Response
from models.user import User, db

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


mod_auth_api = Blueprint('mod_auth_api', __name__)


@mod_auth_api.post('/register/')
def register() -> Response:
    data = request.get_json()
    response = {}
    response['username'] = data.get('username')
    response['email'] = data.get('email')
    current_app.logger.info(f"Recieved data from HTTP request.. Creating user:{data.get('username')} now")
    try:
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'))
        db.session.add(user)
        db.session.commit()
        current_app.logger.info(f"user:{data.get('username')} added to database successfully")
        response['msg'] = "User added succesfully"
        response['status'] = 200
    except Exception as ex:
        current_app.logger.error(ex)
        current_app.logger.warning('Failed to add user in database. Try changing the username/email.')
        response['msg'] = "Failed to add user"
        response['error'] = str(ex)
        response['status'] = 200
    
    return jsonify(response), response.get('status')



@mod_auth_api.post('/login/')
def login() -> Response:
    data = request.get_json()
    response = {}
    response['username'] = data.get('username')
    current_app.logger.info(f"Recieved data from HTTP request.. Logging in user:{data.get('username')} now")
    try:
        user = User.query.filter_by(username=data.get('username')).first()
        if user and user.checkPassword(data.get('password')):
            jwt_token = create_access_token(
                identity=user.as_dict()
            )
            response['jwt_token'] = jwt_token
            response['msg'] = "Successfully logged in."
            response['status'] = 200
        else:
            raise Exception('Failed to login. Check the user input.')
    except Exception as ex:
        current_app.logger.error(ex)
        current_app.logger.warning("Failed to log in user:{data.get('username')}")
        response['msg'] = "Failed to log in"
        response['error'] = str(ex)
        response['status'] = 403

    return jsonify(response), response.get('status')



@mod_auth_api.route('/test')
def test():
    db.create_all()
    return '', 301



@mod_auth_api.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

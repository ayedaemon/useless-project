from flask import Blueprint, jsonify, request, current_app, Response
from models.user import User, db

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from .hibp import Hibp

mod_scanner = Blueprint('mod_scanner', __name__)


@mod_scanner.route('/hibp/<observable>', methods=['GET', 'POST'])
@jwt_required()
def hibp(observable):
    r = Hibp.get(observable).json()
    return jsonify({
        'hibp': r
    })
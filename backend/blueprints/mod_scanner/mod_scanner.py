from flask import Blueprint, jsonify, request, current_app, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from .hibp import Hibp

mod_scanner = Blueprint('mod_scanner', __name__)


@mod_scanner.route('/hibp/<observable>', methods=['GET', 'POST'])
@jwt_required()
def hibp(observable):
    r = Hibp.get(observable).json()
    return jsonify({
        'hibp': r
    })
from flask import Blueprint, request, jsonify


bp = Blueprint('views', __name__, url_prefix='')


@bp.route('/ip', methods=['GET'])
def get_ip():
    return jsonify(ip=request.remote_addr)


@bp.route('/', methods=['GET'])
def index():
    pass

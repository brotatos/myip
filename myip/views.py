from flask import Blueprint, request, jsonify, render_template


bp = Blueprint('views', __name__, url_prefix='')


@bp.route('/ip', methods=['GET'])
def get_ip():
    return jsonify(ip=request.remote_addr)


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

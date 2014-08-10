from flask import Blueprint, request, render_template


bp = Blueprint('views', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def index():
    headers_list = request.headers.getlist("X-Forwarded-For")
    user_ip = headers_list[0] if headers_list else request.remote_addr
    return render_template('index.html', ip=user_ip)

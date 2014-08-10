from flask import Blueprint, request, render_template


bp = Blueprint('views', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', ip=request.remote_addr)

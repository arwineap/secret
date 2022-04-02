import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('messages', __name__)

@bp.route('/messages')
def messages():
#    return 'testing'
    db = get_db()
    messages = db.execute(
        'SELECT p.id, owner_id, created, username, title, body, otp, read_time'
        ' FROM messages p JOIN user u ON p.owner_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('messages/messages.html', messages=messages)

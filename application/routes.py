from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Game


@app.route('/play', methods=['GET', 'POST'])
def user_records():
    if request.method == 'GET':
        new_game = Game()
        db.session.add(new_game)
        db.session.commit()
        return make_response(f"{new_game}")

from flask import request, render_template, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Game



@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'GET':
        new_game = Game.new()
        db.session.add(new_game)
        db.session.commit()
        return jsonify(new_game.dump())
    elif request.method == 'POST':
        body = request.json
        game_id = body.get('uuid')
        position = body.get('position')
        player = body.get('player')
        if not (game_id and position and player):
            return 'Request malformed', 400
        game = Game.query.filter(Game.uuid == game_id).first()
        result = game.play(player, position)
        return jsonify(result)

@app.route('/dice', methods=['GET'])
def dice():
    if not (uuid := request.args.get('id')):
        return 'Missing game ID', 400
    else:
        game = Game.query.filter(Game.uuid == uuid).first()
        return jsonify(game.dice())

@app.route('/status', methods=['GET'])
def status():
    if not (uuid := request.args.get('id')):
        return 'Missing game ID', 400
    else:
        game = Game.query.filter(Game.uuid == uuid).first()
        return jsonify(game.dump())

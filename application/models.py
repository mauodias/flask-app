from . import db
import json
import uuid

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    _uuid = db.Column(
        'uuid',
        db.String(36),
        index=False,
        unique=True,
        nullable=False,
        default=uuid.uuid4
    )
    player1_id = db.Column(
        'player1_id',
        db.Integer,
        db.ForeignKey('players.id')
    )
    player2_id = db.Column(
        'player2_id',
        db.Integer,
        db.ForeignKey('players.id')
    )
    next_player_id = db.Column(
        db.Integer,
        db.ForeignKey('players.id')
    )
    player1 = db.relationship('Player', foreign_keys=[player1_id])
    player2 = db.relationship('Player', foreign_keys=[player2_id])
    next_player = db.relationship('Player', foreign_keys=[next_player_id])
    dice = db.Column(
        db.Integer,
        default=-1
    )
    board = db.Column(
        db.String(64),
        nullable=False,
        default=''
    )

    @property
    def uuid(self):
        return uuid.UUID(self._uuid)

    def __repr__(self):
        return f'{str(self.uuid)}'

    @staticmethod
    def new():
        player = Player()
        game = Game.query.filter(
            Game.player2 == None
        ).first()
        if game:
            game.player2 = player
        else:
            game = Game()
            game.player1 = player
            game.next_player = player
        return game

    def dump(self):
        obj = {
            'id': str(self.uuid),
            'board': self.board,
            'dice': self.dice,
            'player1': {
                'id': self.player1.id,
                'total_rocks': self.player1.total_rocks,
                'active_rocks': self.player1.active_rocks
            },
            'player2': None if not self.player2 else {
                'id': self.player2.id,
                'total_rocks': self.player2.total_rocks,
                'active_rocks': self.player2.active_rocks
            },
            'next_player': self.next_player.id
        }
        return obj


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    total_rocks = db.Column(
        db.Integer,
        default=7
    )
    active_rocks = db.Column(
        db.Integer,
        default=0
    )

    def play_rock(self):
        if self.active_rocks < self.total_rocks:
            self.active_rocks += 1
            return True
        return False

    def return_rock(self):
        if self.active_rocks > 0:
            self.active_rocks -= 1
            return True
        return False

    def score(self):
        if self.total_rocks > 0 and self.active_rocks > 0:
            self.total_rocks -= 1
            self.active_rocks -= 1
            return True
        return False

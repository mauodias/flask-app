from .db import db

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

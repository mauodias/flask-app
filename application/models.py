from . import db
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

    @property
    def uuid(self):
        return uuid.UUID(self._uuid)

    def __repr__(self):
        return f'{str(self.uuid)}'

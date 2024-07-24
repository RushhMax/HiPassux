from app.extensions import db
from datetime import datetime

class Reaction(db.Model):
    __tablename__ = 'REACTIONS'

    reaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('POSTS.post_id', ondelete='CASCADE'), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('COMMENTS.comment_id', ondelete='CASCADE'), nullable=True)
    type = db.Column(db.Enum('like', 'dislike', 'love', 'haha', 'wow', 'sad', 'angry', name='reaction_type'))

    def __repr__(self):
        return f'<Reaction {self.reaction_id}>'

    def to_dict(self):
        return {
            'id': self.reaction_id,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'comment_id': self.comment_id,
            'type': self.type
        }


from app.extensions import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'COMMENTS'

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('POSTS.post_id', ondelete='CASCADE'), nullable=False)

    reactions = db.relationship('Reaction', backref='comment', lazy=True)

    def __repr__(self):
        return f'<Comment {self.comment_id}>'

    def to_dict(self):
        return {
            'id': self.comment_id,
            'content': self.content,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'user_id': self.user_id,
            'post_id': self.post_id
        }

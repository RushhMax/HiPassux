from app.extensions import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'MESSAGES'

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    sender_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id', ondelete='CASCADE'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id', ondelete='CASCADE'), nullable=False)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Message {self.message_id}>'

    def to_dict(self):
        return {
            'id': self.message_id,
            'content': self.content,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'is_read': self.is_read
        }
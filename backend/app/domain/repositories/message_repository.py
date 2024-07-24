from app.domain.entities.message import db, Message

class MessageRepository:

    @staticmethod
    def get_all_messages():
        return Message.query.all()
    
    @staticmethod
    def add_message(message):
        db.session.add(message)
        db.session.commit()

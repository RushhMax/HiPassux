from app.domain.repositories.message_repository import Message,MessageRepository

class MessageService:

    @staticmethod
    def get_all_messages():
        return MessageRepository.get_all_Messages()

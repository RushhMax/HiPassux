from app.domain.repositories.comment_repository import Comment,CommentRepository

class CommentService:

    @staticmethod
    def get_all_comments():
        return CommentRepository.get_all_Comments()

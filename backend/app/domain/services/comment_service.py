from app.domain.repositories.comment_repository import CommentRepository

class CommentService:

    @staticmethod
    def get_all_comments():
        return CommentRepository.get_all_comments()
    
    @staticmethod
    def get_comment_by_id(comment_id):
        return CommentRepository.get_comment_by_id(comment_id)
    
    @staticmethod
    def create_comment(content, user_id, post_id):
        return CommentRepository.create_comment(content, user_id, post_id)
    
    @staticmethod
    def update_comment(comment_id, content):
        return CommentRepository.update_comment(comment_id, content)
    
    @staticmethod
    def delete_comment(comment_id):
        return CommentRepository.delete_comment(comment_id)
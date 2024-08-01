from app.extensions import db
from app.domain.entities.comment import Comment

class CommentRepository:

    @staticmethod
    def get_all_comments():
        return Comment.query.all()
    
    @staticmethod
    def get_comment_by_id(comment_id):
        return Comment.query.get(comment_id)
    
    @staticmethod
    def create_comment(content, user_id, post_id):
        new_comment = Comment(content=content, user_id=user_id, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment
    
    @staticmethod
    def update_comment(comment_id, content):
        comment = Comment.query.get(comment_id)
        if comment:
            comment.content = content
            db.session.commit()
        return comment
    
    @staticmethod
    def delete_comment(comment_id):
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
        return comment
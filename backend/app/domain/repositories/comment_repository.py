from app.domain.entities.comment import db, Comment

class CommentRepository:

    @staticmethod
    def get_all_comments():
        return Comment.query.all()
    
    @staticmethod
    def add_comment(comment):
        db.session.add(comment)
        db.session.commit()

from app.domain.entities.post import db, Post

class PostRepository:

    @staticmethod
    def get_all_posts():
        return Post.query.all()
    
    @staticmethod
    def add_post(post):
        db.session.add(post)
        db.session.commit()

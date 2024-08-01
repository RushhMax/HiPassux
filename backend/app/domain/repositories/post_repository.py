from app.domain.entities.post import db, Post
from app.domain.entities.user  import User

class PostRepository:

    @staticmethod
    def get_all_posts():
        return Post.query.all()
    
    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_posts_by_username(username):
        user = User.query.filter_by(username=username).first()
        if not user:
            return []

        return Post.query.filter_by(user_id=user.user_id).all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.get(post_id)
    
    @staticmethod
    def add(post):
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def update_post(post_id, updated_data):
        post = Post.query.get(post_id)
        if post:
            for key, value in updated_data.items():
                setattr(post, key, value)
            db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
        return post

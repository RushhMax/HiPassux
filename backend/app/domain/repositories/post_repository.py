from app.domain.entities.post import db, Post
from app.domain.entities.user  import User

class PostRepository:

    @staticmethod
    def get_all_posts():
        return Post.query.all()
    
    @staticmethod
    def get_posts_by_user(user_id):
        """Retrieve all posts for a specific user."""
        return Post.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_posts_by_username(username):
        # Obtén el usuario por su ID
        user = User.query.filter_by(username=username).first()
        if not user:
            return []  # o lanza una excepción si el usuario no existe

        # Usa el username del usuario para buscar los posts
        return Post.query.filter_by(user_id=user.user_id).all()
    

    @staticmethod
    def get_post_by_id(post_id):
        """Retrieve a single post by its ID."""
        return Post.query.get(post_id)
    
    @staticmethod
    def add(post):
        db.session.add(post)
        db.session.commit()
        # Añade un usuario a la base de datos y confirma la transacción.

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
        """Delete a post from the database."""
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
        return post

from app.domain.repositories.post_repository import Post,PostRepository

class PostService:

    @staticmethod
    def get_all_posts():
        return PostRepository.get_all_posts()

    @staticmethod
    def create_post(content, user_id):
        new_post = Post(
            content = content,
            user_id = user_id
        )
        PostRepository.add_post(new_post)
        return new_post
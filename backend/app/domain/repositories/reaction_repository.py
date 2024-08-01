from app.domain.entities.reaction import db, Reaction
from app.domain.repositories.base_repository import BaseRepository

class ReactionRepository(BaseRepository):

    @staticmethod
    def get_all_reactions():
        return Reaction.query.all()
        # Obtiene todos las reacciones  de la base de datos.

    def get_reactions_by_post(self, post_id):
        """Get all reactions for a specific post."""
        return Reaction.query.filter_by(post_id=post_id).all()

    def add_reaction_to_post(self, reaction, post_id):
        """
        Add a reaction to a specific post.
        
        Args:
            reaction: The Reaction object to be added.
            post_id: The ID of the post to which the reaction is added.
        """
        reaction.post_id = post_id
        db.session.add(reaction)
        db.session.commit()

    def remove_reaction(self, reaction):
        """Remove a reaction from the database."""
        db.session.delete(reaction)
        db.session.commit()

    def remove_reactions_by_post(self, post_id):
        """
        Remove all reactions for a specific post.
        
        Args:
            post_id: The ID of the post from which all reactions should be removed.
        """
        reactions = Reaction.query.filter_by(post_id=post_id).all()
        for reaction in reactions:
            db.session.delete(reaction)
        db.session.commit()

    def add(self, reaction):
        db.session.add(reaction)
        db.session.commit()
        # Añade un usuario a la base de datos y confirma la transacción.

    def remove(self, reaction):
        db.session.delete(reaction)
        db.session.commit()
        # Elimina un usuario de la base de datos y confirma la transacción.

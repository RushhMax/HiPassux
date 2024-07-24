from app.domain.entities.reaction import db, Reaction

class ReactionRepository:

    @staticmethod
    def get_all_reactions():
        return Reaction.query.all()
    
    @staticmethod
    def add_reaction(reaction):
        db.session.add(reaction)
        db.session.commit()

"""
Modèle Feature pour le Planning Poker
"""

class Feature:
    """Représente une fonctionnalité du backlog"""
    
    def __init__(self, name: str, description: str = "", feature_id: int = None):
        self.name = name
        self.description = description
        self.feature_id = feature_id
        self.estimated_difficulty = None
        self.is_validated = False
        self.vote_history = []  # Historique des tours de vote
        self.current_round = 0
        
    def add_vote_round(self, votes: dict):
        """Ajoute un tour de vote à l'historique"""
        self.current_round += 1
        self.vote_history.append({
            "round": self.current_round,
            "votes": votes.copy()
        })
        
    def validate(self, difficulty):
        """Valide la fonctionnalité avec une difficulté"""
        self.estimated_difficulty = difficulty
        self.is_validated = True
        
    def reset_votes(self):
        """Réinitialise les votes pour un nouveau tour"""
        pass  # Les votes sont gérés au niveau du game
        
    def to_dict(self):
        """Convertit la feature en dictionnaire"""
        return {
            "name": self.name,
            "description": self.description,
            "feature_id": self.feature_id,
            "estimated_difficulty": self.estimated_difficulty,
            "is_validated": self.is_validated,
            "vote_history": self.vote_history,
            "current_round": self.current_round
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crée une feature depuis un dictionnaire"""
        feature = cls(
            data["name"],
            data.get("description", ""),
            data.get("feature_id")
        )
        feature.estimated_difficulty = data.get("estimated_difficulty")
        feature.is_validated = data.get("is_validated", False)
        feature.vote_history = data.get("vote_history", [])
        feature.current_round = data.get("current_round", 0)
        return feature
    
    def __repr__(self):
        status = "✅" if self.is_validated else "⏳"
        return f"Feature({status} '{self.name}', difficulty={self.estimated_difficulty})"
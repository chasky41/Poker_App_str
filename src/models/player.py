"""
Modèle Player pour le Planning Poker
"""

class Player:
    """Représente un joueur dans le Planning Poker"""
    
    def __init__(self, name: str, player_id: int):
        self.name = name
        self.player_id = player_id
        self.current_vote = None
        self.has_voted = False
        
    def vote(self, card_value):
        """Enregistre le vote du joueur"""
        self.current_vote = card_value
        self.has_voted = True
        
    def reset_vote(self):
        """Réinitialise le vote du joueur"""
        self.current_vote = None
        self.has_voted = False
        
    def to_dict(self):
        """Convertit le joueur en dictionnaire"""
        return {
            "name": self.name,
            "player_id": self.player_id,
            "current_vote": self.current_vote,
            "has_voted": self.has_voted
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crée un joueur depuis un dictionnaire"""
        player = cls(data["name"], data["player_id"])
        player.current_vote = data.get("current_vote")
        player.has_voted = data.get("has_voted", False)
        return player
    
    def __repr__(self):
        return f"Player(name='{self.name}', id={self.player_id})"
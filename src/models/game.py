"""
Modèle Game - Logique métier du Planning Poker
"""
from typing import List, Dict, Optional
from datetime import datetime
from .player import Player
from .feature import Feature
from ..voting_modes.strict_mode import StrictMode
from ..voting_modes.average_mode import AverageMode
from ..voting_modes.median_mode import MedianMode

class Game:
    """Gère la logique du jeu Planning Poker"""
    
    def __init__(self, players: List[Player], features: List[Feature], voting_mode: str):
        self.players = players
        self.features = features
        self.voting_mode_name = voting_mode
        self.voting_mode = self._get_voting_mode(voting_mode)
        self.current_feature_index = 0
        self.game_started = False
        self.game_finished = False
        self.start_time = None
        
    def _get_voting_mode(self, mode_name: str):
        """Retourne l'instance du mode de vote"""
        modes = {
            "strict": StrictMode(),
            "average": AverageMode(),
            "median": MedianMode()
        }
        return modes.get(mode_name, StrictMode())
    
    def start_game(self):
        """Démarre la partie"""
        self.game_started = True
        self.start_time = datetime.now()
        
    def get_current_feature(self) -> Optional[Feature]:
        """Retourne la fonctionnalité actuelle"""
        if self.current_feature_index < len(self.features):
            return self.features[self.current_feature_index]
        return None
    
    def get_progress(self) -> Dict:
        """Retourne la progression de la partie"""
        total = len(self.features)
        completed = sum(1 for f in self.features if f.is_validated)
        return {
            "total": total,
            "completed": completed,
            "current": self.current_feature_index + 1,
            "percentage": (completed / total * 100) if total > 0 else 0
        }
    
    def record_votes(self, votes: Dict[str, any]):
        """Enregistre les votes des joueurs"""
        current_feature = self.get_current_feature()
        if current_feature:
            current_feature.add_vote_round(votes)
    
    def process_votes(self) -> Dict:
        """
        Traite les votes et détermine si la feature est validée
        
        Returns:
            Dict avec les clés:
            - validated: bool
            - difficulty: Optional[float]
            - message: str
            - coffee_break: bool
        """
        current_feature = self.get_current_feature()
        if not current_feature:
            return {
                "validated": False,
                "difficulty": None,
                "message": "Aucune feature en cours",
                "coffee_break": False
            }
        
        # Récupérer les votes actuels
        votes = {p.name: p.current_vote for p in self.players if p.has_voted}
        
        # Vérifier si tout le monde a voté
        if len(votes) != len(self.players):
            return {
                "validated": False,
                "difficulty": None,
                "message": "Tous les joueurs n'ont pas encore voté",
                "coffee_break": False
            }
        
        # Vérifier si pause café
        if all(v == "☕" for v in votes.values()):
            return {
                "validated": False,
                "difficulty": None,
                "message": "Pause café demandée ! ☕",
                "coffee_break": True
            }
        
        # Enregistrer les votes
        self.record_votes(votes)
        
        # Calculer le résultat avec le mode de vote
        round_number = current_feature.current_round
        is_validated, difficulty = self.voting_mode.calculate_result(votes, round_number)
        
        if is_validated:
            current_feature.validate(difficulty)
            message = f"✅ Feature validée avec une difficulté de {difficulty}"
        else:
            if round_number == 1:
                message = "❌ Pas d'unanimité. Discussion nécessaire, puis revotez."
            else:
                message = f"❌ Vote non validé (Tour {round_number}). Continuez la discussion."
        
        return {
            "validated": is_validated,
            "difficulty": difficulty,
            "message": message,
            "coffee_break": False
        }
    
    def next_feature(self):
        """Passe à la feature suivante"""
        self.current_feature_index += 1
        if self.current_feature_index >= len(self.features):
            self.game_finished = True
        self.reset_player_votes()
    
    def reset_player_votes(self):
        """Réinitialise les votes de tous les joueurs"""
        for player in self.players:
            player.reset_vote()
    
    def get_results(self) -> Dict:
        """Retourne les résultats finaux de la partie"""
        return {
            "game_date": datetime.now().isoformat(),
            "voting_mode": self.voting_mode_name,
            "players": [p.name for p in self.players],
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "results": [
                {
                    "feature": f.name,
                    "description": f.description,
                    "difficulty": f.estimated_difficulty,
                    "rounds": f.current_round,
                    "vote_history": f.vote_history
                }
                for f in self.features if f.is_validated
            ]
        }
    
    def to_dict(self) -> Dict:
        """Convertit le jeu en dictionnaire pour sauvegarde"""
        return {
            "players": [p.to_dict() for p in self.players],
            "features": [f.to_dict() for f in self.features],
            "voting_mode": self.voting_mode_name,
            "current_feature_index": self.current_feature_index,
            "game_started": self.game_started,
            "game_finished": self.game_finished,
            "start_time": self.start_time.isoformat() if self.start_time else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Crée une partie depuis un dictionnaire"""
        players = [Player.from_dict(p) for p in data["players"]]
        features = [Feature.from_dict(f) for f in data["features"]]
        
        game = cls(players, features, data["voting_mode"])
        game.current_feature_index = data["current_feature_index"]
        game.game_started = data["game_started"]
        game.game_finished = data["game_finished"]
        
        if data.get("start_time"):
            game.start_time = datetime.fromisoformat(data["start_time"])
        
        return game
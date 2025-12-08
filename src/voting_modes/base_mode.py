"""
Classe abstraite pour les modes de vote
"""
from abc import ABC, abstractmethod
from typing import Dict, Tuple, Optional

class VotingMode(ABC):
    """Classe de base pour tous les modes de vote"""
    
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def calculate_result(self, votes: Dict[str, any], round_number: int) -> Tuple[bool, Optional[float]]:
        """
        Calcule le résultat d'un vote
        
        Args:
            votes: Dictionnaire {player_name: vote_value}
            round_number: Numéro du tour actuel
            
        Returns:
            Tuple (is_validated, difficulty)
            - is_validated: True si le vote est validé
            - difficulty: Valeur de difficulté si validé, None sinon
        """
        pass
    
    def filter_numeric_votes(self, votes: Dict[str, any]) -> list:
        """Filtre uniquement les votes numériques"""
        numeric_votes = []
        for vote in votes.values():
            if isinstance(vote, (int, float)) and vote != "?" and vote != "☕":
                numeric_votes.append(vote)
        return numeric_votes
    
    def check_special_cards(self, votes: Dict[str, any]) -> Optional[str]:
        """Vérifie si des cartes spéciales ont été jouées"""
        vote_values = list(votes.values())
        
        # Si tout le monde a joué café
        if all(v == "☕" for v in vote_values):
            return "coffee_break"
        
        # Si quelqu'un a joué "?"
        if "?" in vote_values:
            return "unknown"
            
        return None
    
    def check_unanimity(self, votes: Dict[str, any]) -> Tuple[bool, Optional[float]]:
        """Vérifie l'unanimité"""
        numeric_votes = self.filter_numeric_votes(votes)
        
        if not numeric_votes:
            return False, None
            
        if len(set(numeric_votes)) == 1:
            return True, numeric_votes[0]
            
        return False, None
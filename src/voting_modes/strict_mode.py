"""
Mode de vote strict (Unanimité)
"""
from .base_mode import VotingMode
from typing import Dict, Tuple, Optional

class StrictMode(VotingMode):
    """Mode de vote strict - nécessite l'unanimité"""
    
    def __init__(self):
        super().__init__("Strict (Unanimité)")
        
    def calculate_result(self, votes: Dict[str, any], round_number: int) -> Tuple[bool, Optional[float]]:
        """
        En mode strict, l'unanimité est requise à chaque tour
        
        Args:
            votes: Dictionnaire {player_name: vote_value}
            round_number: Numéro du tour
            
        Returns:
            Tuple (is_validated, difficulty)
        """
        # Vérifier les cartes spéciales
        special = self.check_special_cards(votes)
        if special == "coffee_break":
            return False, None  # Pause café demandée
        
        # Vérifier l'unanimité
        is_unanimous, difficulty = self.check_unanimity(votes)
        
        return is_unanimous, difficulty
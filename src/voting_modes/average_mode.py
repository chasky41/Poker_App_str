"""
Mode de vote par moyenne
"""
from .base_mode import VotingMode
from typing import Dict, Tuple, Optional
import statistics

class AverageMode(VotingMode):
    """Mode de vote par moyenne - après le premier tour"""
    
    def __init__(self):
        super().__init__("Moyenne")
        
    def calculate_result(self, votes: Dict[str, any], round_number: int) -> Tuple[bool, Optional[float]]:
        """
        Premier tour : unanimité requise
        Tours suivants : moyenne des votes
        
        Args:
            votes: Dictionnaire {player_name: vote_value}
            round_number: Numéro du tour (commence à 1)
            
        Returns:
            Tuple (is_validated, difficulty)
        """
        # Vérifier les cartes spéciales
        special = self.check_special_cards(votes)
        if special == "coffee_break":
            return False, None
        
        # Premier tour : unanimité obligatoire
        if round_number == 1:
            return self.check_unanimity(votes)
        
        # Tours suivants : calcul de la moyenne
        numeric_votes = self.filter_numeric_votes(votes)
        
        if not numeric_votes:
            return False, None
        
        # Calculer la moyenne et arrondir
        average = statistics.mean(numeric_votes)
        
        # Arrondir à la valeur Fibonacci la plus proche
        fibonacci_values = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100]
        closest_value = min(fibonacci_values, key=lambda x: abs(x - average))
        
        return True, closest_value
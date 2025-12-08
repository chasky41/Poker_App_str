"""
Gestion des imports/exports JSON
"""
import json
import os
from datetime import datetime
from typing import List, Dict
from pathlib import Path

class JSONHandler:
    """Gère les opérations d'import/export JSON"""
    
    def __init__(self):
        self.data_dir = Path("data")
        self.backlogs_dir = self.data_dir / "backlogs"
        self.saves_dir = self.data_dir / "saves"
        self.results_dir = self.data_dir / "results"
        
        # Créer les dossiers s'ils n'existent pas
        self.backlogs_dir.mkdir(parents=True, exist_ok=True)
        self.saves_dir.mkdir(parents=True, exist_ok=True)
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
    def load_backlog(self, filepath: str) -> List[Dict]:
        """
        Charge un backlog depuis un fichier JSON
        
        Format attendu:
        {
            "backlog": [
                {
                    "name": "Feature 1",
                    "description": "Description..."
                },
                ...
            ]
        }
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("backlog", [])
        except Exception as e:
            raise Exception(f"Erreur lors du chargement du backlog: {str(e)}")
    
    def save_game(self, game_data: Dict, filename: str = None) -> str:
        """Sauvegarde l'état actuel de la partie"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"save_{timestamp}.json"
        
        filepath = self.saves_dir / filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(game_data, f, indent=2, ensure_ascii=False)
            return str(filepath)
        except Exception as e:
            raise Exception(f"Erreur lors de la sauvegarde: {str(e)}")
    
    def load_game(self, filepath: str) -> Dict:
        """Charge une partie sauvegardée"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Erreur lors du chargement de la sauvegarde: {str(e)}")
    
    def save_results(self, results: Dict, filename: str = None) -> str:
        """
        Sauvegarde les résultats finaux
        
        Format:
        {
            "game_date": "2024-12-01",
            "voting_mode": "strict",
            "players": [...],
            "results": [
                {
                    "feature": "Feature 1",
                    "difficulty": 5,
                    "rounds": 2
                },
                ...
            ]
        }
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"results_{timestamp}.json"
        
        filepath = self.results_dir / filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            return str(filepath)
        except Exception as e:
            raise Exception(f"Erreur lors de la sauvegarde des résultats: {str(e)}")
    
    def list_saves(self) -> List[str]:
        """Liste toutes les sauvegardes disponibles"""
        return [str(f) for f in self.saves_dir.glob("*.json")]
    
    def list_backlogs(self) -> List[str]:
        """Liste tous les backlogs disponibles"""
        return [str(f) for f in self.backlogs_dir.glob("*.json")]
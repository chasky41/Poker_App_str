"""
Système de jeu multijoueur en ligne pour Planning Poker
"""

import uuid
import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class OnlinePlayer:
    """Représente un joueur en ligne"""

    player_id: str
    name: str
    is_host: bool = False
    is_connected: bool = True
    current_vote: Optional[str] = None
    has_voted: bool = False
    last_seen: datetime = None

    def __post_init__(self):
        if self.last_seen is None:
            self.last_seen = datetime.now()


class GameRoom:
    """Gère une salle de jeu en ligne"""

    def __init__(self, room_id: str, host_name: str, game_mode: str = "strict"):
        self.room_id = room_id
        self.host_name = host_name
        self.game_mode = game_mode
        self.players: Dict[str, OnlinePlayer] = {}
        self.features: List[Dict] = []
        self.current_feature_index = 0
        self.game_started = False
        self.game_finished = False
        self.created_at = datetime.now()
        self.messages: List[Dict] = []

    def add_player(self, player_name: str, is_host: bool = False) -> str:
        """Ajoute un joueur à la salle"""
        player_id = str(uuid.uuid4())
        player = OnlinePlayer(player_id=player_id, name=player_name, is_host=is_host)
        self.players[player_id] = player
        return player_id

    def remove_player(self, player_id: str) -> bool:
        """Retire un joueur de la salle"""
        if player_id in self.players:
            del self.players[player_id]
            return True
        return False

    def player_vote(self, player_id: str, vote: str) -> bool:
        """Enregistre le vote d'un joueur"""
        if player_id in self.players:
            self.players[player_id].current_vote = vote
            self.players[player_id].has_voted = True
            return True
        return False

    def all_voted(self) -> bool:
        """Vérifie si tous les joueurs ont voté"""
        if not self.players or not self.game_started:
            return False
        return all(p.has_voted for p in self.players.values() if p.is_connected)

    def reset_votes(self) -> None:
        """Réinitialise les votes des joueurs"""
        for player in self.players.values():
            player.current_vote = None
            player.has_voted = False

    def get_votes(self) -> Dict[str, str]:
        """Retourne tous les votes actuels"""
        return {
            p.name: p.current_vote
            for p in self.players.values()
            if p.has_voted and p.is_connected
        }

    def add_feature(self, feature_data: Dict) -> None:
        """Ajoute une fonctionnalité"""
        self.features.append(feature_data)

    def get_current_feature(self) -> Optional[Dict]:
        """Retourne la fonctionnalité actuelle"""
        if self.current_feature_index < len(self.features):
            return self.features[self.current_feature_index]
        return None

    def next_feature(self) -> bool:
        """Passe à la fonctionnalité suivante"""
        if self.current_feature_index < len(self.features) - 1:
            self.current_feature_index += 1
            self.reset_votes()
            return True
        else:
            self.game_finished = True
            return False

    def add_message(self, player_name: str, message: str) -> None:
        """Ajoute un message au chat"""
        self.messages.append(
            {
                "player": player_name,
                "message": message,
                "timestamp": datetime.now().isoformat(),
            }
        )

    def get_connected_players(self) -> List[OnlinePlayer]:
        """Retourne les joueurs connectés"""
        return [p for p in self.players.values() if p.is_connected]

    def get_disconnected_players(self) -> List[OnlinePlayer]:
        """Retourne les joueurs déconnectés"""
        return [p for p in self.players.values() if not p.is_connected]

    def to_dict(self) -> Dict:
        """Convertit la salle en dictionnaire"""
        return {
            "room_id": self.room_id,
            "host_name": self.host_name,
            "game_mode": self.game_mode,
            "players": {pid: asdict(p) for pid, p in self.players.items()},
            "features": self.features,
            "current_feature_index": self.current_feature_index,
            "game_started": self.game_started,
            "game_finished": self.game_finished,
            "created_at": self.created_at.isoformat(),
            "messages": self.messages,
        }


class GameRoomManager:
    """Gère l'ensemble des salles de jeu"""

    def __init__(self):
        self.rooms: Dict[str, GameRoom] = {}

    def create_room(self, host_name: str, game_mode: str = "strict") -> str:
        """Crée une nouvelle salle"""
        room_id = self._generate_room_code()
        room = GameRoom(room_id, host_name, game_mode)
        # L'hôte est automatiquement ajouté
        room.add_player(host_name, is_host=True)
        self.rooms[room_id] = room
        return room_id

    def join_room(self, room_id: str, player_name: str) -> Optional[str]:
        """Joint un joueur à une salle"""
        if room_id in self.rooms:
            return self.rooms[room_id].add_player(player_name)
        return None

    def get_room(self, room_id: str) -> Optional[GameRoom]:
        """Récupère une salle par son ID"""
        return self.rooms.get(room_id)

    def room_exists(self, room_id: str) -> bool:
        """Vérifie si une salle existe"""
        return room_id in self.rooms

    def remove_room(self, room_id: str) -> bool:
        """Supprime une salle"""
        if room_id in self.rooms:
            del self.rooms[room_id]
            return True
        return False

    def list_rooms(self) -> List[Dict]:
        """Liste toutes les salles actives"""
        return [
            {
                "room_id": room.room_id,
                "host_name": room.host_name,
                "game_mode": room.game_mode,
                "player_count": len(room.get_connected_players()),
                "game_started": room.game_started,
                "created_at": room.created_at.isoformat(),
            }
            for room in self.rooms.values()
        ]

    @staticmethod
    def _generate_room_code() -> str:
        """Génère un code de salle unique"""
        import random
        import string

        return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


# Instance globale du gestionnaire de salles
game_room_manager = GameRoomManager()

"""
Tests unitaires pour les modèles
"""
import pytest
from src.models.player import Player
from src.models.feature import Feature
from src.models.game import Game

class TestPlayer:
    """Tests pour la classe Player"""
    
    def test_player_creation(self):
        player = Player("Alice", 1)
        assert player.name == "Alice"
        assert player.player_id == 1
        assert player.current_vote is None
        assert player.has_voted == False
    
    def test_player_vote(self):
        player = Player("Bob", 2)
        player.vote(5)
        assert player.current_vote == 5
        assert player.has_voted == True
    
    def test_player_reset_vote(self):
        player = Player("Charlie", 3)
        player.vote(8)
        player.reset_vote()
        assert player.current_vote is None
        assert player.has_voted == False
    
    def test_player_to_dict(self):
        player = Player("David", 4)
        player.vote(13)
        data = player.to_dict()
        assert data["name"] == "David"
        assert data["player_id"] == 4
        assert data["current_vote"] == 13
        assert data["has_voted"] == True
    
    def test_player_from_dict(self):
        data = {
            "name": "Eve",
            "player_id": 5,
            "current_vote": 3,
            "has_voted": True
        }
        player = Player.from_dict(data)
        assert player.name == "Eve"
        assert player.player_id == 5
        assert player.current_vote == 3
        assert player.has_voted == True

class TestFeature:
    """Tests pour la classe Feature"""
    
    def test_feature_creation(self):
        feature = Feature("Login system", "User authentication", 1)
        assert feature.name == "Login system"
        assert feature.description == "User authentication"
        assert feature.feature_id == 1
        assert feature.is_validated == False
        assert feature.estimated_difficulty is None
    
    def test_feature_add_vote_round(self):
        feature = Feature("Dashboard", "Main dashboard", 2)
        votes = {"Alice": 5, "Bob": 8}
        feature.add_vote_round(votes)
        assert feature.current_round == 1
        assert len(feature.vote_history) == 1
        assert feature.vote_history[0]["votes"] == votes
    
    def test_feature_validate(self):
        feature = Feature("API", "REST API", 3)
        feature.validate(13)
        assert feature.is_validated == True
        assert feature.estimated_difficulty == 13
    
    def test_feature_to_dict(self):
        feature = Feature("Export", "Data export", 4)
        feature.validate(5)
        data = feature.to_dict()
        assert data["name"] == "Export"
        assert data["description"] == "Data export"
        assert data["is_validated"] == True
        assert data["estimated_difficulty"] == 5
    
    def test_feature_from_dict(self):
        data = {
            "name": "Search",
            "description": "Advanced search",
            "feature_id": 5,
            "estimated_difficulty": 8,
            "is_validated": True,
            "vote_history": [],
            "current_round": 0
        }
        feature = Feature.from_dict(data)
        assert feature.name == "Search"
        assert feature.description == "Advanced search"
        assert feature.is_validated == True
        assert feature.estimated_difficulty == 8

class TestGame:
    """Tests pour la classe Game"""
    
    def setup_method(self):
        """Prépare les données de test"""
        self.players = [
            Player("Alice", 0),
            Player("Bob", 1),
            Player("Charlie", 2)
        ]
        self.features = [
            Feature("Feature 1", "Description 1", 0),
            Feature("Feature 2", "Description 2", 1)
        ]
    
    def test_game_creation(self):
        game = Game(self.players, self.features, "strict")
        assert len(game.players) == 3
        assert len(game.features) == 2
        assert game.voting_mode_name == "strict"
        assert game.current_feature_index == 0
        assert game.game_started == False
    
    def test_game_start(self):
        game = Game(self.players, self.features, "strict")
        game.start_game()
        assert game.game_started == True
        assert game.start_time is not None
    
    def test_get_current_feature(self):
        game = Game(self.players, self.features, "strict")
        current = game.get_current_feature()
        assert current == self.features[0]
    
    def test_get_progress(self):
        game = Game(self.players, self.features, "strict")
        progress = game.get_progress()
        assert progress["total"] == 2
        assert progress["completed"] == 0
        assert progress["current"] == 1
        assert progress["percentage"] == 0
    
    def test_next_feature(self):
        game = Game(self.players, self.features, "strict")
        game.next_feature()
        assert game.current_feature_index == 1
        assert game.game_finished == False
        
        game.next_feature()
        assert game.current_feature_index == 2
        assert game.game_finished == True
    
    def test_reset_player_votes(self):
        game = Game(self.players, self.features, "strict")
        self.players[0].vote(5)
        self.players[1].vote(8)
        
        game.reset_player_votes()
        
        assert all(not p.has_voted for p in game.players)
        assert all(p.current_vote is None for p in game.players)
    
    def test_process_votes_unanimity(self):
        game = Game(self.players, self.features, "strict")
        
        # Tous votent 5
        for player in game.players:
            player.vote(5)
        
        result = game.process_votes()
        
        assert result["validated"] == True
        assert result["difficulty"] == 5
        assert "validée" in result["message"]
    
    def test_process_votes_no_unanimity(self):
        game = Game(self.players, self.features, "strict")
        
        # Votes différents
        self.players[0].vote(5)
        self.players[1].vote(8)
        self.players[2].vote(13)
        
        result = game.process_votes()
        
        assert result["validated"] == False
        assert result["difficulty"] is None
    
    def test_process_votes_coffee_break(self):
        game = Game(self.players, self.features, "strict")
        
        # Tous votent café
        for player in game.players:
            player.vote("☕")
        
        result = game.process_votes()
        
        assert result["coffee_break"] == True
        assert result["validated"] == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
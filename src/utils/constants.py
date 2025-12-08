"""
Constantes pour l'application Planning Poker
"""

# Valeurs des cartes Planning Poker (suite de Fibonacci)
CARD_VALUES = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100, "?", "☕"]

# Cartes spéciales
SPECIAL_CARDS = {
    "?": "Point d'interrogation - Je ne sais pas",
    "☕": "Café - Pause nécessaire"
}

# Modes de vote disponibles
VOTING_MODES = {
    "strict": "Unanimité (Strict)",
    "average": "Moyenne",
    "median": "Médiane"
}

# Couleurs pour le design
COLORS = {
    "primary": "#FF6B6B",
    "secondary": "#4ECDC4",
    "success": "#95E1D3",
    "warning": "#FFE66D",
    "info": "#A8E6CF",
    "dark": "#2C3E50",
    "light": "#ECF0F1",
    "card_bg": "#FFFFFF",
    "card_border": "#E0E0E0",
    "card_selected": "#FFD93D"
}

# Emojis pour l'interface
EMOJIS = {
    "trophy": "🏆",
    "card": "🎴",
    "coffee": "☕",
    "check": "✅",
    "cross": "❌",
    "timer": "⏱️",
    "users": "👥",
    "save": "💾",
    "load": "📂",
    "stats": "📊",
    "settings": "⚙️"
}
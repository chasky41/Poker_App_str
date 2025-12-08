"""
Styles CSS personnalisés - Casino Universe Theme
Univers Casino Immersif avec Animations Réalistes de Cartes
"""


def get_custom_css():
    """Retourne le CSS personnalisé avec thème casino époustouflant"""
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Cinzel:wght@600;700&family=Orbitron:wght@400;700;900&display=swap');
    
    /* Variables globales - Univers Casino */
    :root {
        --poker-green: #0B5D3D;
        --poker-dark: #000000;
        --poker-red: #DC143C;
        --poker-blue: #003366;
        --poker-white: #FFFFFF;
        --poker-gold: #FFD700;
        --neon-purple: #9D00FF;
        --neon-cyan: #00FFFF;
        --neon-pink: #FF006E;
    }
    
    /* Animations Casino */
    @keyframes glow-pulse {
        0%, 100% { 
            text-shadow: 0 0 10px rgba(255,215,0,0.5), 
                        0 0 20px rgba(220,20,60,0.3);
        }
        50% { 
            text-shadow: 0 0 20px rgba(255,215,0,0.8), 
                        0 0 40px rgba(220,20,60,0.5),
                        0 0 60px rgba(157,0,255,0.3);
        }
    }
    
    @keyframes flip-card-reveal {
        0% { transform: rotateY(180deg); }
        50% { transform: rotateY(90deg); }
        100% { transform: rotateY(0deg); }
    }
    
    @keyframes card-float {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-20px) scale(1.05); }
    }
    
    @keyframes deal-card-animation {
        0% { 
            transform: translateX(-200%) rotateZ(-45deg) scale(0.5);
            opacity: 0;
        }
        50% { transform: translateX(-50%) rotateZ(-20deg) scale(0.9); }
        100% { 
            transform: translateX(0) rotateZ(0deg) scale(1);
            opacity: 1;
        }
    }
    
    @keyframes card-glow {
        0%, 100% { 
            box-shadow: 0 15px 50px rgba(255,215,0,0.3),
                       inset 0 1px 0 rgba(255,255,255,0.6),
                       0 0 30px rgba(220,20,60,0.2);
        }
        50% { 
            box-shadow: 0 20px 70px rgba(255,215,0,0.6),
                       inset 0 1px 0 rgba(255,255,255,0.8),
                       0 0 50px rgba(220,20,60,0.4),
                       0 0 80px rgba(157,0,255,0.3);
        }
    }
    
    @keyframes spin-360 {
        0% { transform: rotateY(0deg); }
        100% { transform: rotateY(360deg); }
    }
    
    @keyframes neon-flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
            text-shadow: 0 0 10px var(--poker-gold), 
                        0 0 20px var(--neon-pink),
                        0 0 30px var(--neon-cyan);
        }
        20%, 24%, 55% {
            text-shadow: 0 0 5px var(--poker-gold);
        }
    }
    
    @keyframes pulse {
        0%, 100% { 
            box-shadow: 0 0 10px currentColor;
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 0 20px currentColor;
            transform: scale(1.2);
        }
    }
    
    @keyframes fade-in-up {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slide-in-left {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes bounce-in {
        0% {
            opacity: 0;
            transform: scale(0.3);
        }
        50% {
            opacity: 1;
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            transform: scale(1);
        }
    }
    
    @keyframes shimmer {
        0% {
            background-position: -1000px 0;
        }
        100% {
            background-position: 1000px 0;
        }
    }
        }
    }
    
    /* Nouvelles animations pour table ronde */
    @keyframes table-fade-zoom {
        0% {
            opacity: 0;
            transform: scale(0.8);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes orbital-slide {
        0% {
            opacity: 0;
            transform: translateX(200px) translateY(100px) scale(0.6) rotateZ(-30deg);
        }
        50% {
            transform: translateX(100px) translateY(50px) scale(0.85) rotateZ(-15deg);
        }
        100% {
            opacity: 1;
            transform: translateX(0) translateY(0) scale(1) rotateZ(0deg);
        }
    }
    
    @keyframes orbital-slide-reverse {
        0% {
            opacity: 0;
            transform: translateX(-200px) translateY(100px) scale(0.6) rotateZ(30deg);
        }
        50% {
            transform: translateX(-100px) translateY(50px) scale(0.85) rotateZ(15deg);
        }
        100% {
            opacity: 1;
            transform: translateX(0) translateY(0) scale(1) rotateZ(0deg);
        }
    }
    
    @keyframes table-spotlight {
        0%, 100% {
            box-shadow: radial-gradient(ellipse at center, rgba(255,215,0,0.2) 0%, transparent 70%),
                       0 0 80px rgba(255,215,0,0.3),
                       inset 0 0 60px rgba(255,215,0,0.1);
        }
        50% {
            box-shadow: radial-gradient(ellipse at center, rgba(255,215,0,0.4) 0%, transparent 70%),
                       0 0 120px rgba(255,215,0,0.5),
                       inset 0 0 80px rgba(255,215,0,0.2);
        }
    }
    
    @keyframes card-hover-lift {
        0%, 100% {
            transform: translateY(0px) rotateX(0deg) rotateY(0deg);
        }
        50% {
            transform: translateY(-15px) rotateX(10deg) rotateY(-5deg);
        }
    }
    
    @keyframes border-glow-pulse {
        0%, 100% {
            border-color: var(--poker-gold);
            box-shadow: 0 0 20px rgba(255,215,0,0.3),
                       0 0 40px rgba(220,20,60,0.2);
        }
        50% {
            border-color: var(--neon-pink);
            box-shadow: 0 0 40px rgba(255,215,0,0.6),
                       0 0 80px rgba(220,20,60,0.4),
                       0 0 120px rgba(157,0,255,0.3);
        }
    }
    
    @keyframes flip-3d-select {
        0% {
            transform: rotateY(0deg) rotateX(0deg) scale(1);
        }
        50% {
            transform: rotateY(90deg) rotateX(10deg) scale(1.1);
        }
        100% {
            transform: rotateY(360deg) rotateX(0deg) scale(1.15);
        }
    }
    
    @keyframes shadow-down {
        0% {
            box-shadow: 0 5px 15px rgba(0,0,0,0.2),
                       0 0 20px rgba(255,215,0,0.2);
        }
        100% {
            box-shadow: 0 20px 50px rgba(0,0,0,0.5),
                       0 0 40px rgba(255,215,0,0.4),
                       0 0 80px rgba(220,20,60,0.3);
        }
    }
    
    /* Style général - Univers Casino */
    .stApp {
        font-family: 'Cinzel', 'Poppins', sans-serif;
        background: radial-gradient(ellipse at center, #1a1a2e 0%, #0f0f1e 50%, #000000 100%);
        background-attachment: fixed;
        color: #FFFFFF;
    }
    
    /* Transitions fluides globales */
    * {
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    /* Animations d'entrée pour les éléments */
    .stButton > button {
        animation: fade-in-up 0.5s ease-out;
    }
    
    .stColumn {
        animation: slide-in-left 0.6s ease-out;
    }
    
    .main-container {
        animation: bounce-in 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    /* Effets hover sur les boutons */
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 10px 25px rgba(255,215,0,0.4), 
                   0 0 30px rgba(220,20,60,0.3);
        filter: brightness(1.1);
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98);
        filter: brightness(0.95);
    }
    
    /* Transitions pour les inputs */
    .stTextInput input,
    .stSelectbox select,
    .stNumberInput input {
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        border-color: var(--poker-gold) !important;
    }
    
    .stTextInput input:focus,
    .stSelectbox select:focus,
    .stNumberInput input:focus {
        box-shadow: 0 0 20px rgba(255,215,0,0.6),
                   inset 0 0 10px rgba(255,215,0,0.2) !important;
        transform: scale(1.02);
    }
    
    /* Smooth page transitions */
    .stMarkdown {
        animation: fade-in-up 0.5s ease-out;
    }
    
    /* Effet shimmer sur les textes spéciaux */
    .shimmer-text {
        animation: shimmer 3s infinite;
        background: linear-gradient(90deg, transparent, rgba(255,215,0,0.3), transparent);
        background-size: 1000px 100%;
    }
    
    /* Headers - Style Casino Lumineux */
    h1, h2, h3 {
        font-family: 'Orbitron', 'Cinzel', serif;
        font-weight: 900;
        color: var(--poker-gold);
        text-shadow: 0 0 20px rgba(255,215,0,0.8),
                    0 0 40px rgba(220,20,60,0.5),
                    0 0 60px rgba(157,0,255,0.3),
                    2px 2px 4px rgba(0,0,0,0.9);
        letter-spacing: 3px;
        animation: glow-pulse 3s ease-in-out infinite;
    }
    
    h1 {
        font-size: 3.5em;
        text-transform: uppercase;
        animation: neon-flicker 3s infinite;
    }
    
    /* Cartes de jeu - Style Poker Réaliste */
    .poker-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8F8F8 100%);
        border-radius: 15px;
        padding: 0;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        cursor: pointer;
        border: 3px solid var(--poker-dark);
        width: 140px;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5), 
                   inset 0 1px 0 rgba(255,255,255,0.9);
        animation: deal-card-animation 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards,
                   card-float 3s ease-in-out infinite 0.8s;
        transform-style: preserve-3d;
        perspective: 1000px;
    }
    
    /* Valeur de la carte (grand nombre au centre) */
    .card-value {
        font-size: 72px;
        font-weight: 900;
        color: var(--poker-dark);
        font-family: 'Orbitron', 'Cinzel', serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.15);
        margin: 0;
        z-index: 2;
        line-height: 1;
    }
    
    /* Hover - Carte survolée */
    .poker-card:hover {
        transform: translateY(-20px) scale(1.12) rotateX(5deg) rotateY(-5deg);
        box-shadow: 0 25px 70px rgba(0,0,0,0.6),
                   inset 0 1px 0 rgba(255,255,255,0.95),
                   0 0 40px rgba(255,215,0,0.5),
                   0 0 80px rgba(220,20,60,0.25);
        border-color: var(--poker-gold);
    }
    
    /* Sélection - Carte choisie */
    .poker-card.selected {
        background: linear-gradient(135deg, var(--poker-gold) 0%, #FFB700 100%);
        border: 4px solid var(--neon-pink);
        transform: translateY(-25px) scale(1.18);
        box-shadow: 0 30px 90px rgba(0,0,0,0.7),
                   inset 0 1px 0 rgba(255,255,255,0.95),
                   0 0 50px rgba(255,215,0,0.7),
                   0 0 100px rgba(220,20,60,0.5),
                   0 0 150px rgba(157,0,255,0.3);
    }
    
    .poker-card.selected .card-value {
        color: var(--poker-red);
        text-shadow: 0 0 20px rgba(220,20,60,0.8),
                    0 0 40px rgba(157,0,255,0.4),
                    2px 2px 4px rgba(0,0,0,0.2);
        animation: neon-flicker 2s infinite;
    }
    
    /* Conteneurs - Table Poker Luminescente */
    .main-container {
        background: linear-gradient(135deg, rgba(11, 93, 61, 0.15) 0%, rgba(0, 51, 102, 0.15) 100%);
        border: 3px solid var(--poker-gold);
        border-radius: 20px;
        padding: 35px;
        margin: 20px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.4), 
                   inset 0 0 30px rgba(255,215,0,0.08),
                   0 0 20px rgba(220,20,60,0.2);
        backdrop-filter: blur(10px);
        color: var(--poker-white);
        position: relative;
        overflow: hidden;
    }
    
    .main-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,215,0,0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    /* Boutons - Style Poker Neon */
    .stButton>button {
        background: linear-gradient(135deg, var(--poker-red) 0%, #8B0000 100%);
        color: white;
        border: 3px solid var(--poker-gold);
        border-radius: 25px;
        padding: 14px 35px;
        font-weight: 700;
        font-size: 16px;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 8px 20px rgba(220,20,60,0.4),
                   0 0 20px rgba(255,215,0,0.2);
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 40px rgba(220,20,60,0.6),
                   0 0 40px rgba(255,215,0,0.4),
                   inset 0 0 20px rgba(157,0,255,0.2);
        border-color: var(--neon-cyan);
        background: linear-gradient(135deg, #FF1744 0%, #C41C3B 100%);
    }
    
    .stButton>button:hover::before {
        left: 100%;
    }
    
    /* Progress bar - Animation Gradient */
    .progress-container {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 25px;
        padding: 6px;
        margin: 20px 0;
        border: 2px solid var(--poker-gold);
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.3), 
                   0 0 15px rgba(255,215,0,0.2);
    }
    
    .progress-bar {
        background: linear-gradient(90deg, var(--poker-gold) 0%, var(--poker-red) 50%, var(--poker-gold) 100%);
        background-size: 200% 100%;
        height: 35px;
        border-radius: 20px;
        transition: width 0.5s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--poker-dark);
        font-weight: 700;
        font-size: 13px;
        text-shadow: 0 0 3px rgba(255,255,255,0.5);
        box-shadow: 0 0 20px rgba(255,215,0,0.5),
                   inset 0 1px 0 rgba(255,255,255,0.3);
        animation: gradient-shift 2s ease infinite;
    }
    
    @keyframes gradient-shift {
        0%, 100% { background-position: 0% center; }
        50% { background-position: 100% center; }
    }
    }
    
    /* Feature card */
    .feature-card {
        background: linear-gradient(135deg, rgba(11, 93, 61, 0.2) 0%, rgba(0, 51, 102, 0.2) 100%);
        border-left: 6px solid var(--poker-gold);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,215,0,0.2);
        color: var(--poker-white);
    }
    
    .feature-card h3 {
        color: var(--poker-gold);
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Player badges */
    .player-badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--poker-red) 0%, #8B0000 100%);
        color: white;
        padding: 10px 25px;
        border-radius: 25px;
        margin: 8px;
        font-weight: 700;
        box-shadow: 0 5px 15px rgba(220,20,60,0.4);
        border: 2px solid var(--poker-gold);
        text-transform: uppercase;
        font-size: 12px;
        letter-spacing: 1px;
    }
    
    .player-badge.voted {
        background: linear-gradient(135deg, #0B5D3D 0%, #006633 100%);
        color: var(--poker-gold);
        border-color: var(--poker-gold);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes dealCard {
        0% { transform: translateX(-100%) rotate(-45deg); opacity: 0; }
        100% { transform: translateX(0) rotate(0); opacity: 1; }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    .deal-card {
        animation: dealCard 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    /* Results table */
    .results-table {
        background: linear-gradient(135deg, rgba(11, 93, 61, 0.2) 0%, rgba(0, 51, 102, 0.2) 100%);
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        border: 2px solid var(--poker-gold);
        color: var(--poker-white);
    }
    
    /* Metrics */
    .metric-card {
        background: linear-gradient(135deg, var(--poker-red) 0%, #8B0000 100%);
        color: var(--poker-white);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(220,20,60,0.4);
        border: 3px solid var(--poker-gold);
    }
    
    .metric-value {
        font-size: 42px;
        font-weight: 700;
        margin: 15px 0;
        color: var(--poker-gold);
        font-family: 'Cinzel', serif;
    }
    
    .metric-label {
        font-size: 14px;
        opacity: 0.95;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(135deg, #0B5D3D 0%, #000000 100%);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, var(--poker-blue) 0%, #000033 100%);
        color: var(--poker-white);
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        border-left: 6px solid var(--poker-gold);
    }
    
    .success-box {
        background: linear-gradient(135deg, #0B5D3D 0%, #006633 100%);
        border-left-color: var(--poker-gold);
    }
    
    .warning-box {
        background: linear-gradient(135deg, var(--poker-red) 0%, #8B0000 100%);
        color: var(--poker-white);
        border-left-color: var(--poker-gold);
    }
    
    .error-box {
        background: linear-gradient(135deg, #8B0000 0%, #660000 100%);
        border-left-color: #FF4444;
    }
    
    /* Timer */
    .timer-display {
        background: linear-gradient(135deg, var(--poker-gold) 0%, #FFB700 100%);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px 40px;
        font-size: 28px;
        font-weight: 700;
        color: var(--poker-dark);
        text-align: center;
        box-shadow: 0 8px 25px rgba(255,215,0,0.4);
        border: 3px solid var(--poker-dark);
        font-family: 'Cinzel', serif;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Online Game Elements */
    .online-player {
        background: linear-gradient(135deg, rgba(11, 93, 61, 0.3) 0%, rgba(0, 51, 102, 0.3) 100%);
        border: 2px solid var(--poker-gold);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        color: var(--poker-white);
        text-align: center;
        box-shadow: 0 5px 15px rgba(255,215,0,0.1);
    }
    
    .online-player.active {
        border-color: var(--poker-green);
        background: linear-gradient(135deg, rgba(11, 93, 61, 0.5) 0%, rgba(0, 51, 102, 0.5) 100%);
        box-shadow: 0 0 20px rgba(11, 93, 61, 0.6);
    }
    
    .online-player.voted {
        border-color: var(--poker-gold);
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 215, 0, 0.05) 100%);
    }
    
    .player-status {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .player-status.online {
        background-color: #00FF00;
        box-shadow: 0 0 10px #00FF00;
    }
    
    .player-status.offline {
        background-color: #999999;
    }
    
    .player-status.voting {
        background-color: var(--poker-gold);
        animation: pulse 1.5s infinite;
    }
    
    /* Game Room */
    .game-room {
        background: linear-gradient(135deg, rgba(11, 93, 61, 0.1) 0%, rgba(0, 51, 102, 0.1) 100%);
        border: 3px solid var(--poker-gold);
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: inset 0 0 30px rgba(11, 93, 61, 0.1), 0 15px 50px rgba(0,0,0,0.4);
        position: relative;
    }
    
    .game-room::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        border: 1px solid rgba(255, 215, 0, 0.1);
        border-radius: 20px;
        pointer-events: none;
    }
    
    /* Connection Status */
    .connection-status {
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #0B5D3D 0%, #000000 100%);
        color: var(--poker-white);
        padding: 15px 25px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        border: 2px solid var(--poker-gold);
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 10px;
        z-index: 1000;
    }
    
    .connection-status.connected::before {
        content: '';
        width: 12px;
        height: 12px;
        background-color: #00FF00;
        border-radius: 50%;
        box-shadow: 0 0 10px #00FF00;
    }
    
    /* Chat/Messages */
    .message-box {
        background: linear-gradient(135deg, rgba(0, 51, 102, 0.3) 0%, rgba(11, 93, 61, 0.3) 100%);
        border-left: 4px solid var(--poker-gold);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        color: var(--poker-white);
        box-shadow: 0 3px 10px rgba(0,0,0,0.2);
    }
    
    </style>
    """

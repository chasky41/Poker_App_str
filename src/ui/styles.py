"""
Styles CSS personnalisés pour l'application
"""

def get_custom_css():
    """Retourne le CSS personnalisé pour l'application"""
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Variables globales */
    :root {
        --primary-color: #FF6B6B;
        --secondary-color: #4ECDC4;
        --success-color: #95E1D3;
        --warning-color: #FFE66D;
        --dark-color: #2C3E50;
        --light-color: #ECF0F1;
        --card-bg: #FFFFFF;
        --card-border: #E0E0E0;
        --card-selected: #FFD93D;
        --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    /* Style général */
    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Cartes de jeu */
    .poker-card {
        background: white;
        border-radius: 15px;
        padding: 30px 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        cursor: pointer;
        border: 3px solid transparent;
        min-height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .poker-card:hover {
        transform: translateY(-10px) scale(1.05);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        border-color: var(--primary-color);
    }
    
    .poker-card.selected {
        background: var(--gradient-2);
        color: white;
        border-color: var(--card-selected);
        transform: translateY(-15px) scale(1.1);
    }
    
    .card-value {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .card-label {
        font-size: 14px;
        opacity: 0.8;
    }
    
    /* Conteneurs */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    /* Boutons */
    .stButton>button {
        background: var(--gradient-1);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    
    /* Progress bar */
    .progress-container {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 25px;
        padding: 5px;
        margin: 20px 0;
    }
    
    .progress-bar {
        background: var(--gradient-3);
        height: 30px;
        border-radius: 20px;
        transition: width 0.5s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
    }
    
    /* Feature card */
    .feature-card {
        background: white;
        border-left: 5px solid var(--primary-color);
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .feature-card h3 {
        color: var(--dark-color);
        margin-bottom: 10px;
        text-shadow: none;
    }
    
    /* Player badges */
    .player-badge {
        display: inline-block;
        background: var(--gradient-1);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        margin: 5px;
        font-weight: 600;
        box-shadow: 0 3px 10px rgba(0,0,0,0.2);
    }
    
    .player-badge.voted {
        background: var(--success-color);
        color: var(--dark-color);
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
    
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    /* Results table */
    .results-table {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Metrics */
    .metric-card {
        background: var(--gradient-3);
        color: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .metric-value {
        font-size: 36px;
        font-weight: 700;
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 14px;
        opacity: 0.9;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.95);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .success-box {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #FFE66D 0%, #FFA000 100%);
        color: #333;
    }
    
    .error-box {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
    }
    
    /* Timer */
    .timer-display {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 15px 30px;
        font-size: 24px;
        font-weight: 700;
        color: white;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    </style>
    """
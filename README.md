# 🎴 Planning Poker - Application Streamlit

Application web interactive pour réaliser des sessions de Planning Poker en équipe, développée avec Streamlit.

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Table des matières

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Architecture](#architecture)
- [Tests](#tests)
- [Intégration Continue](#intégration-continue)
- [Contribuer](#contribuer)

## 🎯 Présentation

Le Planning Poker est une technique d'estimation collaborative utilisée dans les méthodes agiles. Cette application permet à des équipes de réaliser des sessions d'estimation de manière efficace et ludique.

### Modes de jeu supportés

- **🎯 Strict (Unanimité)** : Tous les joueurs doivent voter la même valeur
- **📊 Moyenne** : Après le premier tour, la moyenne des votes est calculée
- **📈 Médiane** : Après le premier tour, la médiane des votes est retenue

## ✨ Fonctionnalités

### Fonctionnalités principales

- ✅ Configuration flexible du nombre de joueurs (2-10)
- ✅ Import de backlog au format JSON
- ✅ Création manuelle de fonctionnalités
- ✅ 3 modes de vote différents
- ✅ Cartes spéciales (? et ☕)
- ✅ Sauvegarde automatique en cas de pause café
- ✅ Export des résultats au format JSON
- ✅ Interface moderne et responsive
- ✅ Chronomètre intégré
- ✅ Barre de progression
- ✅ Historique des votes par feature

### Fonctionnalités avancées

- 🎨 Design moderne avec animations CSS
- 📊 Statistiques détaillées en fin de partie
- 💾 Système de sauvegarde/chargement
- 🔄 Gestion complète des tours de vote
- 📈 Visualisation de la progression

## 🚀 Installation

### Prérequis

- Python 3.9 ou supérieur
- pip

### Installation pas à pas

1. **Cloner le repository**

```bash
git clone https://github.com/votre-username/planning_str.git
cd planning_str
```

2. **Créer un environnement virtuel**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Créer les dossiers nécessaires**

```bash
mkdir -p data/backlogs data/saves data/results
```

## 💻 Utilisation

### Lancer l'application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

### Workflow typique

1. **Page d'accueil** : Choisir entre nouvelle partie ou charger une sauvegarde
2. **Configuration** : 
   - Définir les joueurs
   - Choisir le mode de vote
   - Charger ou créer le backlog
3. **Jeu** :
   - Chaque joueur vote à tour de rôle (mode local)
   - Révéler les votes
   - Discuter si nécessaire
   - Valider ou revoter
4. **Résultats** : Consulter les estimations et exporter

### Format du backlog JSON

```json
{
  "backlog": [
    {
      "name": "Nom de la feature",
      "description": "Description détaillée"
    }
  ]
}
```

### Format de sauvegarde

Les sauvegardes contiennent :
- L'état complet de la partie
- Les joueurs et leurs votes
- Les features et leur progression
- Le mode de vote utilisé

## 🏗️ Architecture

### Structure du projet

```
planing_str/
├── app.py                      # Application principale
├── src/
│   ├── models/                 # Modèles de données
│   │   ├── player.py
│   │   ├── feature.py
│   │   └── game.py
│   ├── voting_modes/           # Modes de vote
│   │   ├── base_mode.py
│   │   ├── strict_mode.py
│   │   ├── average_mode.py
│   │   └── median_mode.py
│   ├── utils/                  # Utilitaires
│   │   ├── constants.py
│   │   └── json_handler.py
│   └── ui/                     # Interface
│       └── styles.py
├── data/                       # Données
├── tests/                      # Tests unitaires
└── docs/                       # Documentation
```

### Diagramme de classes

```
Game
├── players: List[Player]
├── features: List[Feature]
├── voting_mode: VotingMode
└── current_feature_index: int

Player
├── name: str
├── player_id: int
├── current_vote: Any
└── has_voted: bool

Feature
├── name: str
├── description: str
├── estimated_difficulty: float
├── is_validated: bool
└── vote_history: List[dict]

VotingMode (Abstract)
├── StrictMode
├── AverageMode
└── MedianMode
```

## 🧪 Tests

### Lancer les tests

```bash
# Tous les tests
pytest tests/ -v

# Avec couverture
pytest tests/ --cov=src --cov-report=html

# Tests spécifiques
pytest tests/test_models.py -v
```

### Couverture de code

Les tests couvrent :
- ✅ Modèles de données (Player, Feature, Game)
- ✅ Modes de vote
- ✅ Gestionnaire JSON
- ✅ Logique métier

Objectif de couverture : **> 80%**

## 🔄 Intégration Continue

L'intégration continue est mise en place avec **GitHub Actions**.

### Pipelines CI/CD

1. **Tests** : Exécution automatique sur Python 3.9, 3.10, 3.11
2. **Linting** : Vérification du code avec Black, isort, flake8
3. **Documentation** : Génération automatique avec Sphinx
4. **Sécurité** : Analyse avec Safety et Bandit

### Badges de statut

Les badges CI/CD apparaissent sur le README et indiquent :
- ✅ Statut des tests
- ✅ Couverture de code
- ✅ Qualité du code

## 📊 Modes de vote détaillés

### Mode Strict (Unanimité)

- **Tour 1 et suivants** : Unanimité requise
- **Validation** : Tous les joueurs votent la même valeur
- **Idéal pour** : Équipes petites, features critiques

### Mode Moyenne

- **Tour 1** : Unanimité requise
- **Tours suivants** : Moyenne des votes, arrondie à la valeur Fibonacci la plus proche
- **Idéal pour** : Équipes moyennes, compromis rapide

### Mode Médiane

- **Tour 1** : Unanimité requise
- **Tours suivants** : Médiane des votes, arrondie à la valeur Fibonacci la plus proche
- **Idéal pour** : Éviter l'influence des valeurs extrêmes

## 🎴 Cartes disponibles

- **Numériques** : 0, 1, 2, 3, 5, 8, 13, 20, 40, 100 (suite de Fibonacci)
- **Spéciales** :
  - **?** : Je ne sais pas / besoin d'information
  - **☕** : Pause café nécessaire (sauvegarde automatique)

## 📝 Licence

MIT License - voir le fichier LICENSE pour plus de détails.

## 👥 Auteurs

- Votre Nom - Développement initial

## 🙏 Remerciements

- Streamlit pour le framework
- La communauté Agile pour la méthodologie Planning Poker

---

**Note** : Cette application a été développée dans le cadre d'un projet académique sur les méthodes agiles et l'intégration continue.
# -*- coding: utf-8 -*-
"""
Application Planning Poker avec Streamlit - Mode Poker Réaliste
"""

import streamlit as st
import json
from pathlib import Path
import time
from datetime import datetime

# Imports des modules
from src.models.player import Player
from src.models.feature import Feature
from src.models.game import Game
from src.utils.constants import CARD_VALUES, VOTING_MODES, COLORS, EMOJIS
from src.utils.json_handler import JSONHandler
from src.ui.styles import get_custom_css
from src.online.multiplayer import game_room_manager, GameRoom

# Configuration de la page
st.set_page_config(
    page_title="Planning Poker - Poker Edition",
    page_icon="🎴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Injection du CSS personnalisé
st.markdown(get_custom_css(), unsafe_allow_html=True)


# Sidebar - About / Contributors
st.sidebar.markdown("## ℹ️ À propos")

with st.sidebar.expander("📌 Projet Planning Poker"):
    st.markdown("""
    **Planning Poker** est une application développée dans le cadre du module *Méthodes Agiles*.

    🎯 **Objectif**  
    Faciliter les séances d’estimation collaborative en équipe agile.

    🧩 **Méthodologie**  
    - Travail collaboratif  
    - Estimation collective  
    - Amélioration continue
    """)

with st.sidebar.expander("👥 Contributeurs"):
    st.markdown("""
    - **Charaf** – Architecture du projet & logique métier principale  
    - **Mohamed** – Développement du chronomètre de la partie  
    - **Hamza Meksem** – Section “À propos” + documentation & amélioration UX
    """)




# Initialisation du gestionnaire JSON
json_handler = JSONHandler()


# ========== SESSION STATE ==========
def init_session_state():
    """Initialise les variables de session"""
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "game" not in st.session_state:
        st.session_state.game = None
    if "players" not in st.session_state:
        st.session_state.players = []
    if "features" not in st.session_state:
        st.session_state.features = []
    if "voting_mode" not in st.session_state:
        st.session_state.voting_mode = "strict"
    if "timer_start" not in st.session_state:
        st.session_state.timer_start = None
    if "game_mode" not in st.session_state:
        st.session_state.game_mode = "local"
    if "room_id" not in st.session_state:
        st.session_state.room_id = None
    if "player_id" not in st.session_state:
        st.session_state.player_id = None
    if "player_name" not in st.session_state:
        st.session_state.player_name = None
    if "online_game" not in st.session_state:
        st.session_state.online_game = None


init_session_state()


# ========== FONCTIONS UTILITAIRES ==========
def create_card_html(value, is_selected=False, player_name=None):
    """Crée le HTML pour une carte de poker avec symboles"""
    selected_class = "selected" if is_selected else ""
    display_value = value if value not in ["?", "☕"] else value

    card_html = f"""
    <div class="poker-card {selected_class}">
        <div class="card-value">{display_value}</div>
    </div>
    """
    return card_html


def create_premium_card_html(value, is_selected=False):
    """Crée le HTML pour une carte premium autour de la table ronde"""
    selected_class = "selected" if is_selected else ""
    display_value = value if value not in ["?", "☕"] else value
    label_text = (
        "Break" if value == "☕" else ("?" if value == "?" else f"Points: {value}")
    )

    card_html = f"""
    <div class="card-premium {selected_class}">
        <div class="card-premium-value">{display_value}</div>
        <div class="card-premium-label">{label_text}</div>
    </div>
    """
    return card_html


def show_progress_bar(current, total, percentage):
    """Affiche une barre de progression stylée"""
    st.markdown(
        f"""
    <div class="progress-container">
        <div class="progress-bar" style="width: {percentage}%;">
            {current}/{total} - {percentage:.0f}%
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def show_metric_card(value, label, icon="📊"):
    """Affiche une carte métrique"""
    st.markdown(
        f"""
    <div class="metric-card">
        <div style="font-size: 24px;">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ========== PAGE HOME ==========
def show_home_page():
    """Page d'accueil avec options poker réaliste"""
    st.markdown(
        "<h1 style='text-align: center;'>🎴 PLANNING POKER 🎴</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center; color: #FFD700;'>Un vrai jeu de poker pour estimer vos features</h3>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)

        st.markdown("### 🎯 Mode de Jeu")
        st.write("Choisissez comment vous voulez jouer au Planning Poker!")

        st.markdown("---")

        # Onglets pour les modes de jeu
        tab1, tab2 = st.tabs(["🖥️ Local", "🌐 En Ligne"])

        with tab1:
            st.markdown("### Jeu en Local")
            st.write("Parfait pour jouer avec votre équipe dans la même salle")

            if st.button(
                "🎮 Nouvelle Partie Locale", use_container_width=True, key="new_local"
            ):
                st.session_state.page = "setup"
                st.session_state.game_mode = "local"
                st.rerun()

            if st.button(
                "📂 Charger une Partie", use_container_width=True, key="load_local"
            ):
                st.session_state.page = "load"
                st.session_state.game_mode = "local"
                st.rerun()

        with tab2:
            st.markdown("### Jeu En Ligne")
            st.write("Jouez avec vos collègues à distance - temps réel!")

            col_create, col_join = st.columns(2)

            with col_create:
                if st.button(
                    "🆕 Créer une Salle", use_container_width=True, key="create_online"
                ):
                    st.session_state.page = "online_create"
                    st.session_state.game_mode = "online"
                    st.rerun()

            with col_join:
                if st.button(
                    "🔗 Rejoindre une Salle",
                    use_container_width=True,
                    key="join_online",
                ):
                    st.session_state.page = "online_join"
                    st.session_state.game_mode = "online"
                    st.rerun()

        st.markdown("---")

        # Règles rapides
        with st.expander("📖 Comment jouer ?"):
            st.markdown(
                """
            **Règles du Planning Poker :**
            
            1. **Configuration** : Définissez les joueurs et le mode de vote
            2. **Backlog** : Chargez votre liste de fonctionnalités
            3. **Vote** : Chaque joueur choisit une carte secrètement
            4. **Révélation** : Les cartes sont révélées simultanément
            5. **Discussion** : Si pas d'accord, discutez et revotez
            6. **Validation** : La feature est estimée selon le mode choisi
            
            **Modes de vote disponibles :**
            - 🎯 **Strict** : Unanimité requise
            - 📊 **Moyenne** : Moyenne des votes (après 1er tour)
            - 📈 **Médiane** : Médiane des votes (après 1er tour)
            
            **Cartes spéciales :**
            - ❓ **?** : Je ne sais pas / besoin d'info
            - ☕ **Café** : Pause nécessaire
            """
            )

        st.markdown("</div>", unsafe_allow_html=True)


# ========== PAGE SETUP ==========
def show_setup_page():
    """Page de configuration de la partie"""
    st.markdown(
        "<h1 style='text-align: center;'>⚙️ Configuration de la Partie</h1>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        st.markdown("### 👥 Joueurs")

        # Nombre de joueurs
        num_players = st.number_input(
            "Nombre de joueurs", min_value=2, max_value=10, value=3
        )

        # Noms des joueurs
        player_names = []
        for i in range(num_players):
            name = st.text_input(
                f"Joueur {i+1}", value=f"Joueur {i+1}", key=f"player_{i}"
            )
            player_names.append(name)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        st.markdown("### 🎲 Paramètres")

        # Mode de vote
        voting_mode = st.selectbox(
            "Mode de vote",
            options=list(VOTING_MODES.keys()),
            format_func=lambda x: VOTING_MODES[x],
        )

        st.info(
            f"""
        **Mode sélectionné : {VOTING_MODES[voting_mode]}**
        
        {
            'Tous les joueurs doivent voter la même valeur.' if voting_mode == 'strict'
            else 'Premier tour : unanimité. Tours suivants : moyenne des votes.'
            if voting_mode == 'average'
            else 'Premier tour : unanimité. Tours suivants : médiane des votes.'
        }
        """
        )

        st.markdown("---")

        # Backlog
        st.markdown("### 📋 Backlog")

        upload_option = st.radio(
            "Comment charger le backlog ?",
            ["Uploader un fichier JSON", "Créer manuellement"],
        )

        features = []

        if upload_option == "Uploader un fichier JSON":
            uploaded_file = st.file_uploader("Choisir un fichier JSON", type=["json"])

            if uploaded_file:
                try:
                    backlog_data = json.load(uploaded_file)
                    features_data = backlog_data.get("backlog", [])
                    for idx, f in enumerate(features_data):
                        features.append(
                            Feature(
                                name=f.get("name", f"Feature {idx+1}"),
                                description=f.get("description", ""),
                                feature_id=idx,
                            )
                        )
                    st.success(f"✅ {len(features)} fonctionnalités chargées")
                except Exception as e:
                    st.error(f"❌ Erreur : {str(e)}")
        else:
            num_features = st.number_input(
                "Nombre de fonctionnalités", min_value=1, max_value=20, value=3
            )

            for i in range(num_features):
                with st.expander(f"Feature {i+1}"):
                    f_name = st.text_input(
                        f"Nom", value=f"Feature {i+1}", key=f"feat_name_{i}"
                    )
                    f_desc = st.text_area(
                        f"Description", value="", key=f"feat_desc_{i}"
                    )
                    features.append(
                        Feature(name=f_name, description=f_desc, feature_id=i)
                    )

        st.markdown("</div>", unsafe_allow_html=True)

    # Boutons de navigation
    col_back, col_start = st.columns([1, 1])

    with col_back:
        if st.button("← Retour", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

    with col_start:
        if st.button("🎮 Démarrer la Partie", use_container_width=True, type="primary"):
            if len(features) == 0:
                st.error("❌ Veuillez ajouter au moins une fonctionnalité !")
            else:
                # Créer les joueurs
                players = [
                    Player(name=name, player_id=idx)
                    for idx, name in enumerate(player_names)
                ]

                # Créer la partie
                st.session_state.game = Game(players, features, voting_mode)
                st.session_state.game.start_game()
                st.session_state.page = "game"
                st.session_state.timer_start = time.time()
                st.rerun()


# Suite dans le prochain artifact...


# ========== PAGE GAME (Suite de app.py) ==========
def show_game_page():
    """Page de jeu principale"""
    game = st.session_state.game

    if not game:
        st.error("❌ Aucune partie en cours")
        if st.button("← Retour à l'accueil"):
            st.session_state.page = "home"
            st.rerun()
        return

    # Header avec timer et progression
    col_timer, col_progress = st.columns([1, 3])

    with col_timer:
        if st.session_state.timer_start:
            elapsed = int(time.time() - st.session_state.timer_start)
            minutes = elapsed // 60
            seconds = elapsed % 60
            st.markdown(
                f"""
            <div class="timer-display">
                ⏱️ {minutes:02d}:{seconds:02d}
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col_progress:
        progress = game.get_progress()
        show_progress_bar(
            progress["completed"], progress["total"], progress["percentage"]
        )

    # Vérifier si la partie est terminée
    if game.game_finished:
        show_results_page()
        return

    # Feature actuelle
    current_feature = game.get_current_feature()

    if not current_feature:
        st.error("❌ Aucune feature disponible")
        return

    # Afficher la feature
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown(f"### 🎯 Feature Actuelle : {current_feature.name}")

    if current_feature.description:
        st.info(f"📝 {current_feature.description}")

    st.markdown(f"**Tour de vote : {current_feature.current_round + 1}**")
    st.markdown("</div>", unsafe_allow_html=True)

    # Zone de vote avec table ronde de casino
    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center; color: white;'>🎴 Choisissez Votre Carte</h2>",
        unsafe_allow_html=True,
    )

    # Afficher les cartes en grille simple mais stylisée
    cols_per_row = 6
    card_rows = [
        CARD_VALUES[i : i + cols_per_row]
        for i in range(0, len(CARD_VALUES), cols_per_row)
    ]

    for row in card_rows:
        cols = st.columns(len(row))
        for idx, (col, card_value) in enumerate(zip(cols, row)):
            with col:
                # Bouton pour chaque carte
                card_key = f"card_{card_value}"
                if st.button(str(card_value), key=card_key, use_container_width=True):
                    # Enregistrer le vote du joueur actuel
                    player_selection = st.session_state.get("current_player", 0)
                    if player_selection < len(game.players):
                        game.players[player_selection].vote(card_value)

                        # Passer au joueur suivant ou valider
                        if player_selection < len(game.players) - 1:
                            st.session_state["current_player"] = player_selection + 1
                        else:
                            st.session_state["current_player"] = 0

                        st.rerun()

    st.markdown("---")

    # Sélection du joueur (mode local)
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("### 👤 Joueur actuel")

    current_player_idx = st.session_state.get("current_player", 0)

    player_options = [f"{p.name} {'✅' if p.has_voted else '⏳'}" for p in game.players]
    selected_player = st.selectbox(
        "Sélectionnez le joueur",
        options=range(len(game.players)),
        format_func=lambda x: player_options[x],
        index=current_player_idx,
    )
    st.session_state["current_player"] = selected_player

    # Afficher qui a voté
    st.markdown("### 📊 Statut des votes")
    vote_cols = st.columns(len(game.players))

    for idx, (col, player) in enumerate(zip(vote_cols, game.players)):
        with col:
            status = "✅ A voté" if player.has_voted else "⏳ En attente"
            color = "success-box" if player.has_voted else "warning-box"
            st.markdown(
                f"""
            <div class="info-box {color}">
                <strong>{player.name}</strong><br/>
                {status}
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # Boutons d'action
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        if st.button("🔄 Réinitialiser les votes"):
            game.reset_player_votes()
            st.session_state["current_player"] = 0
            st.rerun()

    with col2:
        # Vérifier si tout le monde a voté
        all_voted = all(p.has_voted for p in game.players)

        if st.button(
            "✅ Révéler et Valider", disabled=not all_voted, use_container_width=True
        ):
            result = game.process_votes()

            if result["coffee_break"]:
                st.warning("☕ Pause café demandée ! La partie est sauvegardée.")
                # Sauvegarder automatiquement
                save_path = json_handler.save_game(game.to_dict())
                st.info(f"💾 Partie sauvegardée : {save_path}")
                time.sleep(2)
                game.reset_player_votes()
                st.rerun()
            elif result["validated"]:
                st.success(result["message"])
                time.sleep(2)
                game.next_feature()
                st.rerun()
            else:
                st.warning(result["message"])
                time.sleep(2)
                game.reset_player_votes()
                st.rerun()

    with col3:
        if st.button("💾 Sauvegarder"):
            try:
                save_path = json_handler.save_game(game.to_dict())
                st.success(f"✅ Partie sauvegardée : {save_path}")
            except Exception as e:
                st.error(f"❌ Erreur : {str(e)}")

    with col4:
        if st.button("🏠 Quitter"):
            if st.button("⚠️ Confirmer ?"):
                st.session_state.page = "home"
                st.session_state.game = None
                st.rerun()


# ========== PAGE RESULTS ==========
def show_results_page():
    """Page des résultats finaux"""
    game = st.session_state.game

    st.markdown(
        "<h1 style='text-align: center;'>🏆 Résultats de la Partie</h1>",
        unsafe_allow_html=True,
    )

    results = game.get_results()

    # Métriques globales
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        show_metric_card(len(results["results"]), "Features Estimées", "✅")

    with col2:
        total_rounds = sum(f["rounds"] for f in results["results"])
        show_metric_card(total_rounds, "Tours Totaux", "🔄")

    with col3:
        avg_difficulty = (
            sum(f["difficulty"] for f in results["results"]) / len(results["results"])
            if results["results"]
            else 0
        )
        show_metric_card(f"{avg_difficulty:.1f}", "Difficulté Moyenne", "📊")

    with col4:
        if st.session_state.timer_start:
            elapsed = int(time.time() - st.session_state.timer_start)
            minutes = elapsed // 60
            show_metric_card(f"{minutes} min", "Durée Totale", "⏱️")

    st.markdown("---")

    # Tableau des résultats
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("### 📋 Détail des Estimations")

    for feature_result in results["results"]:
        with st.expander(
            f"✅ {feature_result['feature']} - Difficulté: {feature_result['difficulty']}"
        ):
            st.write(f"**Description:** {feature_result['description']}")
            st.write(f"**Nombre de tours:** {feature_result['rounds']}")

            if feature_result["vote_history"]:
                st.markdown("**Historique des votes:**")
                for vote_round in feature_result["vote_history"]:
                    st.write(f"Tour {vote_round['round']}: {vote_round['votes']}")

    st.markdown("</div>", unsafe_allow_html=True)

    # Boutons d'action
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("💾 Exporter les Résultats", use_container_width=True):
            try:
                save_path = json_handler.save_results(results)
                st.success(f"✅ Résultats exportés : {save_path}")
            except Exception as e:
                st.error(f"❌ Erreur : {str(e)}")

    with col2:
        if st.button("🆕 Nouvelle Partie", use_container_width=True):
            st.session_state.page = "setup"
            st.session_state.game = None
            st.rerun()

    with col3:
        if st.button("🏠 Retour Accueil", use_container_width=True):
            st.session_state.page = "home"
            st.session_state.game = None
            st.rerun()


# ========== PAGE LOAD ==========
def show_load_page():
    """Page de chargement d'une partie"""
    st.markdown(
        "<h1 style='text-align: center;'>📂 Charger une Partie</h1>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    saves = json_handler.list_saves()

    if not saves:
        st.info("Aucune sauvegarde disponible")
    else:
        selected_save = st.selectbox("Choisir une sauvegarde", saves)

        if st.button("📂 Charger", use_container_width=True):
            try:
                game_data = json_handler.load_game(selected_save)
                st.session_state.game = Game.from_dict(game_data)
                st.session_state.page = "game"
                st.success("✅ Partie chargée avec succès !")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"❌ Erreur : {str(e)}")

    if st.button("← Retour"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ========== PAGES EN LIGNE ==========


def show_online_create_page():
    """Page de création d'une salle en ligne"""
    st.markdown(
        "<h1 style='text-align: center;'>🆕 Créer une Salle de Poker</h1>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)

        st.markdown("### 🎮 Configuration de votre Salle")

        player_name = st.text_input(
            "Votre nom 👤", value="Host", placeholder="Entrez votre nom"
        )

        voting_mode = st.selectbox(
            "Mode de vote",
            options=list(VOTING_MODES.keys()),
            format_func=lambda x: VOTING_MODES[x],
        )

        st.info(f"**Mode sélectionné : {VOTING_MODES[voting_mode]}**")

        st.markdown("---")
        st.markdown("### 📋 Backlog")

        upload_option = st.radio(
            "Comment charger le backlog ?",
            ["Uploader un fichier JSON", "Créer manuellement"],
        )

        features = []

        if upload_option == "Uploader un fichier JSON":
            uploaded_file = st.file_uploader(
                "Choisir un fichier JSON", type=["json"], key="online_upload"
            )
            if uploaded_file:
                try:
                    backlog_data = json.load(uploaded_file)
                    features_data = backlog_data.get("backlog", [])
                    for idx, f in enumerate(features_data):
                        features.append(
                            {
                                "name": f.get("name", f"Feature {idx+1}"),
                                "description": f.get("description", ""),
                            }
                        )
                    st.success(f"✅ {len(features)} fonctionnalités chargées")
                except Exception as e:
                    st.error(f"❌ Erreur : {str(e)}")
        else:
            num_features = st.number_input(
                "Nombre de fonctionnalités",
                min_value=1,
                max_value=20,
                value=3,
                key="online_features",
            )
            for i in range(num_features):
                with st.expander(f"Feature {i+1}"):
                    f_name = st.text_input(
                        f"Nom", value=f"Feature {i+1}", key=f"online_feat_name_{i}"
                    )
                    f_desc = st.text_area(
                        f"Description", value="", key=f"online_feat_desc_{i}"
                    )
                    features.append({"name": f_name, "description": f_desc})

        st.markdown("</div>", unsafe_allow_html=True)

        col_back, col_create = st.columns([1, 1])

        with col_back:
            if st.button("← Retour", use_container_width=True):
                st.session_state.page = "home"
                st.rerun()

        with col_create:
            if st.button("🚀 Créer la Salle", use_container_width=True, type="primary"):
                if not player_name:
                    st.error("❌ Veuillez entrer votre nom !")
                elif len(features) == 0:
                    st.error("❌ Veuillez ajouter au moins une fonctionnalité !")
                else:
                    room_id = game_room_manager.create_room(player_name, voting_mode)
                    room = game_room_manager.get_room(room_id)
                    for feature in features:
                        room.add_feature(feature)
                    st.session_state.room_id = room_id
                    st.session_state.player_name = player_name
                    st.session_state.player_id = list(room.players.keys())[0]
                    st.session_state.online_game = room
                    st.session_state.page = "online_game"
                    st.success(f"✅ Salle créée! Code: {room_id}")
                    time.sleep(1)
                    st.rerun()


def show_online_join_page():
    """Page pour rejoindre une salle en ligne"""
    st.markdown(
        "<h1 style='text-align: center;'>🔗 Rejoindre une Salle</h1>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)

        st.markdown("### 👥 Rejoindre une Partie")

        player_name = st.text_input("Votre nom 👤", placeholder="Entrez votre nom")

        st.markdown("---")
        st.markdown("### 📋 Salles disponibles")
        rooms = game_room_manager.list_rooms()

        if rooms:
            for room in rooms:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(
                        f"**Hôte:** {room['host_name']} | **Joueurs:** {room['player_count']}"
                    )
                    st.write(f"Mode: {room['game_mode']}")
                with col2:
                    if st.button(
                        "Rejoindre",
                        key=f"join_{room['room_id']}",
                        use_container_width=True,
                    ):
                        if not player_name:
                            st.error("❌ Veuillez entrer votre nom !")
                        else:
                            player_id = game_room_manager.join_room(
                                room["room_id"], player_name
                            )
                            if player_id:
                                st.session_state.room_id = room["room_id"]
                                st.session_state.player_name = player_name
                                st.session_state.player_id = player_id
                                st.session_state.online_game = (
                                    game_room_manager.get_room(room["room_id"])
                                )
                                st.session_state.page = "online_game"
                                st.success(f"✅ Connecté!")
                                time.sleep(1)
                                st.rerun()
        else:
            st.info("Aucune salle disponible. Créez-en une!")

        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("← Retour", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()


def show_online_game_page():
    """Page de jeu en ligne"""
    room = st.session_state.online_game

    if not room:
        st.error("❌ Salle non trouvée")
        if st.button("← Retour à l'accueil"):
            st.session_state.page = "home"
            st.rerun()
        return

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.markdown(
            f"<div class='connection-status connected'>Salle: {room.room_id}</div>",
            unsafe_allow_html=True,
        )

    with col3:
        if st.button("🏠 Quitter"):
            st.session_state.page = "home"
            st.session_state.online_game = None
            st.rerun()

    st.markdown("---")

    st.markdown("### 👥 Joueurs Connectés")

    if len(room.players) > 0:
        player_cols = st.columns(len(room.players))
        for col, (pid, player) in zip(player_cols, room.players.items()):
            with col:
                st.markdown(
                    f"""
                <div class="online-player {'voted' if player.has_voted else 'active'}">
                    <strong>{player.name}</strong><br/>
                    {'✅ A voté' if player.has_voted else '⏳ En attente'}
                </div>
                """,
                    unsafe_allow_html=True,
                )

    st.markdown("---")

    current_feature = room.get_current_feature()

    if not current_feature:
        st.error("❌ Aucune feature disponible")
        return

    st.markdown(
        f"""
    <div class="main-container">
        <h3 style="color: #FFD700;">🎯 {current_feature['name']}</h3>
        <p>{current_feature['description']}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        "<h2 style='text-align: center; color: #FFD700;'>🎴 Choisissez votre carte</h2>",
        unsafe_allow_html=True,
    )

    current_player = room.players.get(st.session_state.player_id)

    if current_player and current_player.has_voted:
        st.success(f"✅ Vous avez voté: {current_player.current_vote}")
    else:
        cols_per_row = 6
        card_rows = [
            CARD_VALUES[i : i + cols_per_row]
            for i in range(0, len(CARD_VALUES), cols_per_row)
        ]

        for row in card_rows:
            cols = st.columns(len(row))
            for idx, (col, card_value) in enumerate(zip(cols, row)):
                with col:
                    if st.button(
                        str(card_value),
                        key=f"online_card_{card_value}",
                        use_container_width=True,
                    ):
                        room.player_vote(st.session_state.player_id, str(card_value))
                        st.session_state.online_game = room
                        st.rerun()

    st.markdown("---")

    if room.all_voted():
        st.markdown("### 📊 Votes Révélés")
        votes = room.get_votes()

        if len(votes) > 0:
            votes_cols = st.columns(len(votes))
            for col, (player_name, vote) in zip(votes_cols, votes.items()):
                with col:
                    st.markdown(
                        f"""
                    <div class="poker-card selected">
                        <div class="card-value">{vote}</div>
                        <div class="card-label">{player_name}</div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔄 Nouveau Vote"):
                room.reset_votes()
                st.session_state.online_game = room
                st.rerun()

        with col2:
            if st.button("➡️ Feature Suivante"):
                if room.next_feature():
                    st.session_state.online_game = room
                    st.rerun()
                else:
                    st.success("🏆 Partie Terminée!")


# ========== MAIN ==========
def main():
    """Fonction principale"""
    page = st.session_state.page

    if page == "home":
        show_home_page()
    elif page == "setup":
        show_setup_page()
    elif page == "game":
        show_game_page()
    elif page == "load":
        show_load_page()
    elif page == "online_create":
        show_online_create_page()
    elif page == "online_join":
        show_online_join_page()
    elif page == "online_game":
        show_online_game_page()


if __name__ == "__main__":
    main()

# Pages en ligne pour Planning Poker
# Ce fichier contient les pages pour le jeu multijoueur en ligne

def setup_online_pages(st, game_room_manager, CARD_VALUES, VOTING_MODES, json):
    """Configure les pages en ligne"""
    
    def show_online_create_page():
        """Page de création d'une salle en ligne"""
        st.markdown("<h1 style='text-align: center;'>🆕 Créer une Salle de Poker</h1>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("<div class='main-container'>", unsafe_allow_html=True)
            
            st.markdown("### 🎮 Configuration de votre Salle")
            
            # Informations du joueur
            player_name = st.text_input("Votre nom 👤", value="Host", placeholder="Entrez votre nom")
            
            # Mode de vote
            voting_mode = st.selectbox(
                "Mode de vote",
                options=list(VOTING_MODES.keys()),
                format_func=lambda x: VOTING_MODES[x]
            )
            
            st.info(f"""
            **Mode sélectionné : {VOTING_MODES[voting_mode]}**
            """)
            
            st.markdown("---")
            
            # Backlog
            st.markdown("### 📋 Backlog")
            
            upload_option = st.radio(
                "Comment charger le backlog ?",
                ["Uploader un fichier JSON", "Créer manuellement"]
            )
            
            features = []
            
            if upload_option == "Uploader un fichier JSON":
                uploaded_file = st.file_uploader("Choisir un fichier JSON", type=['json'], key="online_upload")
                
                if uploaded_file:
                    try:
                        backlog_data = json.load(uploaded_file)
                        features_data = backlog_data.get("backlog", [])
                        for idx, f in enumerate(features_data):
                            features.append({
                                "name": f.get("name", f"Feature {idx+1}"),
                                "description": f.get("description", "")
                            })
                        st.success(f"✅ {len(features)} fonctionnalités chargées")
                    except Exception as e:
                        st.error(f"❌ Erreur : {str(e)}")
            else:
                num_features = st.number_input("Nombre de fonctionnalités", min_value=1, max_value=20, value=3, key="online_features")
                
                for i in range(num_features):
                    with st.expander(f"Feature {i+1}"):
                        f_name = st.text_input(f"Nom", value=f"Feature {i+1}", key=f"online_feat_name_{i}")
                        f_desc = st.text_area(f"Description", value="", key=f"online_feat_desc_{i}")
                        features.append({"name": f_name, "description": f_desc})
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Boutons
            col_back, col_create = st.columns([1, 1])
            
            with col_back:
                if st.button("← Retour", use_container_width=True):
                    st.session_state.page = 'home'
                    st.rerun()
            
            with col_create:
                if st.button("🚀 Créer la Salle", use_container_width=True, type="primary"):
                    if not player_name:
                        st.error("❌ Veuillez entrer votre nom !")
                    elif len(features) == 0:
                        st.error("❌ Veuillez ajouter au moins une fonctionnalité !")
                    else:
                        # Créer la salle
                        room_id = game_room_manager.create_room(player_name, voting_mode)
                        room = game_room_manager.get_room(room_id)
                        
                        # Ajouter les fonctionnalités
                        for feature in features:
                            room.add_feature(feature)
                        
                        st.session_state.room_id = room_id
                        st.session_state.player_name = player_name
                        st.session_state.player_id = list(room.players.keys())[0]
                        st.session_state.online_game = room
                        st.session_state.page = 'online_game'
                        st.success(f"✅ Salle créée! Code: {room_id}")
                        st.rerun()
    
    return show_online_create_page

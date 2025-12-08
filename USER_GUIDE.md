# 🎰 Guide Utilisateur - Casino Universe Planning Poker

## 🎬 Démarrage Rapide

### 1. Lancer l'Application

```bash
cd c:\Users\DEll\Desktop\planing_str
echo "" | streamlit run app.py
```

Ouvrir dans le navigateur: **http://localhost:8505**

---

## 🏠 Page d'Accueil

Vous verrez 2 onglets:

- 🖥️ **Local** - Jouer avec équipe locale
- 🌐 **En Ligne** - Jouer avec équipe distribuée

### Mode Local: Nouvelle Partie

1. Cliquer "🎮 Nouvelle Partie Locale"
2. Ajouter les joueurs (Ex: "Joueur 1", "Joueur 2", etc.)
3. Sélectionner mode de vote
4. Ajouter features à estimer
5. **Cliquer "Démarrer Partie"**

---

## 🎴 La Table Ronde (CE QUI EST NOUVEAU!)

### Vue Générale

Vous verrez une **table ronde de casino** avec **6 cartes** positionnées autour:

```
        🎴 1

  🎴 2       🎴 13


  🎴 8       🎴 5

      🎴 3
```

Chaque position correspond à une carte:

- **1** - En haut (Top)
- **2** - Haut-droit (Top-right)
- **3** - Bas-droit (Bottom-right)
- **5** - En bas (Bottom)
- **8** - Bas-gauche (Bottom-left)
- **13** - Haut-gauche (Top-left)

### ✨ Animations

#### Chargement

- La table **apparaît graduellement** (zoom 0.8 → 1.0)
- Les cartes **arrivent en arc** depuis les côtés

#### Survol (Hover)

1. La carte **s'élève** progressivement
2. Brille avec **glow or + rouge + violet**
3. Légère **rotation 3D**
4. L'ombre au sol s'agrandit
5. Tout en boucle infiniment (subtil)

#### Clic/Sélection

1. **Rotation 3D spectaculaire** (flip 360°)
2. Fond change en **gradient or**
3. Bordure devient **neon-pink pulsante**
4. **Glow maximal** (5 couches de lumière)
5. Texte flicke (style néon Vegas)
6. Ombre au sol maximale

### Comment Voter

1. **Regarder** la table ronde
2. **Survoler** les cartes (voir glow)
3. **Cliquer** la carte choisie
4. Voir l'**animation flip 3D**
5. Votre vote est enregistré!
6. Joueur suivant peut voter

---

## 🎯 Flux de Jeu Complet

```
┌─────────────────┐
│  Page Accueil   │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│ Configuration   │
│ (Joueurs, Mode) │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Jeu - Feature 1│
│ Table Ronde 🎰  │ ← VOUS ÊTES ICI!
│ 6 cartes        │
└────────┬────────┘
         │ Tous votent
         ↓
┌─────────────────┐
│ Résultats       │
│ Graphiques      │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│ Feature Suivante│
│ (ou Fin)        │
└─────────────────┘
```

---

## 🎮 Contrôles

### Clavier

- **Souris**: Hover et cliquer les cartes
- **Écran tactile**: Tapoter les cartes (mobile/tablet)

### Souris

- **Hover**: Voir glow et flottaison
- **Clic**: Flip 3D et sélection
- **Clic autre**: Désélectionner (optionnel)

---

## 🎨 Couleurs - Signification

| Couleur            | Signification                     |
| ------------------ | --------------------------------- |
| 🟡 **Or**          | Cartes normales, border principal |
| 🔴 **Rouge**       | Energie, sélection active         |
| 💜 **Violet Néon** | Effets futuristes                 |
| 🔵 **Cyan**        | Accents high-tech                 |
| 🩷 **Pink Néon**    | Carte sélectionnée = INTENSE      |

---

## 💡 Tips & Tricks

### Pour Mieux Voir les Effets

1. **Full screen** le navigateur (F11)
2. **Obscurcir** la pièce (néon brille mieux dans le noir!)
3. **Zoom 100%** (pas de zoom navigateur)
4. **Désactiver blocker pub** (certains bloquent CSS)

### Pour Utiliser au Maximum

- **Prendre son temps** à l'étape vote
- **Survoler** chaque carte (voir glow)
- **Apprécier** l'animation flip
- **Profiter** de l'ambiance casino!

### Performance

- Animations fluides = 60 FPS stable
- Pas de lag même avec animations multiples
- Optimisé pour Chrome, Firefox, Safari, Edge

---

## 🔧 Troubleshooting

### Les cartes ne s'animent pas

**Solution**:

- Rafraîchir (F5)
- Effacer cache (Ctrl+Shift+Del)
- Essayer autre navigateur

### La table n'apparaît pas

**Solution**:

- Scrollez vers le bas (table est grande)
- Vérifiez résolution (minimum 800x600)
- Vérifiez JavaScript activé

### Lag ou saccades

**Solution**:

- Fermer autres tabs
- Fermer extensions lourd
- Réduire qualité vidéos
- Utiliser navigateur plus récent

### Mode sombre trop sombre

**Solution**:

- Augmenter brillance moniteur
- Utiliser mode jour navigateur (si dispo)
- Éloigner du reflet lumière

---

## 📱 Utilisation Mobile/Tablet

### ✅ Fonctionne

- Animations réduites (moins de glow)
- Tap au lieu de click
- Responsive design
- Portrait et landscape

### ⚠️ Limitations

- Plus petit = moins visible (zoom recommandé)
- Animations moins lisses (moins GPU power)
- Tactile peut avoir lag minimal

### 💡 Tips Mobile

- Utilisez landscape si possible
- Augmentez zoom à 120%
- Utilisez appareil récent
- Testez connexion Wi-Fi

---

## 🎓 Pour Comprendre les Animations

### Vocabulaire Technique (Explicatif)

**Fade-in**: La chose apparaît graduellement (opacity: 0 → 1)

**Zoom**: Effet agrandissement/rétrécissement (scale: 0.8 → 1.0)

**3D/Flip**: Rotation en 3D comme une vraie carte (rotateY: 0 → 360°)

**Glow**: Lumière fluorescente autour (box-shadow)

**Hover**: Action de survoler avec souris

**Animation loop**: Qui répète infiniment (vs une seule fois)

**Cubic-bezier**: Formule pour vitesse = plus naturelle

---

## 📊 Statistiques de Votre Session

Streamlit affiche:

- **Timer**: Temps écoulé depuis début
- **Progress Bar**: % de joueurs ayant voté
- **Feature Actuelle**: Nom et description
- **Tour de vote**: Quel round en cours

---

## 🎉 Fin de Partie

Après tous les votes:

1. **Voir les résultats** en graphique
2. **Moyenne, Médiane, Mode** des estimations
3. **Consensus** ou **Divergence**
4. **Exporter** résultats en JSON
5. **Charger** partie sauvegardée (optionnel)

---

## 🌐 Mode En Ligne

### Différences

- Créer ou rejoindre **GameRoom**
- Joueurs connectés **simultanément**
- Votes en **temps réel**
- Voir status: **Online/Offline/Voting**

### Étapes

1. Cliquer "🌐 En Ligne"
2. Créer salle (générer ID)
3. Partager ID avec équipe
4. Ou rejoindre salle existante
5. Même animation table ronde!

---

## 🚀 Astuces Avancées

### Personnaliser Cartes

Éditer `src/utils/constants.py`:

```python
CARD_VALUES = [1, 2, 3, 5, 8, 13, 21, "?", "☕"]
```

### Modifier Animations

Éditer `src/ui/styles.py`:

- Durées: Chercher `0.8s`, `1s`, etc.
- Couleurs: Modifier `#FFD700`, `#DC143C`, etc.
- Effets: Changer `transform`, `box-shadow`

### Ajouter Sons (Futur)

```python
# À ajouter dans create_premium_card_html()
st.audio("card_sound.mp3", ...)
```

---

## 📞 Support

### Besoin d'Aide?

1. Vérifiez navigateur supporté (Chrome 90+)
2. Effacez cache et cookies
3. Relancez `streamlit run app.py`
4. Réouvrez http://localhost:8505

### Partager Feedback

Créez issue GitHub avec:

- Version navigateur
- Capture d'écran
- Description du bug

---

## 🎓 Ressources

- **Fichier complet des animations**: `CASINO_UNIVERSE_DESIGN.md`
- **Démo HTML standalone**: `casino_table_demo.html`
- **Summary technique**: `IMPLEMENTATION_SUMMARY.md`
- **Code source**: `src/ui/styles.py`

---

## ✨ Enjoy!

Vous avez maintenant une **planning poker experience premium** avec:

✅ Table ronde casino authentique  
✅ Animations fluides 60 FPS  
✅ Palette néon immersive  
✅ Interactions 3D réalistes  
✅ Design professional

**Prêt à estimer avec style! 🎰🎴**

---

**Dernière mise à jour**: December 8, 2025  
**Version**: 2.0 - Casino Universe Edition  
**Status**: ✅ Production Ready

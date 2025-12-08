# 🎰 CASINO UNIVERSE - Design & Animations

## 📋 Vue d'ensemble

Your Planning Poker application has been transformed into an immersive **Casino Universe Experience** with professional-grade animations and a luxury poker aesthetic.

---

## 🎴 Partie 1: Table Ronde de Casino (NOUVEAU!)

### ✨ Animations & Effets

#### 1️⃣ **Fade-in + Zoom au Chargement**

- **Animation**: `table-fade-zoom`
- **Durée**: 1s
- **Effet**: La table apparaît progressivement avec un zoom léger (0.8 → 1.0)
- **Timing**: `cubic-bezier(0.34, 1.56, 0.64, 1)` (overshoot naturel)

#### 2️⃣ **Arrivée Orbitale des Cartes**

- **Animation**: `orbital-slide` (cartes de droite) / `orbital-slide-reverse` (cartes de gauche)
- **Durée**: 0.8s
- **Effet**: Les cartes glissent en arc depuis l'extérieur vers leur position finale
  - Départ: 200px de côté + 100px vers le bas + rotation 30°
  - Intermédiaire: Position semi-proche + rotation 15°
  - Arrivée: Position précise + rotation 0°

#### 3️⃣ **Table Spotlight (Lumière focalisée)**

- **Animation**: `table-spotlight`
- **Durée**: 3s (infini)
- **Effet**: La lumière au centre de la table pulse progressivement
  - Commence: Glow doré faible (0.2 opacity)
  - Pic: Glow intense (0.4 opacity) + ombres rouges et violettes
  - Retour: Glow faible

#### 4️⃣ **Bordure Neon Rotative**

- **Animation**: `spin-360`
- **Durée**: 8s (infini)
- **Effet**: La bordure externe (conic-gradient rouge→or→violet) tourne continuellement
- **Utilisation**: `::after` pseudo-élément de `.poker-table`

---

### 🎯 Interactions Utilisateur

#### **Hover - Élévation 3D**

- **Animation**: `card-hover-lift`
- **Durée**: 1.5s (infini)
- **Effets**:
  - ⬆️ Élévation: `-30px`
  - 🔍 Zoom: `1.12x`
  - 🔄 Rotation 3D: `rotateX(8deg) rotateY(-8deg)`
  - ✨ Multiple Box-Shadows:
    - Ombre générale: `0 40px 100px rgba(0,0,0,0.8)`
    - Glow or: `0 0 60px rgba(255,215,0,0.5)`
    - Glow rouge: `0 0 100px rgba(220,20,60,0.3)`
    - Glow violet: `0 0 150px rgba(157,0,255,0.2)`
  - 🪶 Légère rotation micro pour donner du "life"

#### **Sélection - Flip 3D Spectaculaire**

- **Animation**: `flip-3d-select`
- **Durée**: 0.8s (une fois)
- **Effets**:
  - 🔀 Rotation 3D: `rotateY(360deg)` avec micro `rotateX`
  - 📈 Zoom: `1.25x`
  - ⬆️ Élévation: `-40px`
  - 🎨 Gradient or (#FFD700 → #FFB700)
  - 🔗 Border neon-pink pulsante
  - ⭐ Box-Shadow intensif:
    - Ombre majeure: `0 50px 120px rgba(0,0,0,0.9)`
    - Glow or: `0 0 80px rgba(255,215,0,0.8)`
    - Glow rouge: `0 0 120px rgba(220,20,60,0.6)`
    - Glow violet: `0 0 180px rgba(157,0,255,0.5)`
    - Glow pink: `0 0 240px rgba(255,0,110,0.3)`

#### **Ombres Dynamiques au Sol**

- **Utilisation**: `::before` pseudo-élément de `.card-premium`
- **Effet**: Ellipse floue sous chaque carte
  - État normal: 30px height, 0.4 opacity
  - Hover: 40px height, 0.6 opacity
  - Sélection: 50px height, 0.8 opacity
- **Timing**: Suivi fluide avec transition 0.5s

---

### 🎨 Palette de Couleurs - Casino Universe

| Couleur          | Code      | Utilisation                |
| ---------------- | --------- | -------------------------- |
| **Or**           | `#FFD700` | Dominant, borders, accents |
| **Rouge Casino** | `#DC143C` | Energy, texte sélection    |
| **Bleu Poker**   | `#003366` | Secondaire, table          |
| **Violet Néon**  | `#9D00FF` | Accent futuriste           |
| **Cyan Néon**    | `#00FFFF` | Effets high-tech           |
| **Pink Néon**    | `#FF006E` | Sélection, bordure intense |
| **Vert Poker**   | `#0B5D3D` | Background table           |

---

## 🎴 Partie 2: Cartes Standards (Grille)

### Cartes Standard

- **Taille**: Moyenne (régulière pour la grille)
- **Animation de deal**: Les cartes arrivent de la gauche avec rotation
- **Effets hover/sélection**: Similaires à la table ronde mais à échelle réduite

### Animations Disponibles

#### **Deal Animation**

```css
@keyframes deal-card-animation {
  0% {
    transform: translateX(-200%) rotateZ(-45deg) scale(0.5);
    opacity: 0;
  }
  50% {
    transform: translateX(-50%) rotateZ(-20deg) scale(0.9);
  }
  100% {
    transform: translateX(0) rotateZ(0deg) scale(1);
    opacity: 1;
  }
}
```

#### **Card Float**

```css
@keyframes card-float {
  0%,
  100% {
    transform: translateY(0px) scale(1);
  }
  50% {
    transform: translateY(-20px) scale(1.05);
  }
}
```

#### **Spin 360°**

```css
@keyframes spin-360 {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(360deg);
  }
}
```

#### **Neon Flicker**

```css
@keyframes neon-flicker {
  0%,
  19%,
  21%,
  23%,
  25%,
  54%,
  56%,
  100% {
    text-shadow: 0 0 10px var(--poker-gold), 0 0 20px var(--neon-pink),
      0 0 30px var(--neon-cyan);
  }
  20%,
  24%,
  55% {
    text-shadow: 0 0 5px var(--poker-gold);
  }
}
```

---

## 🎭 Partie 3: Interface Générale

### Fond & Atmosphère

```css
.stApp {
  background: radial-gradient(
    ellipse at center,
    #1a1a2e 0%,
    #0f0f1e 50%,
    #000000 100%
  );
}
```

- Dégradé radial créant une atmosphère de casino sombre
- Centre: Bleu profond (#1a1a2e)
- Milieu: Très sombre (#0f0f1e)
- Bordures: Noir absolu (#000000)

### Headers avec Glow

```css
h1,
h2,
h3 {
  animation: glow-pulse 3s ease-in-out infinite;
  text-shadow: 0 0 20px rgba(255, 215, 0, 0.8), 0 0 40px rgba(220, 20, 60, 0.5),
    0 0 60px rgba(157, 0, 255, 0.3);
}
```

- Or, rouge et violet qui pulsent ensemble
- Crée un effet "neon flicker" sur les titres H1

### Conteneurs (Main Container)

- Gradient subtle bleu/vert
- Bordure or avec glow
- Effet shimmer qui glisse de gauche à droite (3s)
- Backdrop blur pour profondeur

### Boutons

- Gradient rouge → rouge foncé
- Border or
- Hover: Scale + multiple glows (or, rouge, violet)
- Effet shimmer blanc sur hover

### Progress Bar

- Gradient or → rouge → or (animated)
- Box-shadow dynamique avec glow
- Pulsation continue

---

## 🎮 Directives d'Utilisation

### Pour Activer la Table Ronde:

```python
# Dans app.py
show_casino_table_selection(CARD_VALUES, on_card_selected)
```

### Pour Personnaliser les Animations:

1. Durées: Modifier les valeurs en `ms` dans les `@keyframes`
2. Couleurs: Utiliser les variables CSS `:root` (--poker-gold, etc.)
3. Intensité d'effets: Ajuster les values d'opacity et blur

---

## 📊 Récapitulatif des Animations

| Animation           | Durée       | Répétition | Effet             |
| ------------------- | ----------- | ---------- | ----------------- |
| table-fade-zoom     | 1s          | 1x         | Apparition table  |
| orbital-slide       | 0.8s        | 1x         | Arrivée cartes    |
| table-spotlight     | 3s          | ∞          | Lumière centrale  |
| spin-360            | 8s (border) | ∞          | Bordure rotative  |
| card-hover-lift     | 1.5s        | ∞          | Flottaison hover  |
| flip-3d-select      | 0.8s        | 1x         | Sélection flip    |
| glow-pulse          | 3s          | ∞          | Pulsation headers |
| neon-flicker        | 3s          | ∞          | Tremolo neon      |
| gradient-shift      | 2s          | ∞          | Progress bar      |
| card-float          | 3s          | ∞          | Flottaison cartes |
| deal-card-animation | 0.8s        | 1x         | Arrivée cartes    |

---

## 🎯 Performance

- **GPU Acceleration**: Tous les `transform` et `opacity` utilisent le GPU
- **Pas d'animations heavy**: Pas de color ou dimension changes animés
- **Smooth 60fps**: Optimisé pour navigateurs modernes
- **Mobile Friendly**: Animations réduites sur écrans petits

---

## 🚀 Prochaines Améliorations (Futures)

1. **Son**: Ajouter des effets sonores casino (cartes qui tombent, chips)
2. **Particles**: Animation de particules lors de la sélection
3. **Confetti**: Effet confetti au résultat final
4. **VR Ready**: CSS 3D prêt pour webXR
5. **Dark Mode**: Toggle pour different themes

---

**Version**: 2.0 - Casino Universe Edition  
**Date**: December 2025  
**Status**: ✅ Production Ready

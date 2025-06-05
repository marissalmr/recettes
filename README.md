# recettes
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Status](https://img.shields.io/badge/Status-En%20développement-orange)
Stage - 1ére année
# Crumble Kiss – Une plateforme gourmande pour créer, partager et noter vos recettes

L’application propose une expérience utilisateur complète : 
- création de compte,
- découverte et publication de recettes,
- commentaires,
- système de notation avec affichage de la moyenne pour chaque recette.

---
## Pourquoi Django ?

En tant que débutante, j'avais une meilleure maîtrise de Python que d'autres langages back-end.  
Choisir Django m’a permis non seulement de progresser dans ce langage, mais aussi de découvrir et comprendre pour la première fois ce qu’est un framework web.  
C’était l’occasion d’apprendre à organiser un projet proprement avec une architecture MVT, de gérer la base de données, les vues, les templates, et de manipuler des concepts concrets comme les formulaires, les routes ou les relations entre modèles.

---
## Défis rencontrés

J’ai rencontré plusieurs difficultés techniques, notamment :
- la compréhension du fonctionnement du modèle MVT,
- la construction des vues et la gestion des formulaires dynamiques,
- l’affichage conditionnel des données dans les templates (comme les ID, la moyenne des notes, etc.).

Ces obstacles m'ont poussée à aller plus loin dans mes recherches, à lire de la documentation ce qui a grandement renforcé mes compétences.

---
## Pistes d’évolution

Voici quelques fonctionnalités que j’aimerais ajouter à l’avenir :
- Ajout d’un système de recherche ou de filtres (par ingrédient, catégorie, durée, etc.),
- Système de favoris (pour sauvegarder ses recettes préférées),
- Gestion des photos multiples pour les étapes d'une recette,
- Pagination pour les listes de recettes.

---
## Comment installer et exécuter le projet

Voici les étapes pour installer et lancer le projet Crumble Kiss en local sur votre machine.




## Étapes d’installation

**Cloner le projet**

```bash
git clone https://github.com/marissalmr/recettes.git
cd recettes
```
**Créer et activer un environnement virtuel**



```bash
python -m venv env
source env/bin/activate #Sur macOS/Linux
env\Scripts\activate #Sur Windows

```
##  Installer les dépendances

```bash
pip install -r requirements.txt
```
**Créer la base de données**
```bash
python manage.py migrate
```

**Lancer le serveur en local**
```bash
python manage.py runserver
```

**Une fois le serveur lancé, ouvrez votre navigateur à l'adresse ci-dessous pour vous inscrire :**
```bash
http://127.0.0.1:8000/authentification/signup/
```







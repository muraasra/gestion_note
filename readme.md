# Gestion des Notes des Étudiants

## Description
Ce projet est une application console en Python pour la gestion des notes des étudiants. Il permet :
- *D’enregistrer des matières* (nom, code).
- *D’enregistrer des apprenants* (nom, prénom, ID).
- *D’enregistrer des notes* pour chaque apprenant dans une matière.
- *D’afficher les données* :
  - Liste des matières.
  - Liste des apprenants.
  - Notes attribuées à un apprenant donné.

## Prérequis
Assurez-vous d’avoir :
- Python 3 installé sur votre machine.
- Un terminal ou une console pour exécuter le projet.

---

## Cloner le projet
Pour cloner le projet depuis GitHub, utilisez la commande suivante dans votre terminal :

```bash
 git clone <https://github.com/muraasra/gestion_note.git> 
 cd ges_note
```
## Execution
l'Execution du programme se fait via la classe principale avec la commande :
```bash
python gestion_scolaires.py
```
## Fonctionnalités
- Enregistrer une matière
- Enregistrer un apprenant
- Enregistrer une note pour un apprenant
- Afficher les matières, les apprenants, et les notes d’un apprenant

## Structure des Classes
### Classe Matiere
- Attributs : nom, code ... 
- Méthodes :
  - ajouterMatiere(matieres, nom, code ... )
  - afficherMatieres(matieres ... )

### Classe Apprenant
- Attributs : nom, prenom, id ....
- Méthodes :
  - ajouterApprenant(apprenants, nom, prenom, id ...)
  - afficherApprenants(apprenants   ... )

### Classe Note
- Attributs : valeur, apprenantId, matiereCode ...
- Méthodes :
  - ajouterNote(notes, valeur, apprenantId, matiereCode ...)
  - afficherNotesApprenant(notes, apprenantId ...)
from matiere import Matiere
from apprenant import Apprenant
# Importation des classes nécessaires
class Matiere:
    def __init__(self, nom, code, coef, enseignant):
        self.nom = nom
        self.code = code
        self.coef = coef
        self.enseignant = enseignant

    @classmethod
    def ajouterMatiere(cls, matieres, nom, code, coef, enseignant):
        for matiere in matieres:
            if matiere.code == code:
                print(f"Erreur : Une matière avec le code {code} existe déjà.")
                return False

        # Crée une nouvelle matière et l'ajoute à la liste
        nouvelle_matiere = cls(nom, code, coef, enseignant)
        matieres.append(nouvelle_matiere)
        print(f"Matière '{nom}' ajoutée avec succès.")
        return True

    @staticmethod
    def afficherMatieres(matieres):
        if not matieres:
            print("Aucune matière enregistrée.")
            return

        print("Liste des matières :")
        for matiere in matieres:
            print(f"Nom : {matiere.nom}, Code : {matiere.code}, Coefficient : {matiere.coef}, Enseignant : {matiere.enseignant}")


class Apprenant:
    def __init__(self, nom, prenom, id):
        self.nom = nom
        self.prenom = prenom
        self.id = id

    @classmethod
    def ajouterApprenant(cls, apprenants, nom, prenom, id):
        for apprenant in apprenants:
            if apprenant.id == id:
                print(f"Erreur : Un apprenant avec l'ID {id} existe déjà.")
                return False

        # Crée un nouvel apprenant et l'ajoute à la liste
        nouvel_apprenant = cls(nom, prenom, id)
        apprenants.append(nouvel_apprenant)
        print(f"Apprenant '{prenom} {nom}' ajouté avec succès.")
        return True

    @classmethod
    def afficherApprenants(cls, apprenants):
        if not apprenants:
            print("Aucun apprenant enregistré.")
            return

        print("Liste des apprenants :")
        for apprenant in apprenants:
            print(f"ID: {apprenant.id}, Nom: {apprenant.nom}, Prénom: {apprenant.prenom}")


class Note:
    def __init__(self, valeur, apprenantId, matiereCode):
        self.valeur = valeur
        self.apprenantId = apprenantId
        self.matiereCode = matiereCode

    @classmethod
    def ajouterNote(cls, notes, valeur, apprenantId, matiereCode):
        notes.append(cls(valeur, apprenantId, matiereCode))
        print(f"Note de {valeur} ajoutée pour l'apprenant ID {apprenantId} en matière {matiereCode}.")

    @staticmethod
    def afficherNotesApprenant(notes, apprenantId):
        print(f"\nNotes pour l'apprenant ID {apprenantId} :")
        for note in notes:
            if note.apprenantId == apprenantId:
                print(f"Matière Code : {note.matiereCode}, Note : {note.valeur}")


class GestionScolaire:
    def __init__(self):
        self.matieres = []
        self.apprenants = []
        self.notes = []

    def menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Enregistrer une matière")
            print("2. Enregistrer un apprenant")
            print("3. Enregistrer une note")
            print("4. Lister les matières")
            print("5. Lister les apprenants")
            print("6. Voir les notes d’un apprenant")
            print("0. Quitter")

            choix = input("Entrez votre choix : ")

            if choix == "1":
                self.enregistrerMatiere()
            elif choix == "2":
                self.enregistrerApprenant()
            elif choix == "3":
                self.enregistrerNote()
            elif choix == "4":
                self.afficherMatieres()
            elif choix == "5":
                self.afficherApprenants()
            elif choix == "6":
                self.afficherNotesApprenant()
            elif choix == "0":
                break
            else:
                print("Choix invalide, veuillez réessayer.")
    
    def enregistrerMatiere(self):
        nom = input("Entrez le nom de la matière : ")
        code = input("Entrez le code de la matière : ")
        coef = float(input("Entrez le coefficient de la matière : "))
        enseignant = input("Entrez le nom de l'enseignant : ")
        Matiere.ajouterMatiere(self.matieres, nom, code, coef, enseignant)
    
    def enregistrerApprenant(self):
        nom = input("Entrez le nom de l'apprenant : ")
        prenom = input("Entrez le prénom de l'apprenant : ")
        id = input("Entrez l'ID de l'apprenant : ")
        Apprenant.ajouterApprenant(self.apprenants, nom, prenom, id)
    
    def enregistrerNote(self):
        apprenantId = input("Entrez l'ID de l'apprenant : ")
        matiereCode = input("Entrez le code de la matière : ")
        valeur = float(input("Entrez la note : "))
        Note.ajouterNote(self.notes, valeur, apprenantId, matiereCode)
    
    def afficherMatieres(self):
        Matiere.afficherMatieres(self.matieres)
    
    def afficherApprenants(self):
        Apprenant.afficherApprenants(self.apprenants)
    
    def afficherNotesApprenant(self):
        apprenantId = input("Entrez l'ID de l'apprenant : ")
        Note.afficherNotesApprenant(self.notes, apprenantId)
    
if __name__ == "__main__":
    gestion = GestionScolaire()
    gestion.menu()

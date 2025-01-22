from matiere import Matiere
from apprenant import Apprenant
from note import Note

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

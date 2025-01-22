from matiere import Matiere
from apprenant import Apprenant
from note import Note

class GestionScolaire:
    def _init_(self):
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
                print("Merci d'avoir utilisé le système !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def enregistrerMatiere(self):
        nom = input("Nom de la matière : ")
        code = input("Code de la matière : ")
        coef = int(input("Entrez le coefficient de la matière: "))
        enseignant = input("Entrez le nom de l'enseignant: ")
        Matiere.ajouterMatiere(self.matieres, nom, code, coef, enseignant)
        print(f"Matière '{nom}' ajoutée avec succès.")

    def enregistrerApprenant(self):
        nom = input("Nom de l'apprenant : ")
        prenom = input("Prénom de l'apprenant : ")
        id = input("ID de l'apprenant : ")
        Apprenant.ajouterApprenant(self.apprenants, nom, prenom, id)
        print(f"Apprenant '{prenom} {nom}' ajouté avec succès.")

    def enregistrerNote(self):
        apprenantId = input("ID de l'apprenant : ")
        matiereCode = input("Code de la matière : ")
        valeur = float(input("Valeur de la note : "))
        Note.ajouterNote(self.notes, valeur, apprenantId, matiereCode)
        print(f"Note de {valeur} ajoutée pour l'apprenant ID {apprenantId} en matière {matiereCode}.")

    def afficherMatieres(self):
        print("\nListe des matières :")
        if not self.matieres:
            print("Aucune matière enregistrée.")
        else:
            Matiere.afficherMatieres(self.matieres)

    def afficherApprenants(self):
        print("\nListe des apprenants :")
        if not self.apprenants:
            print("Aucun apprenant enregistré.")
        else:
            Apprenant.afficherApprenants(self.apprenants)

    def afficherNotesApprenant(self):
        apprenantId = input("ID de l'apprenant : ")
        print(f"\nNotes pour l'apprenant ID {apprenantId} :")
        Note.afficherNotesApprenant(self.notes, apprenantId)


# Exécution principale
if __name__ == "_main_":
    gestion = GestionScolaire()
    gestion.menu()

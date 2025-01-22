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
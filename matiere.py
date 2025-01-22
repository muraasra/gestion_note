class Matiere:
    def init(self, nom, code, coef, enseignant):
        self.nom = nom
        self.code = code
        self.coef = coef
        self.enseignant = enseignant

    @staticmethod
    def ajouterMatiere():
        nom = input("Entrez le nom de la matière: ")
        code = int(input("Entrez le code de la matière: "))
        coef = int(input("Entrez le coefficient de la matière: "))
        enseignant = input("Entrez le nom de l'enseignant: ")
        return Matiere(nom, code, coef, enseignant)

    def afficherMatiere(matieres):
        for matiere in matieres:
            print(f"Nom : {matiere.nom}, Code : {matiere.code}, Coefficient : {matiere.coef}, Enseignant : {matiere.enseignant}")
        
    

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
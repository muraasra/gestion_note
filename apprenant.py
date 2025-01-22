
        
class Apprenant:
    # Liste pour stocker tous les apprenants
    liste_apprenants = []

    def _init_(self, nom, prenom, id):
        self.nom = nom
        self.prenom = prenom
        self.id = id

    @classmethod
    def ajouter_apprenant(cls, nom, prenom, id):
        """
        Ajoute un apprenant à la liste après vérification de l'unicité de l'ID.
        """
        for apprenant in cls.liste_apprenants:
            if apprenant.id == id:
                print(f"Erreur : Un apprenant avec l'ID {id} existe déjà.")
                return False
        
        # Crée un nouvel apprenant et l'ajoute à la liste
        nouvel_apprenant = cls(nom, prenom, id)
        cls.liste_apprenants.append(nouvel_apprenant)
        print(f"Apprenant {nom} {prenom} ajouté avec succès.")
        return True

    @classmethod
    def afficher_apprenants(cls):
        """
        Affiche la liste des apprenants enregistrés.
        """
        if not cls.liste_apprenants:
            print("Aucun apprenant enregistré.")
            return

        print("Liste des apprenants enregistrés :")
        for apprenant in cls.liste_apprenants:
            print(f"ID: {apprenant.id}, Nom: {apprenant.nom}, Prénom: {apprenant.prenom}")

    @classmethod
    def rechercher_apprenant(cls, id):
        """
        Recherche un apprenant par ID et retourne ses informations.
        """
        for apprenant in cls.liste_apprenants:
            if apprenant.id == id:
                print(f"Apprenant trouvé : ID: {apprenant.id}, Nom: {apprenant.nom}, Prénom: {apprenant.prenom}")
                return apprenant
        print(f"Aucun apprenant trouvé avec l'ID {id}.")
        return None

    @classmethod
    def supprimer_apprenant(cls, id):
        """
        Supprime un apprenant de la liste en fonction de son ID.
        """
        for apprenant in cls.liste_apprenants:
            if apprenant.id == id:
                cls.liste_apprenants.remove(apprenant)
                print(f"Apprenant avec l'ID {id} supprimé avec succès.")
                return True
        print(f"Aucun apprenant trouvé avec l'ID {id}.")
        return False
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
class Note:
    def _init_(self, valeur, apprenantId, matiereCode):
        self.valeur = valeur
        self.apprenantId = apprenantId
        self.matiereCode = matiereCode

    @staticmethod
    def ajouterNote(notes, valeur, apprenantId, matiereCode):
        notes.append(Note(valeur, apprenantId, matiereCode))

    @staticmethod
    def afficherNotesApprenant(notes, apprenantId):
        print(f"Notes pour l'apprenant ID {apprenantId} :")
        for note in notes:
            if note.apprenantId == apprenantId:
                print(f"Matière Code : {note.matiereCode}, Note : {note.valeur}")
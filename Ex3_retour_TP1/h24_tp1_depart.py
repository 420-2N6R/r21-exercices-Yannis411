import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

class Etudiant:
    def __init__(self, Id:int, nom:str, programme:str, notes_TP:list[int], notes_Exam:list[int]) -> None:
        self.Id = Id
        self.nom = nom
        self.programme = programme
        self.notes_TP = notes_TP
        self.notes_Exam = notes_Exam

    def calculer_note_final(self):
        moyenne_TP = 0
        moyenne_exam = 0
        try:
            for note_TP in self.notes_TP:
                moyenne_TP += int(note_TP) / 5

            for note_exam in self.notes_Exam:
                moyenne_exam += int(note_exam) / 3
            note_final = (moyenne_TP + moyenne_exam) / 2
        except ValueError:
            print(étudiants)
        return note_final
class Bilan :
    def __init__(self, cours:str, etudiants:list[Etudiant]) -> None:
        self.cours = cours
        self.etudiants = etudiants
        self.moyenne:int
        self.__calculer_moyenne()
        self.taux_succes:int
        self.__calculer_taux_succes()

    def __calculer_moyenne(self):
        total = 0
        for etudiant in self.etudiants:
            total += etudiant.calculer_note_final()
        self.moyenne = total / len(étudiants)
    def __calculer_taux_succes(self):
        etudiant_reussi = 0
        for etudiant in étudiants:
            if etudiant.calculer_note_final() >= 60:
                etudiant_reussi +=1
        self.taux_succes = (etudiant_reussi / len(étudiants)) * 100

    def __str__(self) -> str:
        print(f"{self.moyenne} {self.taux_succes}")


def lire_CSV_notes(path) -> list[Etudiant]:

        with open(path, "r", encoding='utf-8') as f_lu:
            csv_reader = csv.reader(f_lu,delimiter=';')
            next(csv_reader)
            liste_etudiants = []
            try:
                next(csv_reader)
                for ligne in csv_reader :
                    nouveau_etudiants = Etudiant(ligne[0], ligne[1], ligne[2], ligne[3:8], ligne[8:10])
                    liste_etudiants.append(nouveau_etudiants)
                    nouveau_etudiants.calculer_note_final()

            except ValueError:
                print(ligne[1])
            return liste_etudiants

if __name__ == "__main__" :
    nom_cours = "Prog 2"
    étudiants = lire_CSV_notes("resultats_evaluation.csv")
    
    bilan_cours = Bilan(nom_cours, étudiants)

print(bilan_cours.moyenne, bilan_cours.taux_succes)

# À la fin de cette partie, on veut imprimer : 
#           - Le nombre d'étudiants ayant passé.
#           - La moyenne de ces étudiants
#           - La moyenne de tous les étudiants
#           - Le taux de succès au cours (pourcentage d'étudiants ayant passé)

# Vous devez aussi imprimer les étudiants, leur id, et s'ils on passé ou non dans le terminal en imprimant l'instance de bilan.
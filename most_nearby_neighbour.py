from levenshtein_distance import levenshtein_distance
from color import color

NombreDeSequences = int(input("Entrez le nombre de séquences d'ADN à classer: "))

Sequences = []
for _ in range(NombreDeSequences):
    Sequence = input("Entrez la séquence d'ADN numéro " + str(_+1) + ": ")
    Sequences.append(Sequence)

print("\nLes séquences que vous avez entré:" + str(Sequences) + "\n")

# implémentation de l'algorithme
Seuil = int(input("Entrer le seuil t: "))
Classes = []
Classe1 = []
Classe1.append(Sequences[0])
Classes.append(Classe1)
j = 1
m = 1
while j < len(Sequences):
    Distances = []
    for classe in Classes:
        DistancesEntreLesSequences = []     
        for sequence in classe:
            distance = levenshtein_distance(sequence, Sequences[j])
            DistancesEntreLesSequences.append(distance)
        DistanceEntreLaClasseEtLaSequence = min(DistancesEntreLesSequences)
        Distances.append(DistanceEntreLaClasseEtLaSequence)
    DistanceMinimale = min(Distances)
    PositionDeLaDistanceMinimal = Distances.index(DistanceMinimale)
    if DistanceMinimale <= Seuil:
        ClassDeLaSequence = Classes[PositionDeLaDistanceMinimal]
        ClassDeLaSequence.append(Sequences[j])
    else:
        Classes.append([]) # nouvelle classe pour Sequences[j]
        Classes[m].append(Sequences[j]) # insertion de la sequence dans la nouvelle classe
        m += 1
    j += 1

#Affichage
print()
for classe in Classes:
    GroupeClass = color.UNDERLINE + "Classe " + str(Classes.index(classe)+1) + ":" + color.END
    for sequence in classe:
        GroupeClass += " " + sequence + ", "
    print(GroupeClass)
print()

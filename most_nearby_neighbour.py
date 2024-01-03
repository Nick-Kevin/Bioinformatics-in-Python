from levenshtein_distance import levenshtein_distance

NumberOfSequences = int(input("Enter the number of ADN sequences: "))

Sequences = []
for _ in range(NumberOfSequences):
    Sequence = input("Enter the ADN sequence " + str(_+1) + ": ")
    Sequences.append(Sequence)

print("All sequences you'd enter:", Sequences)

DoorStep = int(input("Enter the doorstep: "))
Classes = []
Classe1 = []
Classe1.append(Sequences[0])
Classes.append(Classe1)
j = 1
m = 1
while j < len(Sequences):
    DansUneClasse = False   
    for classe in Classes:
        Distancese = []
        for sequence in classe:
            distance = levenshtein_distance(sequence, Sequences[j])
            Distancese.append(distance)
        minD = Distancese[0]
        for dist in Distancese:
            if dist < minD:
                minD = dist
        if minD <= DoorStep:
            classe.append(Sequences[j])
            DansUneClasse = True
            break
    if DansUneClasse == False:
        Classes.append([]) # new class for Sequences[j]
        Classes[m].append(Sequences[j]) # insert the sequence in the new class
    j += 1

for classe in Classes:
    GroupeClass = "Classe " + str(Classes.index(classe)+1) + ":"
    for sequence in classe:
        GroupeClass += " " + sequence + ", "
    print(GroupeClass)
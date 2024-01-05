def levenshtein_distance(PremiereSequence, DeuxiemeSequence):
    ApresDerniereLigne = len(DeuxiemeSequence) + 1
    ApresDerniereColonne = len(PremiereSequence)+1
    Distances = [[] for _ in range(ApresDerniereLigne)]    
    Distances[0].append(0)
    for Ligne in range(1, ApresDerniereLigne):
        Distances[Ligne].append(Distances[Ligne-1][0] + 1)
    for Colonne in range(1, ApresDerniereColonne):
        Distances[0].append(Distances[0][Colonne-1]+1)
    for Ligne in range(1, len(Distances)):
        for Colonne in range(1, ApresDerniereColonne):
            if PremiereSequence[Colonne-1] != DeuxiemeSequence[Ligne-1]:
                distance1 = Distances[Ligne-1][Colonne-1] + 1
            else:
                distance1 = Distances[Ligne-1][Colonne-1]
            distance2 = Distances[Ligne-1][Colonne] + 1
            distance3 = Distances[Ligne][Colonne-1] + 1
            Distances[Ligne].append(min(distance1, distance2, distance3))
    DistanceDeLevenshtein = Distances[len(DeuxiemeSequence)][len(PremiereSequence)]
    print("La distance de Levenshtein entre '"
        +PremiereSequence
        +"' et '"
        + DeuxiemeSequence
        +"' est: Dl("
        +PremiereSequence
        +","
        +DeuxiemeSequence
        +") =",
        DistanceDeLevenshtein
    )
    return DistanceDeLevenshtein

PremiereSequence = input("Entrez la premiere séquence d'ADN: ")
DeuxiemeSequence = input("Entrez la deuxième séquence d'ADN: ")

levenshtein_distance(PremiereSequence, DeuxiemeSequence)

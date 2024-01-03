print("\nCe module calcul la distance de Levenshtein entre 2 séquences d'ADN\n")

FirstSequence = input("Entrer la première séquence: ")
SecondSequence = input("Entrer la deuxième séquence: ")

def minimum(arg1, arg2, arg3):
    if arg1 < arg2:
        if arg1 < arg3:
            return arg1
        else: return arg3
    elif arg2 < arg3:
        return arg2
    else: return arg3

def distance_levenshtein(premiereSequence, deuxiemeSequence):
    numeroDeLApresDerniereLigne = len(deuxiemeSequence) + 1
    numeroDeLApresDerniereColonne = len(premiereSequence)+1
    Distance = [[] for _ in range(numeroDeLApresDerniereLigne)]    
    Distance[0].append(0)
    for ligne in range(1, numeroDeLApresDerniereLigne):
        Distance[ligne].append(Distance[ligne-1][0] + 1)
    for colonne in range(1, numeroDeLApresDerniereColonne):
        Distance[0].append(Distance[0][colonne-1]+1)
    for ligne in range(1, len(Distance)):
        for colonne in range(1, numeroDeLApresDerniereColonne):
            if premiereSequence[colonne-1] != deuxiemeSequence[ligne-1]:
                dist1 = Distance[ligne-1][colonne-1] + 1
            else:
                dist1 = Distance[ligne-1][colonne-1]
            dist2 = Distance[ligne-1][colonne] + 1
            dist3 = Distance[ligne][colonne-1] + 1
            Distance[ligne].append(minimum(dist1, dist2, dist3))
    LaDistanceDeLevenshtein = Distance[len(deuxiemeSequence)][len(premiereSequence)]
    print("La distance de Levenshtein entre est:")
    print("Dl(" + premiereSequence + "," + deuxiemeSequence + ") =", LaDistanceDeLevenshtein)
    return LaDistanceDeLevenshtein
    
distance_levenshtein(FirstSequence, SecondSequence)
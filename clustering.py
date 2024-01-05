from levenshtein_distance import levenshtein_distance
from color import color

# sequences: ensemble de mots
# mots ou sequence: ADN

def cherher(tableau, valeur):
    for Ligne in tableau:
        for Sequence in Ligne:
            if valeur == Sequence:
                return { 'ligne': tableau.index(Ligne), 'colonne': Ligne.index(valeur)}
    return { 'ligne': -1, 'colonne': -1 }

def prendre_le_minimum_dans_le_tableau(TableauDeDistances):
    DistancesSansZero = []
    for Ligne in TableauDeDistances:
        for Sequence in Ligne:
            if isinstance(Sequence, int) and Sequence > 0:
                DistancesSansZero.append(Sequence)
    minimum = min(DistancesSansZero)
    return minimum

def prendre_les_sequences(tableau, distance):
    Position = cherher(tableau, distance)    
    ColonneDeLaSequence = Position['colonne']
    PremiereSequence = tableau[0][ColonneDeLaSequence]
    LigneDeLaDistance = Position['ligne']
    DeuxiemeSequence = tableau[LigneDeLaDistance][0] 
    return { 'first_sequence': PremiereSequence, 'second_sequence': DeuxiemeSequence }

def une_seule_classe_pour_tous_objects(tableau, tableau_de_sequence):
    NombreDeSequences = 0
    for Ligne in tableau:
        for sequence in tableau_de_sequence:
            if Ligne == sequence:
                NombreDeSequences += 1
    if NombreDeSequences != len(tableau_de_sequence):
        return False
    return True

def est_une_classe(valeur):
    if isinstance(valeur, list) == False:
        return False
    return True

def distance_entre_classe_et_sequence(classe, sequence):
    Distances = []
    for item in classe:
        distance = levenshtein_distance(item, sequence)
        Distances.append(distance)
    minimum = min(Distances)
    return minimum

def distance_entre_classes(premiere_classe, deuxieme_classe):
    Distances = []
    for sequence in deuxieme_classe:
        distance = distance_entre_classe_et_sequence(premiere_classe, sequence)
        Distances.append(distance)
    print("Distances = ", Distances )
    minimum = min(Distances)
    return minimum

def fusionner_classes(premiere_classe, deuxieme_classe):
    Fusion = []
    for sequence in deuxieme_classe:
        Fusion.append(sequence)
    for sequence in premiere_classe:
        Fusion.append(sequence)    
    return Fusion

def creer_tableau(sequences):
    Tableau = []
    PremiereLigne = []
    PremiereLigne.append("")
    for sequence in sequences:
        PremiereLigne.append(sequence)
    Tableau.append(PremiereLigne)
    # ajout de nouvelles lignes dans le tableau
    for sequence in sequences:
        NouvelleLigne = []
        NouvelleLigne.append(sequence)
        for item in sequences:
            distance = 0
            if est_une_classe(item) and est_une_classe(sequence):
                distance = distance_entre_classes(item, sequence)
            elif est_une_classe(item):
                distance = distance_entre_classe_et_sequence(item, sequence)
            elif est_une_classe(sequence):
                distance = (distance_entre_classe_et_sequence(sequence, item))
            else:
                distance = levenshtein_distance(item, sequence)
            NouvelleLigne.append(distance)
        Tableau.append(NouvelleLigne)
    return Tableau

def creer_sequences_pour_un_tableau(DernieresSequences, NouvelleClasse):
    NewSequences = []
    for item in DernieresSequences:
        if est_une_classe(item):
            compteur = 0
            for sequence in NouvelleClasse:
                for i in item:
                    if i == sequence:
                        compteur += 1
            if(compteur == 0):
                NewSequences.append(item)    
        else:
            DansLaNouvelleClasse = False
            for sequence in NouvelleClasse:
                if sequence == item:
                    DansLaNouvelleClasse = True
            if DansLaNouvelleClasse == False:
                NewSequences.append(item)
    NewSequences.append(NouvelleClasse)
    return NewSequences

def prendre_la_plus_longue_sequence_d_une_colonne(tableau, Colonne):
    NombreDeCaractereMaximum = len(str(tableau[0][Colonne]))
    for Ligne in tableau:
        if len(str(Ligne[Colonne])) > NombreDeCaractereMaximum:
            NombreDeCaractereMaximum = len(str(Ligne[Colonne]))
    return NombreDeCaractereMaximum

def afficher_tableau(tableau):
    Afficher = ""
    MaximumDeCharacteresPourLesColonnes = []
    NombreDeColonneDuTableau = len(tableau[0])
    for numero_colonne in range(NombreDeColonneDuTableau):
        MaxCharacteres = prendre_la_plus_longue_sequence_d_une_colonne(tableau, numero_colonne)
        MaximumDeCharacteresPourLesColonnes.append(MaxCharacteres)
    for Ligne in tableau:
        espace = " "
        AfficherLigne = ""
        NumColonne = 0
        for Column in Ligne:
            NombreCharacteres = len(str(Column))
            AfficherColonne = ""
            NombreDesEspaces = MaximumDeCharacteresPourLesColonnes[NumColonne] - NombreCharacteres
            for _ in range(NombreDesEspaces):
                AfficherColonne += espace
            AfficherColonne += str(Column) + "| "
            AfficherLigne += AfficherColonne
            NumColonne += 1
        Afficher += AfficherLigne + "\n"
    return Afficher

def principale():
    NombreDeSequencesADN = int(input("Entrer le nombres de séquences d'ADN: "))
    Sequences = []
    for compteur in range(NombreDeSequencesADN):
        sequence = input("Entre la séquence num " + str(compteur+1) + ": ")
        Sequences.append(sequence)

    print("Les séquences que vous avez entré: ", Sequences)
    print()

    Classes = []
    DernieresSequences = Sequences
    # implémentation de l'algorithme
    while True:
        Tableau = creer_tableau(DernieresSequences)
        print(color.BOLD + color.UNDERLINE + "Tableau de distances:" + color.END)
        print(afficher_tableau(Tableau))
        DistanceMinimale = prendre_le_minimum_dans_le_tableau(Tableau)        
        PositionDesSequences = prendre_les_sequences(Tableau, DistanceMinimale)
        PremiereSequence = PositionDesSequences['first_sequence']
        DeuxiemeSequence = PositionDesSequences['second_sequence']
        print("La distance minimale est: "+ color.BOLD +"Dl("+ str(PremiereSequence) + ","
            + str(DeuxiemeSequence) + ") =" + str(DistanceMinimale) + color.END)
        # creer une nouvelle classe
        NouvelleClasse = []
        if est_une_classe(PremiereSequence) and est_une_classe(DeuxiemeSequence):
            NouvelleClasse = fusionner_classes(PremiereSequence, DeuxiemeSequence)
        elif est_une_classe(PremiereSequence):
            for sequence in PremiereSequence:
                NouvelleClasse.append(sequence)
            NouvelleClasse.append(DeuxiemeSequence)
        elif est_une_classe(DeuxiemeSequence):
            for sequence in DeuxiemeSequence:
                NouvelleClasse.append(sequence)
            NouvelleClasse.append(DeuxiemeSequence)
        else:
            NouvelleClasse = [DeuxiemeSequence, PremiereSequence]
        Classes.append(NouvelleClasse)
        print(color.BOLD + "La nouvelle classe:" + str(NouvelleClasse) + color.END)
        print()
        DernieresSequences = creer_sequences_pour_un_tableau(DernieresSequences, NouvelleClasse)
        DerniereClasseTrouvee = Classes[len(Classes)-1]
        if une_seule_classe_pour_tous_objects(DerniereClasseTrouvee, Sequences):
            break
    
    # affichage du diagramme des classes
    print("\n\n" + color.BOLD + "RESULTATS FINALS" + color.END)
    PositionDeLaDerniereClasse = len(Classes)-1
    SequenceLaPlusAGauche = Classes[PositionDeLaDerniereClasse][0]
    niveau = 0
    ClasseNiveau = []
    for classe in reversed(Classes):
        if classe[0] == SequenceLaPlusAGauche:
            ClasseNiveau.append(classe)
            AffichageDeClasseNiveau = ""
            for item in reversed(ClasseNiveau):
                AffichageDeClasseNiveau += str(item) + "   |   "
            niveau += 1
            print("Classe niveau " + str(niveau) + ": |   " + AffichageDeClasseNiveau)
            ClasseNiveau = []
        else:
            ClasseNiveau.append(classe)
    niveau += 1
    DerinierNiveau = "Classe niveau " + str(niveau) + ": |   "
    for sequence in Classes[len(Classes)-1]:
        SequenceEnClasse = [sequence]
        DerinierNiveau += str(SequenceEnClasse) + "   |   "
    print(DerinierNiveau)

principale()

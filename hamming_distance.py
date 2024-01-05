print("\nCe module calcul la distance de Hamming entre deux séquence d'ADN entrer par l'utilisatuer.")

while True:
    print("\nNB: Le nombre de nucléotide des deux séquences doivent être égale.")
    PremiereSequence = input("\tEntrez la première séquence: ")
    DeuxièmeSequence = input("\tEntrez la deuxième séquence: ")
    if len(PremiereSequence) == len(DeuxièmeSequence):
        break

Distance = 0
for nucleotide in range(len(PremiereSequence)):
    if PremiereSequence[nucleotide] != DeuxièmeSequence[nucleotide]:
        Distance += 1

print("\nThe hamming distance between '" + PremiereSequence +"' and '" + DeuxièmeSequence + "' is:")
print("Dh(" + PremiereSequence + "," + DeuxièmeSequence + ") =", Distance)
print("")


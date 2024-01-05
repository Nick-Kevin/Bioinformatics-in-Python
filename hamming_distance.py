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

print("\nLa distance de Hamming entre '" + PremiereSequence +"' et '" + DeuxièmeSequence + "' est:")
print("Dh(" + PremiereSequence + "," + DeuxièmeSequence + ") =", Distance)
print("")


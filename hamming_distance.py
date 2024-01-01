print("\nThis script calculates hamming distance between two ADN sequences.")

while True:
    print("\nNB: The first and second sequences mmust have the same length.")
    FirstSequence = input("\tEnter the first sequence: ")
    SecondSequence = input("\tEnter the second sequence: ")
    if len(FirstSequence) == len(SecondSequence):
        break

print("The first sequence is:", FirstSequence,", and the second one is:", SecondSequence)

Distance = 0
for nucleotide in range(len(FirstSequence)):
    if FirstSequence[nucleotide] != SecondSequence[nucleotide]:
        Distance += 1

print("\nThe hamming distance between '" + FirstSequence +"' and '" + SecondSequence + "' is:", Distance)
print("")
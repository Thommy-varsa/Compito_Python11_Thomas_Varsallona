base = int(input("Inserisci la base: "))
esponente = int(input("Inserisci l'esponente: "))

for i in range(esponente + 1):
    print(base**i, end=" ")
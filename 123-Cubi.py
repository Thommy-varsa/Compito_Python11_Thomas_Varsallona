n = int(input("Inserisci un numero: "))

for i in range(1, int(n**(1/3)) + 1):
    print(i**3, end=" ")
a = int(input("Inserisci il primo numero (a): "))
b = int(input("Inserisci il secondo numero (b): "))

if b < a:
    print("Errore: b deve essere maggiore o uguale ad a.")
else:
    somma = sum(range(a, b + 1))
    print("La somma dei numeri tra", a, "e", b, "è:", somma)
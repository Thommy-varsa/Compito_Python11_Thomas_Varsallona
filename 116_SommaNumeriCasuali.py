import random
def somma_numeri_casuali():
    try:
        N = int(input("Inserisci un numero intero positivo: "))
        if N <= 0:
            print("Il numero deve essere positivo.")
            return
        
        numeri = [random.randint(0, 100) for _ in range(N)]
        somma = sum(numeri)
        
        print(f"Numeri generati: {numeri}")
        print(f"Somma dei numeri: {somma}")
    except ValueError:
        print("Errore: Inserisci un numero intero valido.")

somma_numeri_casuali()
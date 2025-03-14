N = int(input("Inserisci un numero: "))

if N > 1:
    for i in range(2, N):
        if N % i == 0:
            print(N, "non è un numero primo")
            break
    else:
        print(N, "è un numero primo")
else:
    print(N, "non è un numero primo")
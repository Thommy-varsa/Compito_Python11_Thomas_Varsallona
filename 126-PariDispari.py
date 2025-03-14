for i in range(1, 12):
    if i % 2 == 0:
        print("*")  # Per i numeri pari, stampa un solo asterisco
    else:
        print("*" * ((i + 1) // 2))  # Per i numeri dispari, aumenta gli asterischi
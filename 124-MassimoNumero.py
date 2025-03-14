n = int(input("Quanti numeri vuoi inserire? "))
max_num = int(input("Inserisci il primo numero: "))

for i in range(1, n):
    num = int(input("Inserisci un numero: "))
    if num > max_num:
        max_num = num

print("Il numero massimo inserito è:", max_num)
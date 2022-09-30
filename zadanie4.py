# Program wyświetlający nty wyraz ciągu fibonacciego

nty_wyraz = int(input("Ile wyrazów wsytępuje w ciągu? "))

# Pierwsze dwa wyrazy ciągu
n1, n2 = 0, 1
count = 0

# Sprawdza czy liczba wayrazów ciągu jest odpowiednia
if nty_wyraz <= 0:
   print("Podaj liczbę większą od zera")
# Jeśli jeden wyraz zwraca 1
elif nty_wyraz == 1:
   print("Ciąg Fibonacciego ",nty_wyraz,":")
   print(n1)
#Podaje ciąg
else:
   print("Ciąg Fibonacciego:")
   while count < nty_wyraz:
       print(n1)
       nty = n1 + n2
       # Aktualizowane są wartości dla n1 i n2
       n1 = n2
       n2 = nty
       count += 1
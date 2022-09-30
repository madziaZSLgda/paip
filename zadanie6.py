import math

numer = int(input("Podaj liczbę: "))
logarytm = math.log(numer,3)
if logarytm - int(logarytm) != 0:
    print("Nie jest potęga liczby 3")
else:
    print("Jest potęga liczby 3")
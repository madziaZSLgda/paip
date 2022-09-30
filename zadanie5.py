print("Wybierz tryb:")
print("1. Z binarnego na decymalny")
print("2. Z decymalnego na binarny")
while True:
    choice = input("Wybierz 1/2: ")
    if choice in ['1', '2']:

        if  choice == '1':
            numer = input("Podaj liczbę: ")
            print(int(numer,2))
            break

        if choice == '2':
            numer2 = int(input("Podaj liczbę: "))
            print(bin(numer2).replace("0b", ""))
            break

    else:
        print("Podaj dobrą liczbę")










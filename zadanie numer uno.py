
import math



def findRoots(a, b, c):

    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))


    if dis_form > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis_form == 0:
        print(" real and same roots")
        print(-b / (2 * a))


    else:
        print("Pierwiastki")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


a = int(input('Podaj a:'))
b = int(input('Podaj b:'))
c = int(input('Podaj c:'))


if a == 0:
    print("Podaj poprawne wartości")

else:
    findRoots(a, b, c)

import math

n = 0
r = 0

print("Combinaciones y Permutaciones: ")
print("¿Que quieres hacer?")
print("Permutación Ingresa 1: ")
print("Combinación Ingresa 2: ")
print("--------------------------------------------")

eleccion = int(input())


if eleccion == 1:
    print("--------------------------------------------")
    print("Elegiste Permutación")
    print("Con Repeticion o Sin repeticion?")
    print("Con Repeticion Ingresa 1: ")
    print("Sin Repeticion Ingresa 2: ")
    print("--------------------------------------------")
    eleccion2 = int(input())

    if eleccion2 == 1:
        print("--------------------------------------------")
        print("P(n,r)=n!/(n-r)!")
        print("Ingresa valor de n y r")
        n = int(input("n: "))
        r = int(input("r: "))
        respt = math.factorial(n) / math.factorial(n - r)
        print("Respuesta:", "P(", n, ",", r, ") = ", respt)
        print("--------------------------------------------")
        print("Reinicia el programa")

    elif eleccion2 == 2:
        print("--------------------------------------------")
        print("P(n)= n!")
        print("Ingresa valor de n")
        n = int(input("n: "))
        respt = math.factorial(n)
        print("Respuesta:", "P(", n, ") = ", respt)
        print("--------------------------------------------")
        print("Reinicia el programa")

    else:
        print("--------------------------------------------")
        print("No elegiste una de las opciones corre de nuevo el programa")

elif eleccion == 2:
    print("--------------------------------------------")
    print("Elegiste Combinación")
    print("Con Repeticion o Sin repeticion?")
    print("Con Repeticion Ingresa 1: ")
    print("Sin Repeticion Ingresa 2: ")
    print("--------------------------------------------")
    eleccion3 = int(input())

    if eleccion3 == 1:
        print("--------------------------------------------")
        print("C(n+r-1,r)=(n+r-1)!/r!*(n-1)!")
        print("Ingresa valor de n y r")
        n = int(input("n: "))
        r = int(input("r: "))
        respt = math.factorial(n + r - 1) / (math.factorial(r) * math.factorial(n - 1))
        print("Respuesta:", "C(", n, ",", r, ") = ", respt)
        print("--------------------------------------------")
        print("Reinicia el programa")

    elif eleccion3 == 2:
        print("--------------------------------------------")
        print("C(n,r)=n!/r!*(n-r)!")
        print("Ingresa valor de n y r")
        n = int(input("n: "))
        r = int(input("r: "))
        respt = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        print("Respuesta:", "C(", n, ",", r, ") = ", respt)
        print("--------------------------------------------")
        print("Reinicia el programa")

    else:
        print("--------------------------------------------")
        print("No elegiste una de las opciones corre de nuevo el programa")

else:
    print("No elegiste una de las opciones corre de nuevo el programa")

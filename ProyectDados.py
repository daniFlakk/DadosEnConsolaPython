import random

def dados():
    dado1 = int(random.random()*10)%6+1
    dado2 = int(random.random()*10)%6+1
    print("El primer dado es: ",dado1)
    print("El segundo dado es: ",dado2)
    print("El valor de la suma de los dados es: ",dado1 + dado2)

def menu():
    election = input("¿Desea lanzar nuevamente los dados? \n1.SI \n2.NO")
    if election == '1':
        dados()
        menu()
    else:
        print("Termino")

dados()
menu()






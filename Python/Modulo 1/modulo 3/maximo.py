import random

#tira los dados
repite = 1

def tirar_dados():
    dado_1 = int(random.random()*10%6+1)
    dado_2 = int(random.random()*10%6+1)
    print("los dados fueron tirados, valores :",dado_1," y " , dado_2)
    repite = int(input("desea tirar nuevamente los dados ? [1:Si / 2:No]"))
    return repite

while(repite == 1):
    repite = tirar_dados()


print("Adios")
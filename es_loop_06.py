#Crea un programma che dice “Di quale forma geometrica vuoi calcolare il 
# perimetro? 
# Quadrato, rettangolo o triangolo?" e quindi restituire il valore desiderato.
#Affinché tre numeri possano essere le lunghezze dei lati di un triangolo è necessario che 
# siano tutte positive e che ciascuna sia inferiore alla somma delle altre due


def check_somma_l (lato1, lato2, lato3):
    if (lato1 < lato2 + lato3) and (lato2 < lato1+lato2) and (lato3 < lato1+ lato2):
        return True
    else:
        return False


print ("Di quale forma geometrica vuoi calcolare il perimetro? Quadrato, rettangolo o triangolo?")
forma_g = input ()

while (forma_g.lower() not in ["quadrato","rettangolo","triangolo"]):
    print ("La forma geometrica non è valida. Fornire una forma geometrica tra quadrato, rettangolo o triangolo")
    forma_g = input ()

if (forma_g.lower() == "quadrato"):
    print ("Fornire la misura del lato")
    lato_q = int (input ())
    perimetro_q = 4* lato_q
    print (f"Il perimetro del quadrato è {perimetro_q}")
elif (forma_g.lower() == "triangolo"):
    print ("Fornire le misure dei 3 lati")
    lato1_t = int (input ())
    lato2_t = int (input ())
    lato3_t = int (input ())
    while (lato1_t < 0 or lato2_t < 0 or lato3_t < 0) or (not check_somma_l (lato1_t, lato2_t, lato3_t)):
        print ("I lati forniti non sono validi. Fornire 3 misure positive dei lati")
        lato1_t = int (input ())
        lato2_t = int (input ())
        lato3_t = int (input ())
    perimetro_t = (lato1_t+ lato2_t + lato3_t)
    print (f"Il perimetro del triangolo è {perimetro_t}")
else:
    print ("Fornire la base e l'altezza del rettangolo")
    base = int (input ())
    altezza = int (input ())
    perimetro_r = (2* base) + (2*altezza)
    print (f"Il perimetro del rettangolo è {perimetro_r}")



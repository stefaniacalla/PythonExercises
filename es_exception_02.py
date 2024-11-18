#Scrivere un programma che legga da tastiera un valore nell'intervallo [1,12],
#  la cui corrispondenza al numero è il rispettivo mese e, 
# stampi la stagione relativa al mese inserito. 
# Il codice deve cercare di intercettare possibili situazioni
# di errore dovute a input fuori dall’intervallo predefinito.


""" def stagione (n):
    try:
        if (n == int (n)):
            if (n>0) and (n<13):
                if (1<=n<=3):
                    print ("La stagione è Inverno")
                elif (3<n<=6):
                    print ("La stagione è Primavera")
                elif (6<n<=9):
                    print ("La stagione è Estate")
                else:
                    print ("La stagione è Autunno")
            else:
                raise OutOfRangeException
        else:
            raise NotIntException
    except OutOfRangeException as e:
        print ("Il numero inserito è fuori dall'intervallo")
    except NotIntException as e:
        print ("Il numero inserito non è un intero")
    except:
        print ("Altro errore non riconosciuto") """

def stagione (n):
    try:
        if (n == int (n)):
            if (n>0) and (n<13):
                if (1<=n<=3):
                    print ("La stagione è Inverno")
                elif (3<n<=6):
                    print ("La stagione è Primavera")
                elif (6<n<=9):
                    print ("La stagione è Estate")
                else:
                    print ("La stagione è Autunno")
            else:
                raise Exception("outofrange")
        else:
            raise Exception("notaint")
    except Exception as e:
        if str(e) == "outofrange":
            print ("Il numero inserito è fuori dall'intervallo")
        elif str(e) == "notaint":
            print ("Il numero inserito non è un intero")
        else:
            print ("Altro errore non riconosciuto")


def main ():
    print ("Digitare un numero per cui si vuole conoscere la stagione")
    n = float (input ())
    stagione (n)



main ()
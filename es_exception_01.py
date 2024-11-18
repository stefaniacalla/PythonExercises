#Scrivere del codice in Python per calcolare la radice quadrata di 
# un numero intero positivo, inserito da tastiera. 
# Il codice deve gestire anche un caso di errore,
# cioè viene inserito un numero non intero.


def radice (num):
    try:
        if (num == int (num)):
            ris = num ** (1/2)
            print (f"La radice quadata è {ris}")
        else:
            raise 
    except:
        print ("Il numero non è intero")
    

def main ():
    print ("Digitare un numero")
    n = float (input())
    radice (n)

main ()
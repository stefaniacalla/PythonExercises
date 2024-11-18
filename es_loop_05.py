#Trova il valore massimo tra tre numeri forniti in input 

""" print ("Digita 3 numeri")
num1= int (input ())
num2= int (input ())
num3= int (input ())

if (num1 > num2 and num1 > num3):
    print (f"Il numero massimo è {num1}")
elif (num2 > num1 and num2 > num3):
    print (f"Il numero massimo è {num2}")
else:
    print (f"Il numero massimo è {num3}") """


def mass (l=[]):
    mx = 0
    for i in l:
        if (i>mx):
            mx = i
    return print (mx)

def main ():
    i = 0     #contatore
    l = []    #lista che contiene i numeri
    print ("Quanti numeri vuoi inserire?")
    num_l = int (input ())  #num_l: numeri della lista
    while (i < num_l-1):
        print ("")
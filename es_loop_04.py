#Dati due numeri di input, determina se sono entrambi pari o dispari 

print ("Digita 2 numeri")
num1= int (input ())
num2= int (input ())

if (num1 % 2 == 0 and num2 % 2==0):
    print ("I numeri sono entrambi pari")
elif (num1 % 2 != 0 and num2 % 2!=0):
    print ("I numeri sono entrambi dispari")
else:
    print ("Un numero è pari e l'altro dispari")

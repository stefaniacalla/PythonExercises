print ("Fornire due numeri compresi tra 0 e 9999")
num1 = int (input ())
num2 = int (input ())

while (num1 <0 or num1 > 9999 or num2 <0 or num2 > 9999):
    print ("I numeri non sono validi. Digitare nuovi due numeri tra 0 e 9999")
    num1 = int (input ())
    num2 = int (input ())

if (num1 == num2):
    print ("I due numeri sono uguali")
elif (num1 != num2) and (num1 > num2):
    print ("I due numeri sono diversi. Il primo numero è maggiore del secondo")
else:
    print ("I due numeri sono diversi. Il secondo numero è dmaggiore del primo")

if (num1 % 2 == 0 and num2 % 2 == 0 ):
    print ("I due numeri sono pari e sono: " + str (num1) + " e " + str (num2))
elif (num1 % 2 == 0 and num2 % 2 != 0 ):
    print ("Il primo numero è pari ed è: " + str (num1) + " . Il secondo numero è dispari ed è: " + str (num2))
elif (num1 % 2 != 0 and num2 % 2 == 0 ):
    print ("Il primo numero è dispari ed è: " + str (num1) + " . Il secondo numero è pari ed è: " + str (num2))
else:
    print ("I due numeri sono dispari e sono: " + str (num1) + " e " + str (num2))

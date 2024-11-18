#Scrivere una funzione in cui, inserendo una stringa, si stamperà una
#versione inversa della stessa stringa (es. "abcd" diventerà "dcba")


def inversa (s):
    res = ''
    for i in s:
        res = i + res
    return res

def main ():
    print ("Digitare una parola")
    s = input ()
    print ("La parola inversa è: ")
    print (inversa (s))
 


main ()
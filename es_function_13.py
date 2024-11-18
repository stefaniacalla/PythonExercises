#Scrivere una funzione che restituisca i numeri di sequenza di Fibonacci, 
# entro una soglia specifica impostata dall'utente in input 
# ("quanti valori vuoi vedere?") 
# es. input: 7 → output: 1, 1, 2, 3, 5, 8, 13



def fib (max_len):
    f = [1,1]
    for i in range(0, max_len-2):
        f.append(f [i] + f[(i+1)])
    return f

    
def main ():
    print ("Quanti valori vuoi vedere?")
    val = int (input ())
    print( fib (val) )

main ()


''''
scrivere la propria versione della funzione length

def my_len (lis):
    c=0
    for i in lis:
        c+=1
    return c

print (my_len ([5,7,8,8,0,4,7]))
'''

'''Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output 
una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

def l_in (l):
    l_out = [len (i) for i in l]  #with list comprehension
    #for i in l:
    #    l_out.append(len(i))
    return l_out

print (l_in (['ape','casa']))
'''


'''Scrivi una funzione che, data una stringa come parametro, 
restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun 
carattere componente la stringa.

Per fare un esempio, data una stringa "ababcc", 
otterremo in risultato {"a": 2, "b": 2, "c": 2}'''

def freq (str):
    freq_char = {}
    for i in str:
        if (i in freq_char):
            freq_char [i] += 1
        else:
            freq_char [i] = 1
    return freq_char

print (freq ('casa'))
    
'''
Scrivere un programma che 
chieda all’utente le lunghezze dei lati di un rettangolo 
e calcoli e visualizzi, 
scegliendo da un menu le possibili seguenti operazioni: 
l’area , 
il perimetro, 
la diagonale.
'''
#import delle librerie per radice e potenza
from math import sqrt as rad
from math import pow


#funzione calcolo perimetro
def perimetro(lato_1, lato_2):
    return (lato_1 + lato_2) * 2

#funzione calcolo area
def area(lato_1, lato_2):
    return lato_1 * lato_2

#funzione per il calcolo della diagonale
def diagonale(lato_1, lato_2):
    return rad(pow(lato_1, 2) + pow(lato_2, 2))
    

#richiesta dati all'utente
lato_1 = int(input('inserisci la lunghezza del primo lato: '))
lato_2 = int(input('inserisci la lunghezza del secondo lato: '))

#variabile per ciclo while
conferma = True

#inizio ciclo while
while(conferma):
    print('scegli l\'operazione desiderata: ')

    print('1. perimetro')
    print('2. area')
    print('3. diagonale')
    
    #input valore scelta dell'utente
    scelta = int(input('la tua scelta: '))
    
    if scelta == 1:
        print(perimetro(lato_1, lato_2))
    elif scelta == 2:
        print(area(lato_1, lato_2))
    elif scelta == 3:
        print(diagonale(lato_1, lato_2))
    else:
        print('scelta errata!')
    
    
    #richiesta di contunare all'utente 
    continua = input('vuoi continuare? (si)')
    if continua == 'si':
        conferma = True
    else:
        conferma = False
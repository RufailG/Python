'''
Scrivere un programma in Python che chieda all’utente due numeri interi e poi visualizzi l il risultato
si un’operazione scelta da un menu che conterrà la seguente lista: 
somma, 
differenza, 
prodotto,
valore medio, 
la distanza(valore assoluto della differenza tra i due numeri), 
il valore massimo tra i due, 
il valore minimo, 
la radice quadrata della loro somma, 
la potenza considerando il primo numero come base e il secondo come esponente. 
Mettere come opzione del menu anche visualizzazione di tutti i risultati di tutte le operazioni, 
ottenendo come visualizzazione un incolonnamento ordinato di tutti i risultati
'''
#import delle librerie per radice e potenza
from math import sqrt as rad
from math import pow

#funzione per la somma
def somma(input_1 , input_2):
    print(input_1 + input_2)

#funzione per la differenza
def differenza(input_1 , input_2):
    print(input_1 - input_2)

#funzione per il prodotto
def prodotto(input_1 , input_2):
    print(input_1 * input_2)

#funzione per il vaolre medio
def val_medio(input_1 , input_2):
    print((input_1 + input_2) / 2)

#funzione per la distanza tra i due numeri
def dist(input_1 , input_2):
    print(abs(input_1 - input_2))

#funzione per il valore massimo
def val_max(input_1 , input_2):
    print(max(input_1, input_2))

#funzione per il valore minimo
def val_min(input_1 , input_2):
    print(min(input_1, input_2))

#funzione per la radice
def radice(input_1 , input_2):
    sum = input_1 + input_2
    print(rad(sum))

#funzione per la potenza
def potenza(input_1 , input_2):
    print(pow(input_1, input_2))

#funzione in cui si richiamano tutte le funzioni
def tutto(input_1 , input_2):
    print('somma: ')
    somma(input_1 , input_2)
    print('differenza: ')
    differenza(input_1 , input_2)
    print('prodotto: ')
    prodotto(input_1 , input_2)
    print('valore medio: ')
    val_medio(input_1 , input_2)
    print('distanza: ')
    dist(input_1 , input_2)
    print('valore massimo: ')
    val_max(input_1 , input_2)
    print('valore minimo: ')
    val_min(input_1 , input_2)
    print('radice della somma: ')
    radice(input_1 , input_2)
    print('potenza: ')
    potenza(input_1 , input_2)


    
#richiesta dei vaolri all'utente
input_1 = int(input('inserisci il primo valore intero: \n'))
input_2 = int(input('inserisci il secondo valore intero: \n'))


#variabile per il ciclo while
conferma = True

#inizio ciclo while
while(conferma):

    #inizio menu: 
    print('scegli l\'operazione desiderata: ')

    print('1. somma')
    print('2. differenza')
    print('3. prodotto')
    print('4. valore medio')
    print('5. distanza')
    print('6. max')
    print('7. min')
    print('8. radice quadrata somma')
    print('9. potenza')
    print('10. tutte le operazioni')



    
    #input valore scelta dell'utente
    scelta = int(input('la tua scelta: '))


    #serie di if per la gestione della scelta dell'utente
    if scelta == 1:
        somma(input_1 , input_2)
    elif scelta == 2:
        differenza(input_1 , input_2)
    elif scelta == 3:
        prodotto(input_1 , input_2)
    elif scelta == 4:
        val_medio(input_1 , input_2)
    elif scelta == 5:
        dist(input_1 , input_2)
    elif scelta == 6:
        val_max(input_1 , input_2)
    elif scelta == 7:
        val_min(input_1 , input_2)
    elif scelta == 8:
        radice(input_1 , input_2)
    elif scelta == 9:
        potenza(input_1 , input_2)
    elif scelta == 10:
        tutto(input_1 , input_2)
    else:
        print('scelta errata!')

    #richiesta di contunare all'utente
    continua = input('vuoi continuare? (si)')
    if continua == 'si':
        conferma = True
    else:
        conferma = False

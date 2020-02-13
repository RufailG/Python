'''
Scrivere un programma che legga una stringa e visualizzi i messaggi appropriati, dopo aver
verificato se:
contiene soltanto lettere
contiene soltanto lettere maiuscole
contiene solo lettere minuscole
contiene solo cifre
contiene almeno una lettera maiuscola
contiene almeno 4 lettere minuscole
temina con un punto
'''

#funzione per verifica presenza di numeri
def caratteri(parola):
    check =  any(char.isdigit() for char in parola)
    
    if check:
        print('la parola inserita contiene dei numeri\n')
    else:
        print('la parola inserita contiene solo lettere\n')


#funzione per verifica lettere maiuscole
def maiuscole(parola):
    if parola.isupper:
        print('la parola inserita contiene solo lettere maiuscole\n')
    else:
        print('la parola inserita contiene anche lettere minuscole\n')


#funzione per verifica lettere minuscole
def minuscole(parola):
    if parola.islower:
        print('la parola inserita contiene solo lettere minuscole\n')
    else:
        print('la parola inserita contiene anche lettere maiuscole\n')
        

#funzione per verificare se sono solo numeri
def numeri(parola):
    if parola.isdigit():
        print('la parola contiene solo numeri\n')
    else:
        print('la parola contiene non contiene solo numeri\n')


#funzione controllo almeno una lettera maiuscola
def una_maiuscola(parola):
    check = any(char.isupper() for char in parola)

    if check:
        print('la parola inserita contiene alemno una lettera maiuscola\n')
    else:
        print('la parola inserita non contiene lettere maiuscole\n')


#funzione controllo almeno 4 lettere minuscole
def quattro_min(parola):
    count = int(sum(1 for c in parola if c.islower()))

    if count >= 4:
        print('la parola contiene almeno 4 lettere minuscole\n')
    else:
        print('la parola contine meno di 4 lettere minuscole\n')



#funzione controllo punto finale
def punto(parola):
    if parola[len(parola) - 1] == '.':
        print('la parola termina con un punto.')
    else:
        print('la parola non termina con un punto.')

#richiesta parola all'utente
parola = input('inserisci una parola: \n')


quattro_min(parola)
caratteri(parola)
maiuscole(parola)
minuscole(parola)
numeri(parola)
una_maiuscola(parola)
quattro_min(parola)
punto(parola)

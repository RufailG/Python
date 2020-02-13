'''
Scrivere un programma che 
legga una parola e ne visualizza 
il primo carattere, 
l’ultimo carattere 
e il carattere centrale. 
Se la lunghezza della parola è pari, il programma deve visualizzare il primo dei due caratteri centrali, dal momento che non esiste il carattere centrale.
Contare quante volte una sotto-stringa fornita in input compare nella parola inserita all’inizio.
Verificare se la parola inizia con una sotto-stringa inserita in input o termina con la sotto-stringa inserita
'''
#funzione per trovare la prima lettera
def prima_lettera(parola):
    print('prima lettera: ' + parola[0])

#funzione per trovare l'ultima lettera
def ultima_lettera(parola):
    print('ultima lettera: ' + parola[len(parola) - 1])

#funzion eper trovare la lettera centrale
def lettera_centrale(parola):
    cen = int((len(parola) - 1) / 2)
    print('lettera centrale: ' + parola[cen])

#funzione per il controllo su una sotto stringa
def sotto_stringa(parola, sub_str):
    #conteggio presenza
    times = parola.count(sub_str)
    #variabile booleana per verificare l'iniio
    start = parola.startswith(sub_str)
    #variabile booleana per verificare la fine
    end = parola.endswith(sub_str)
    
    print('la parola ' + sub_str + ' e presente ' + str(times) + ' volte.')
    
    #controllo sulle variabili booleane
    if start:
        print('la aprola inserita iniza con ' + sub_str)
    else:
        print('la aprola inserita non iniza con ' + sub_str)
    
    if end:
        print('la aprola inserita finisce con ' + sub_str)
    else:
        print('la aprola inserita non finisce con ' + sub_str)
    



#richiesta input all'utente
parola = input('inserisci una parola: \n')
sub_str = input('inserire sotto stringa: \n')




#richiamo delle funzioni
prima_lettera(parola)
ultima_lettera(parola)
lettera_centrale(parola)
sotto_stringa(parola, sub_str)

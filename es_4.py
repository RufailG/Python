'''
Scrivere un programma per tradurre i numeri da 1 a 12 nei nomi dei mesi corrispondenti,
visualizzando anche il corrispondente numero di giorni di ciascun mese. Attenti alla visualizzazione
'''


#array mesi e giorni
mesi = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
giorni = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#richiesta numero all'utente
numero_utente = int(input('inserisci un numero da 1 A 12: \n'))


#controllo sul numero scelto dall'utente
if numero_utente > 12 and numero_utente < 1:
    #sta,mpa di un errore
    print('numero errato')
else:
    #stampa dei risultati
    print('Mese: ' + mesi[numero_utente - 1] + '\n')
    print('Giorni: ' + str(giorni[numero_utente - 1]) + '\n')

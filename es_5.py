'''
Scrivere un programma che inserisca una parola in input e ne visualizzi i primi tre caratteri seguiti
da tre punti ancora seguiti dagli ultimi tre caratteri(es. Giornata visualizzazione Gio…ata)
'''

#richiesta parola all'utente
parola = input('inserisci una parola: \n')


#creazione nuova stringa
new_parola = parola[0:3] + '...' + parola[len(parola) - 3 : len(parola)]

#stampa della nuova stringa
print(new_parola)
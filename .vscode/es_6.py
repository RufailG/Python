'''
Scrivere un programma che legga tre stringhe e le visualizzi in ordine alfabetico
'''


#richiesta numero parole all'utente
dim = int(input('inserire numero parole: \n'))

#creazione lista per contenere le parole
parole = []


#ciclo for per inserire parole
for i in range(dim):
    parole.append(input('inserisci parola: \n'))

#metodo per roirdinare le parole
parole = sorted(parole)

#ciclo for per la stampa delle parole ordinate
for i in parole:
    print(i)
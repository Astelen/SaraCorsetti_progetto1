##Hai 60 min per creare un esercizio che rappresenti tutto quello che hai imparato nella settimana precedente,
# riprendi la tabella delle conoscenze per maggiori info.

#Software Bignami: aiuto per la scuola

#esercizio if per numero pari/dispari ed esercizio For
numero_inserito = 0
if numero_inserito%2 == 0:
    print("Il numero e' pari")
elif numero_inserito%2 != 0:
    print("Il numero e' dispari")
    scelta2 = input("Vuoi sapere se e' dispari? Scegli S o N: ")
    if scelta2.lower() == "s":
        for numero in range(3, numero_inserito):
            if numero_inserito % numero != 0:
                print("Il numero e' anche primo, farai un figurone!")
            else: 
                print("Il numero non e' primo.")
    elif scelta2.lower() == "n":
        pass
    else:
        print("Scelta non valida.")
else:
    print("C'e' stato un errore.")
    
#esercizio while
while True:
    scelta = input("Se hai bisogno del Bignami per barare al compito di matematica, digita 21, che e' la risposta universale! Altrimenti digita Esc. ")
    if scelta == "21":
        print("Ci pensa il tuo Bignami informatico!")
    elif scelta.lower() == "esc":
        print("Bugiardo, tutti ne hanno bisogno!")
        break
    else:
        print("Se non sai neanche digitare 21 o Esc, decisamente ti serve il nostro aiuto. Torna al menu' principale.")    








## Andiamo ora a creare un sistema di funzioni che richiami tutte le singole parti che abbiamo creato nel precedente esercizio,
# devono essere usate SOLO funzioni e almeno da 2 decoratori ed essere ripetibile.
import os
import readchar

def Gmenu():
    print('-' * 20)
    print('Gestione negozio')
    print('-' * 20)
    
    print('1. Aggiungi articolo')
    print('2. Mostra carrello')
    print('3. Calcola totale')
    print('4. Stampa scontrino')
    print('5. Togli articolo')
    print('6. Azzera carrello')
    print('7. Esci ')

    while True:
        val1 = input('Inserisci una scelta di menu [1,2,3,4,5,6,7]: ')
        try:
            val1 = int(val1)
        except:
            print('Selezione non valida')
            continue
 
        if val1 < 1 or val1 > 7:
            print('Selezione non valida')
            continue
        else:
            return val1

def Garticolo():
    print('-' * 20)
    print('Aggiungi articolo al carrello')
    print('-' * 20)

    var1 = " ABCDEFGHKIJLMNOPQRSTUVWXYZ01234567890"
    while True:
        var2 = input('Nome ').lstrip().rstrip()
        var3 = True

        if var2 == '':
            continue

        for i in range(0, len(var2), 1):
            if var2[i].upper() not in var1:
                 var3 = False
                 break

        if var3:
            break
        else:
            print('Descrizione articolo non ammessa')
            continue

    while True:
        try:
            var3 = float(input('Prezzo '))
            break
        except:
            print('Prezzo non valido')
            continue

    while True:
        try:
            var4 = int(input('Qta '))
            break
        except:
            print('Quantità non valida')
            continue

    var5 = {}
    var5["Prezzo"] = var3
    var5["Qta"] = var4

    var6 = {var2:var5}
    
    return(var6)

def Mcarrello(var1):
    print('-' * 40)
    print('Composizione carrello della spesa')
    print('-' * 40)

    if not var1:
        input('\nIl carrello della spesa è vuoto, premere INVIO per continuare')
        return

    for a, b in var1.items():
        print(f'Prodotto: {a}\nPrezzo {b['Prezzo']:.2f}\nQta {b['Qta']}\nTotale {float(b['Prezzo']) * int(b['Qta']):.2f}')
        print('')

    input('Premere INVIO, per continuare')

def CalcolaT(var1):
    
    var2 = 0
    for a, b in var1.items():
        var2 += float(b['Prezzo']) * int(b['Qta'])

    print('-' * 35)
    print(f'Totale carrello spesa euro {var2:.2f}')
    print('-' * 35)
    input('\nPremere INVIO, per continuare')

def Sscontrino(var1):
    print('-' * 35)
    print('Scontrino del carrello della spesa')
    print('-' * 35)

    if not var1:
        input('\nIl carrello della spesa è vuoto, premere INVIO per continuare')
        return

    for a, b in var1.items():
        print(f'{a} {b['Prezzo'] * b['Qta']:.2f} euro')

    var2 = 0
    for a, b in var1.items():
        var2 += float(b['Prezzo']) * int(b['Qta'])
    
    if var2 > 100:
        print(f'\nTotale sconto applicato {var2 * 0.10:.2f}')

    print(f'Totale carrello della spasa finale {var2 - var2 * 0.10:.2f}')

    input('\nPremere INVIO, per continuare')

def Tarticolo(var1):
    print('-' * 50)
    print('Togli un articolo dal carrello della spesa')
    print('-' * 50)

    if not var1:
        input('\nIl carrello della spesa è vuoto, premere INVIO per continuare')
        return

    var2 = " ABCDEFGHKIJLMNOPQRSTUVWXYZ01234567890"
    while True:
        var3 = input('Nome ').lstrip().rstrip()
        var4 = True

        if var3 == '':
            continue

        for i in range(0, len(var3), 1):
            if var3[i].upper() not in var2:
                 var4 = False
                 break

        if var4:
            try:
                del var1[var3]
            except:
                print('Articolo non trovato')
                continue
            
            input(f'\nArticolo tolto dal carrello della spesa, premere INVIO per continuare')
            break
        else:
            print('Descrizione articolo non ammessa')
            continue

def Ccarrello(var1):
    print('-' * 40)
    print('Azzera l\'intero carrello della spesa')
    print('-' * 40)

    if not var1:
        input('\nIl carrello della spesa è vuoto, premere INVIO per continuare')
        return('')
    
    print('Confermi [S]?')
    var3 = readchar.readchar().upper()

    if var3.upper() != 'S':
        return
    else:
        var2 = []
        for a in var1.keys():
            var2.append(a)
        
        for a in var2:
            del var1[a]



Dcarrello = {}
while True:
    os.system('cls')
    var1 = Gmenu()

    if var1 == 1:
        os.system('cls')
        Dcarrello.update(Garticolo())
    elif var1 == 2:
        os.system('cls')
        Mcarrello(Dcarrello)
    elif var1 == 3:
        os.system('cls')
        CalcolaT(Dcarrello)
    elif var1 == 4:
        os.system('cls')
        Sscontrino(Dcarrello)
    elif var1 == 5:
        os.system('cls')
        Tarticolo(Dcarrello)
    elif var1 == 6:
        os.system('cls')
        Ccarrello(Dcarrello)
    else:
        break
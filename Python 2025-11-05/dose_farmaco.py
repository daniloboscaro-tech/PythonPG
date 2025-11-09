import os
import readchar

def user_v():
    var1 = 'ABCDEFGHIJKLAMNOPQRSTUVWYZ'
    
    while True:
        os.system('cls')

        var2 = False
        Nome = input('Nome ').strip()
        
        if len(Nome) != 0:
            for i in range(len(Nome)):
                if Nome[i].upper() not in var1:
                    var2 = True
                    break
        else:
            var2 = True

        if var2:
            print('Nome non valido, premere INVIO')
            readchar.readkey()
            continue

        break

    while True:
        os.system('cls')

        var2 = False
        Cognome = input('Cognome ').strip()
        
        if len(Cognome) != 0:
            for i in range(len(Cognome)):
                if Cognome == '':
                    var2 = True
                    break
        else:
            var2 = True
     
        if var2:
            print('Cognome non valido, premere INVIO')
            readchar.readkey()
            continue
        
        break

    while True:
        try:
            os.system('cls')
            Eta = int(input('Età '))

            if Eta <= 0:
                print('Digita un numero maggiore di zero, premere INVIO')
                readchar.readkey()
                continue
            else:
                break

        except:
            print('Digita un numero, premere INVIO')
            readchar.readkey()
            continue

    while True:
        try:
            os.system('cls')
            Peso = int(input('Peso in kilogrammi '))

            if Peso <= 0:
                print('Digita un numero maggiore di zero, premere INVIO')
                readchar.readkey()
                continue
            else:
                break

        except:
            print('Digita un numero, premere INVIO')
            readchar.readkey()
            continue

    return[Eta, Peso]

def young_m(val1):
    dose_a = 1000
    dose_p = round(val1 / (val1 + 12) * dose_a)

    return(dose_p)

def clark_m(val1):
    dose_a = 1000
    dose_p = round((val1 / 70) * dose_a)

    return(dose_p)

while True:
    var1 = user_v()
    Eta = var1[0]
    Peso = var1[1]

    if Eta <= 3 or Peso <= 5:
        print('Va consultato il pediatra, premere INVIO')

    elif Eta > 18 or Peso > 70:
        print('Utilizzare la dose da 1000mg')

    elif (Eta > 3 and Eta < 18) or (Peso > 5 and Peso < 70):
        print(f'Dose pediatrica secondo Young {round(young_m(Eta))}mg')
        print(f'Dose pediatrica secondo Clark {round(clark_m(Peso))}mg')

        #print(f'Dose pediatrica secondo Young {round(young_m(Eta) / 1000 * 100)}% di 1000mg')
        #print(f'Dose pediatrica secondo Clark {round(clark_m(Peso) / 1000 * 100)}% di 1000mg')

    print('\nVuoi controllare un altro utente? [S]')
    var1 = readchar.readkey().upper()

    if var1 != 'S':
        break
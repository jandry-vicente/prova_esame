import datetime

from trasferimento import trasferimento, utente



if __name__ == '__main__':

#test 1 nome
    try:
        s = utente("Pa olo", "Arviho", "PLOVSG96B15Z605d")
        print("test 1 non passato")
    except ValueError as ve:
        print("test 1 passato", ve.args)

#test 2 cognome
    try:
        s = utente("Paolo", "A87", "PLOVSG96B15Z605d")
        print("test 2 non passato")
    except ValueError as ve:
        print("test 2 passato", ve.args)

#test 3 importo
    try:
        imp = trasferimento("p", "IT9876543524f3425676543")
        print("test 3 non passato")
    except ValueError as ve:
        print("test 3 passato", ve.args)
#test 3 importo
    try:
        imp = trasferimento(1223, "ITA8e28")
        print("test 4 non passato")
    except ValueError as ve:
        print("test 4 passato", ve.args)

    x = trasferimento

    imp = input("inserire importo da inviare")
    iban = input("inserire iban")
    s = trasferimento(imp, iban)
    testo = "importo:" + s.getImporto() + "\ndata:" + str(datetime.datetime.now()) + "\niban:" + s.getIban()
    print(testo)
    print("confermare operazione \n1:SI (esci)")
    x = input("premi 1 per uscire")
    if x == "1":
        exit()


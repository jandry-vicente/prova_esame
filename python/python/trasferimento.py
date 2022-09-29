import datetime
class utente:
    def __init__(self, nome, cognome, codFiscale):
        if (" " in nome):
            raise (ValueError("il nome senza spazi"))

        if (len(nome) > 20 or len(nome) < 2):
            raise (ValueError("lunghezza deve essere di almeno 2 caratteri e massimo 20"))

        if (any((c < "A" or c > "z") for c in nome)):
            raise (ValueError("Il cognome puo contenere solo lettere, non caratteri speciali e senza spazi"))

        if (len(cognome) > 20 or len(cognome) < 2):
            raise (ValueError("lunghezza deve essere di almeno 2 caratteri e massimo 20"))

        if (any((c < "A" or c > "z") for c in cognome)):
            raise (ValueError("Il cognome puo contenere solo lettere, non caratteri speciali e senza spazi"))
        if (" " in cognome):
            raise (ValueError("l'importo puo contenere solo numeri e senza spazi"))

        self.__nome = nome
        self.__cognome = cognome
        self.__codFiscale = codFiscale

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCognome(self):
        return self.__cognome

    def setCognome(self, cognome):
        self.__cognome = cognome

    def getcodFiscale(self):
        return  self.__codFiscale

class cliente:
    def __init__(self, nome, cognome, codFiscale):
        super().__init__(nome, cognome, codFiscale)
        self.__codCliente = []

    def getCodCliente(self):
        return self.__codCliente

    def setCodCliente(self, codCliente):
        self.__codCliente = codCliente

class trasferimento:

    def __init__(self, importo, iban):
        if int(importo) < 0:
            raise (ValueError("l'importo puo contenere solo numeri "))

        if len(iban) != 27:
            raise (ValueError("l\'iban deve contenere 27 caratteri"))

        self.__importo = importo
        self.__data = datetime
        self.__iban = iban

    def getImporto(self):
        return self.__importo

    def setImporto(self, importo):
        self.__importo = importo

    def getIban(self):
        return self.__iban

    def setIban(self, iban):
        self.__iban = iban





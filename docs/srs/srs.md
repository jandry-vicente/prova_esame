#### Diagramma Classi.
![Diagramma_classi.png](https://github.com/jandry-vicente/prova_esame/blob/main/docs/srs/imgs/Diagramma_classi.png)

#### Diagramma di sequenza
![Diagramma_uml.png]([https://github.com/jandry-vicente/prova_esame/blob/main/docs/srs/imgs/Diagramma_classi.png](https://github.com/jandry-vicente/prova_esame/blob/main/docs/srs/imgs/Diagramma_uml.png))
#### Scenari


###	2.1 Studente


		Caso di cliente: apertura conto
	

			scenario principale:

				1) il cliente decide di aprire un nuovo conto
				2) l'azienda verifica i requisiti 
				3) l'azienda crea nuovo conto
				4) conto aperto

			Scenario alternativo	

		
				3b) requisiti non idonei
				1) conto non aperto

			Post condizione
				Viene creato un conto corrente con tutte le informazioni personali e gli vengono assegnate
				delle credenziali di accesso.

		Caso di cliente: visualizzare operazioni

			scenario principale:

				1) il cliente vuole visualizzare le operazioni effettuate
				2) il sistema verifica i dati
				3) il sistema fa visualizzare le operazioni 
					

		caso di cliente: Visualizza saldo disponibile

			scenario 

				1) il cliente chiede di visualizzare il saldo disponibile
				2) il sistema verifica il saldo 
				3) il sistema stampa a schermo il saldo
				
	
			scenario alternativo

				3b) saldo negativo
				


		Caso di cliente: operazioni di prelievo e deposito

			scenario
		
				1) cliente vuole effettuare operazione di prelievo
				2) il sistema verifica soldi disponibili
				3) il sistema emette banconote
				4) il cliente preleva i soldi
				
			scenario alternativo:
		
				3b) soldi non disponibili
				1
	
			Post condizione:

				Viene stampato ricevuta

		
			

		Caso di studente: bonifico bancario
		
				1) il cliente vuole effettuare bonifico
				2) il sistema verifica i dati 
				3) il sistema effettua il bonifico
				4) bonifico eseguito
	
			Post condizione:
		
				viene stampata ricevuta

	
###	2.2 Azienda

		Caso di Azienda: crea conto utente
	

			scenario principale:

				1) l'azienda verifica i dati del cliente
				2) il sistema verifica l'esistenza del cliente
				3) l'azienda crea nuovo conto
				4) conto aperto
			
		Caso di Azienda: trasferimento denaro

			scenario principale:
				1)L'azienda riceve ordine di invio soldi
				2)l'azienda verifica i dati del cliente
				3)l'azienda invia i soldi
				




	


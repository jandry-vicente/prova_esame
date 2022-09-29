
### Documento delle specifiche dei requisiti dell'utente
##### ePortafoglio


**VERSIONE : 11.0.1**

** Autori**  
Franco G.
Gil M.

**Revisioni precedenti**

| Versione    | Data        | Autori     | Note        |
| ----------- | ---------- | -----------  | -----------  |
| 10.2.1 | 15/09/2021  | Franco G.,  Gil M. | Aggiornamento di sicurezza  |
| 10.2.2 | 21/12/2021  | Franco G.| Correzione bug |
| 10.2.3 | 28/04/2022  | Franco G.,  Gil M. | Aggiornamento di sicurezza  |
| 11.0.1 | 15/09/2022  | Franco G.,  Gil M. | Nuova versione del software |

# Tabella dei contenuti

1. [Introduzione](#p1)
	1. [Ambito del documento](#sp1.1)
	2. [Definizioni & Acronimi](#sp1.2) 
	3. [Riferimenti](#sp1.3)
2. [Descrizione Sistema ](#p2)
	1. [Contesto e Motivazione](#sp2.1)
	2. [Obiettivi del progetto](#sp2.2)
3. [Requisito](#p3)
 	1. [Stakeholders](#sp3.1)
 	2. [Requisiti funzionali](#sp3.2)
 	3. [Requisiti non funzionali](#sp3.3)
  
  

<a name="p1"></a>

## 1. Introduzione

<a name="sp1.1"></a>

### 1.1 Ambito del documento

L'azienda ePortafoglio ha deciso di affidarsi a noi per la progettazione di un applicazione, che sia in grado di gestire i conti dei clienti.


<a name="sp1.2"></a>

### 1.2 Definizioni & Acronimi

| Acronimo				| Definizione | 
| ------------------------------------- | ----------- | 
| SW                               | Software |
| DBMS                            | DataBase Management System |
| SQL                           | Structure Query Language |
| PDF                           | Portable Document Format |

<a name="sp1.3"></a>

### 1.3 Riferimenti

<a name="p2"></a>

## 2. Sistema


### 2.1 Contesto e motivazione

L'applicazione dovrà gestire i conti dei suoi clienti, i quali potranno collegarsi tramite credenziali.


<a name="sp2.2"></a>

### 2.2 Obiettivi del progetto]

L'obiettivo è riuscire a realizzare l'applicazioni utilizzando le tecnologie più avanzate, in modo da garantire una migliore efficenza e sicurezza ai suoi utenti.

<a name="p3"></a>

## 3. Requisiti

| Priorità | Significato | 
| --------------- | ----------- | 
| V | **Vincolante:**   |
| D | **Desiderabile:** |
| O | **Opzionale:**    |
| F | **Miglioratori futurit:** |

<a name="sp3.1"></a>
### 3.1 Stakeholders


| Nome | _____________ | 
| --------------- | ----------- | 
| Azienda | **Personale di rete e di staff, personale in ruoli di responsabilità, top management**   |
| Clienti | **Privati, Famiglie, Grandi imprese** |


<a name="sp3.2"></a>
### 3.2 Requisiti funzionali

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.0 |  Il sistema deve fornire una ricevuta dell'operazione effettuata |D|
| 1.1 |  L'utente deve essere in grado di visualizzare il suo saldo |V|
| 1.2 |  L'utente deve essere in grado di visualizzare i suoi movimenti |V|
| 1.3 |  L'utente deve essere in grado di effettuare operazioni di prelievo e deposito |V|
| 1.4 |  Il sistema dovrà permettere di inviare soldi ad un altro utente tramite IBAN |V|
| 1.5 |	 L'utente deve avere la possibilità di visualizzare i movimenti in un determinato periodo |D|
| 1.6 | L'applicazione deve stampare l'estratto conto in PDF |V|



<a name="sp3.3"></a>
### 3.2 Requisiti non funzionali 
 
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 2.0 | L'applicazione deve funzionare su sistemi WINDOWS, e MACOS |V|
| 2.1 | L'applicazione deve essere compatibile con IOS e ANDROID |F|
| 2.2 | L'applicazione deve funzionare su sistemi WINDOWS, e MACOS |V|
| 2.3 | il sistema deve essere molto veloce nelle operazioni |D|
| 2.4 | l'applicazione deve essere disponibile anche in Inglese
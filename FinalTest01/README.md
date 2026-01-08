# Final Test 01
## Description
1. Scrivere due funzioni per leggere e restituire:
   - tutti i libri presenti nel file `library.csv`
   - tutte le recensioni presenti nel file `reviews.csv`

   N.B. Le funzioni devono essere richiamate, dove necessario in `app.py` per ottenere l'elenco dei libri e delle recensioni. Il caricamento dei file deve essere implementato in un'unica parte del codice.

2. Visualizzare in `index.html` una tabella contenente l’elenco dei libri, se presenti.
   Se il file è vuoto o mancante, mostrare "Nessun libro trovato".
   
3. Rendere cliccabile ogni libro e renderizzare ad una pagina di dettaglio del libro con una route dinamica con il codice del prodotto (es. `/libro/<codice_libro>`) e visualizzare una pagina con i dettagli del libro formattati in modo pulito.

4. Nella pagina di dettaglio, inserire un form sotto i dettagli del libro per l’inserimento di una recensione. Il codice della nuova recensione deve essere
generato lato backend. La nuova recensione sovra essere memorizzata nel file `reviews.csv`.

5. Crea due API:
   - una API per ritornare tutti i libri inseriti
   - una per tutte le recensioni associate al singolo libro in base al codice_libro passato nell’url

6. Nel template `index_react.html`, creare una componente React BookList per renderizzare una tabella dei libri analoga quella del punto 2. Sopra la tabella deve essere inserito un form per l'aggiunta di un libro. Associare questa componente alla route `/react`.

7. Rendere cliccabile il codice libro di ogni tabella per navigare verso la route `/react/book/:id`. Tale root deve essere associata a una componente BookDetail che mostri i dettagli del libro in maniera simile alla pagina del punto 3. Sotto i dettagli del libro, devono essere mostrate anche le recensioni associate ad esso.

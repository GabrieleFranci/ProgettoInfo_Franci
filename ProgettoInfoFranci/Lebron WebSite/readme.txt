# LeBron James WebSite

Questo progetto è un sito web dedicato alla carriera di LeBron James, sviluppato con Flask e SQLite. Il sito permette di esplorare le tappe principali della carriera di LeBron, visualizzare statistiche, highlights, citazioni e commenti, oltre a gallerie fotografiche delle sue esperienze con le varie squadre NBA.

## Struttura del Progetto

- **app.py**  
  Applicazione principale Flask. Gestisce le rotte, la connessione al database e l'inizializzazione delle tabelle. Ogni rotta corrisponde a una pagina del sito (carriera, attributi, record, famiglia, foto delle squadre, statistiche, ecc.).

- **models.py**  
  Definisce i modelli SQLAlchemy per le tabelle del database: Stats, Game, Highlight, Quote, CareerEvent, Comment.

- **/templates/**  
  Contiene i file HTML (Jinja2) per le varie pagine del sito, tra cui `index.html`, `carriera.html`, `attributi.html`, `record.html`, `famiglia.html`, e le pagine fotografiche delle squadre.

- **/static/**  
  Contiene file statici come immagini (`/favicon/`), CSS (`/css/style.css`), e altre risorse multimediali.

- **lebron.db**  
  Database SQLite con tutte le informazioni su statistiche, partite, highlights, citazioni, eventi di carriera e commenti.

## Come avviare il sito

1. **Prerequisiti**  
   - Python 3.x  
   - Flask  
   - Flask-SQLAlchemy

2. **Installazione dipendenze**
   ```bash
   pip install flask flask_sqlalchemy
   ```

3. **Avvio del server**
   ```bash
   python app.py
   ```
   Il sito sarà accessibile su `http://127.0.0.1:5000/`.

## Funzionalità principali

- **Home**: Pagina iniziale con introduzione.
- **Carriera**: Timeline delle squadre NBA di LeBron con immagini e descrizioni.
- **Attributi**: Caratteristiche tecniche e fisiche del giocatore.
- **Record**: Principali record e traguardi raggiunti.
- **Famiglia**: Sezione dedicata alla famiglia di LeBron.
- **Gallerie fotografiche**: Foto delle varie esperienze NBA.
- **Statistiche avanzate**: Query SQL per visualizzare statistiche stagionali, migliori partite, highlights, citazioni e commenti.

## Personalizzazione

- Puoi modificare i file HTML in `/templates/` per cambiare i contenuti delle pagine.
- Le immagini e i file CSS si trovano nella cartella `/static/`.
- Per aggiungere dati, modifica direttamente il database `lebron.db` oppure aggiorna i modelli in `models.py` e crea nuove rotte in `app.py`.

## Note

- Il sito è pensato per uso didattico e personale.
- Assicurati che la struttura delle cartelle sia rispettata per il corretto funzionamento delle rotte Flask.

---


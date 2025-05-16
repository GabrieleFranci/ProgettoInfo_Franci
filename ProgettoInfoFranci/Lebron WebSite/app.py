from flask import Flask, render_template
from models import db, Stats, Game, Highlight, Quote, CareerEvent, Comment
from sqlalchemy import text
import os

app = Flask(__name__)

# Configurazione del database SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'lebron.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza il database con l'app Flask
db.init_app(app)

# Crea tutte le tabelle definite nei modelli se non esistono già
with app.app_context():
    db.create_all()

# Rotta per la home page
@app.route('/')
def home():
    return render_template('index.html')

# Rotta per la pagina della carriera
@app.route('/carriera')
def carriera():
    return render_template('carriera.html')

# Rotta per la pagina degli attributi
@app.route('/attributi')
def attributi():
    return render_template('attributi.html')

# Rotta per la pagina dei record
@app.route('/record')
def record():
    return render_template('record.html')

# Rotta per la pagina della famiglia
@app.route('/famiglia')
def famiglia():
    return render_template('famiglia.html')

# Rotte per le gallerie fotografiche delle squadre
@app.route('/cavs-photos')
def cavs_photos():
    return render_template('cavs_photos.html')

@app.route('/heat-photos')
def heat_photos():
    return render_template('heat_photos.html')

@app.route('/cavs2-photos')
def cavs2_photos():
    return render_template('cavs2_photos.html')

@app.route('/lakers-photos')
def lakers_photos():
    return render_template('lakers_photos.html')

# Rotte per le pagine dedicate ai membri della famiglia
@app.route('/bronny.html')
def bronny():
    return render_template('bronny.html')

@app.route('/bryce.html')
def bryce():
    return render_template('bryce.html')

@app.route('/zhuri.html')
def zhuri():
    return render_template('zhuri.html')

@app.route('/savannah.html')
def savannah():
    return render_template('savannah.html')

# Rotta per la pagina delle statistiche avanzate
@app.route('/top_stats')
def top_stats():
    # Dizionario che conterrà i risultati delle query
    results = {}

    # Dizionario di query SQL per estrarre varie statistiche dal database
    queries = {
        "seasons_over_25_ppg": """
        SELECT season, points_per_game FROM stats
        WHERE points_per_game > 25
        ORDER BY points_per_game DESC
        """,
        "top_5_assist_seasons": """
        SELECT season, assists_per_game FROM stats
        ORDER BY assists_per_game DESC
        LIMIT 5
        """,
        "season_avg_pts_reb_ast": """
        SELECT season, points_per_game, rebounds_per_game, assists_per_game
        FROM stats
        ORDER BY season
        """,
        "season_max_rebounds": """
        SELECT season, rebounds_per_game FROM stats
        ORDER BY rebounds_per_game DESC
        LIMIT 1
        """,
        "teams_played_for": """
        SELECT DISTINCT team FROM stats
        """,
        "top_5_highest_scoring_games": """
        SELECT game_date, opponent, points FROM game
        ORDER BY points DESC
        LIMIT 5
        """,
        "games_with_10_ast_10_reb": """
        SELECT game_date, opponent, assists, rebounds FROM game
        WHERE assists >= 10 AND rebounds >= 10
        """,
        "avg_points_home_vs_away": """
        SELECT home_away, AVG(points) as avg_points FROM game
        GROUP BY home_away
        """,
        "total_points_vs_opponents": """
        SELECT opponent, SUM(points) as total_points FROM game
        GROUP BY opponent
        ORDER BY total_points DESC
        """,
        "latest_5_highlights": """
        SELECT title, event_date FROM highlight
        ORDER BY event_date DESC
        LIMIT 5
        """,
        "highlight_categories_count": """
        SELECT category, COUNT(*) as count FROM highlight
        GROUP BY category
        """,
        "quotes_with_year": """
        SELECT quote, quote_year, source FROM quote
        ORDER BY quote_year DESC
        """,
        "quotes_per_source": """
        SELECT source, COUNT(*) as num_quotes FROM quote
        GROUP BY source
        """,
        "recent_career_events": """
        SELECT event_date, description FROM career_event
        ORDER BY event_date DESC
        """,
        "latest_5_comments": """
        SELECT username, content, comment_date FROM comment
        ORDER BY comment_date DESC
        LIMIT 5
        """,
        "games_with_highlights": """
        SELECT g.game_date, g.opponent, h.title AS highlight_title
        FROM game g
        JOIN highlight h ON g.game_date = h.event_date
        ORDER BY g.game_date DESC
        LIMIT 10
        """,
    }

    # Esegue tutte le query e salva i risultati nel dizionario results
    for key, query in queries.items():
        result = db.session.execute(text(query)).fetchall()
        results[key] = [dict(row._mapping) for row in result]  # Conversione dei risultati in dizionari

    # Messaggi descrittivi per le varie statistiche (usati nel template)
    messages = {
        "top_seasons": "Top 5 stagioni per punti per partita",
        "top_rebounds": "Top 5 stagioni per rimbalzi per partita",
        "best_teams": "Top 5 squadre per punti medi",
        "best_teams_assists": "Top 5 squadre per assist medi",
        "best_teams_rebounds": "Top 5 squadre per rimbalzi medi",
        "recent_games": "Ultime 5 partite",
        "top_games_by_points": "Top 5 partite per punti segnati",
        "recent_highlights": "Ultimi 5 highlights",
        "recent_quotes": "Ultime 5 citazioni",
        "career_events": "Ultimi eventi della carriera",
        "recent_comments": "Ultimi 5 commenti",
        "top_points_rebound_ratio": "Top 5 stagioni per rapporto punti/rimbalzi",
        "top_assist_points_ratio": "Top 5 stagioni per rapporto assist/punti",
        "top_games_by_assist_point_ratio": "Top 5 partite per rapporto assist/punti",
        "recent_comments_with_season": "Ultimi 5 commenti con stagione"
    }

    # Ritorna la pagina delle statistiche con i risultati e i messaggi
    return render_template("top_stats.html", results=results, messages=messages)

# Avvia il server Flask in modalità debug
if __name__ == "__main__":
    app.run(debug=True)
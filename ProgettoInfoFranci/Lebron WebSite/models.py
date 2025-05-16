from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stats(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String)
    team = db.Column(db.String)
    games_played = db.Column(db.Integer)
    points_per_game = db.Column(db.Float)
    rebounds_per_game = db.Column(db.Float)
    assists_per_game = db.Column(db.Float)
    steals_per_game = db.Column(db.Float)
    blocks_per_game = db.Column(db.Float)

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    game_date = db.Column(db.String)
    opponent = db.Column(db.String)
    home_away = db.Column(db.String)
    result = db.Column(db.String)
    points = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    rebounds = db.Column(db.Integer)
    location = db.Column(db.String)

class Highlight(db.Model):
    __tablename__ = 'highlight'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    video_url = db.Column(db.String)
    category = db.Column(db.String)
    event_date = db.Column(db.String)

class Quote(db.Model):
    __tablename__ = 'quote'
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String)
    source = db.Column(db.String)
    quote_year = db.Column(db.Integer)

class CareerEvent(db.Model):
    __tablename__ = 'career_event'
    id = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.String)
    description = db.Column(db.String)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    content = db.Column(db.String)
    comment_date = db.Column(db.String, server_default=db.func.current_timestamp())

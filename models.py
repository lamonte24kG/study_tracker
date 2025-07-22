from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy for database management

db = SQLAlchemy() # Create an instance of SQLAlchemy to manage the database


class StudyEntry(db.Model): # Define the StudyEntry model to represent a study log entry
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for each study entry
    date = db.Column(db.Date, nullable=False) # Date of the study session
    category = db.Column(db.String(50), nullable=False) # Category of the study session (e.g., Math, Science)
    topic = db.Column(db.String(100)) # Specific topic studied
    chapters_completed = db.Column(db.Float, nullable=False) # Number of chapters completed
    goal = db.Column(db.Float) # Study goal 
    notes = db.Column(db.String(200)) # Additional notes about the study session

    
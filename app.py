# Import necessary libraries from Flask
from flask import Flask, render_template, request, redirect, url_for

# Import the database instance and model from models.py
from models import db, StudyEntry

from datetime import datetime # Import datetime for handling date fields

# Create/Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Turn off the event system to avoid warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Create the database tables before the first request is processed
with app.app_context(): # Create an application context to access the database
    db.create_all() # This will create the "StudyEntry' table if it doesn't exist

# Route: Home page - displays all study log entries
@app.route('/') # Define the route for the home page
def index(): # Define the index route for the home page
    # Query the database to get all study entries
    entries = StudyEntry.query.all() # Fetch all entries from the database
    return render_template('index.html', entries=entries) # Send entries to index.html for display

# Route: Add a new study entry - handles both showing and submitting the form
@app.route("/add", methods=["POST"])
def add_entry(): # Define the route to add a new entry
    # Get the form data from the request
    date_str = request.form["date"]# Extract the date string from the form
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date() #

    entry = StudyEntry(
        date=date_obj,
        category=request.form["category"],
        topic=request.form["topic"],
        chapters_completed=float(request.form["chapters_completed"]),
        goal=float(request.form["goal"]) if request.form["goal"] else None,
        notes=request.form["notes"]
    )
    db.session.add(entry) # Add the new entry to the session
    db.session.commit() # Commit the session to save the entry to the database
    return redirect(url_for("index")) # Redirect back to the home page after adding the entry

@app.route('/edit/<int:id>', methods=['GET', 'POST']) # Define the route to edit an entry by its ID
def edit_entry(id): # Get the ID of the entry to edit from the URL
    entry = StudyEntry.query.get_or_404(id) # Fetch the entry by ID or return a 404 error if not found
    if request.method == 'POST': # Check if the request method is POST (form submission)
        # Update the entry with the form data
        entry.date = datetime.strptime(request.form['date'], "%Y-%m-%d").date() # Convert the date string to a date object
        entry.category = request.form['category'] # Update the category
        entry.topic = request.form['topic'] # Update the topic
        entry.chapters_completed = float(request.form['chapters_completed']) # Update the chapters completed
        entry.goal = float(request.form['goal']) if request.form['goal'] else None # Update the goal, if provided
        entry.notes = request.form['notes'] # Update the notes

        db.session.commit() # Commit the changes to the database

        return redirect(url_for('index')) # Redirect back to the home page after editing
    return render_template('edit.html', entry=entry) # Render the edit form with the current entry data
    
# Route: Delete a study entry - handles the deletion of an entry
@app.route('/delete/<int:id>', methods=['POST']) # Define the route to delete an entry by its ID
def delete_entry(id): # Get the ID of the entry to delete from the URL
    # Query the database to find the entry by ID and delete it
    entry = StudyEntry.query.get_or_404(id)# Fetch the entry by ID or return a 404 error if not found
    db.session.delete(entry)# Delete the entry from the session
    db.session.commit()# Commit the changes to the database
    # Redirect back to the homepage after deletion
    return redirect(url_for('index'))
        

# Start the Flask server when this file is run directly
if __name__ == '__main__': # Check if this file is being run directly
    app.run(debug=True) # Run the app in debug mode for development
# study_tracker
flask study tracker app

Study Tracker

A web-based study tracker built with Flask, designed to help users log and review their learning progress. Users can add study sessions, categorize them, track chapters completed, set goals, and leave notes — all in a clean, responsive interface.

This project started as a personal tool to help me keep track of assignments and learning milestones. More importantly, it serves as a DIY tutorial — a hands-on way for me to teach myself Flask by building something practical from scratch. The app is designed to be modular and expandable, so I can keep adding features as I learn more about web development and backend systems.

⸻

Features
	•	Add and manage study entries by date
	•	Track subjects, topics, chapters completed, and goals
	•	Add personal notes to each session
	•	Responsive Bootstrap layout for desktop & mobile
	•	Editable fields and database integration (SQLite via SQLAlchemy)

⸻

 Tech Stack
	•	Backend: Flask, SQLAlchemy
	•	Frontend: HTML, Bootstrap 5
	•	Database: SQLite
	•	Deployment: Replit / Localhost

⸻

Getting Started

1. Clone the Repository

git clone https://github.com/your-username/study_tracker.git
cd study_tracker

2. Create and Activate a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate    # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the App

export FLASK_APP=app.py   # Mac/Linux
# set FLASK_APP=app.py    # Windows

flask run

Visit: http://127.0.0.1:5000 in your browser.

⸻

Project Structure

study_tracker/
├── app.py
├── models.py
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── style.css
├── database.db
├── requirements.txt
└── README.md


⸻

Lessons Learned

This app was part of a portfolio project to reinforce:
	•	Flask routing and form handling
	•	SQLAlchemy ORM integration
	•	Bootstrap layout customization
	•	Responsive design and mobile-first UI
	•	Project planning and Git version control

⸻

Future Improvements
	•	Add user authentication for multiple users
	•	Export data as CSV or PDF
	•	Add weekly/monthly progress graphs
	•	Dark mode toggle

⸻


Author

Lamonte Golden**  
[Portfolio](https://24kgdesign.com/portfolio) · [LinkedIn](https://www.linkedin.com/in/lamonte-golden-24kg/)) · [GitHub](https://github.com/lamonte24kG)


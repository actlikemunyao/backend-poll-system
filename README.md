Django Poll App – Backend Project
Project Overview

This is a backend for an online poll system built with Django and Django REST Framework.
Users can create polls, add options, and vote. The API is hosted online and accessible via Render.

Technologies Used:

Python 3

Django 5

Django REST Framework

SQLite (for database)

Render (for hosting)

drf-yasg (Swagger docs, optional)

Host Links

Live App / API Root: https://backend-poll-system.onrender.com/api/

Polls Endpoint: https://backend-poll-system.onrender.com/api/polls/

Admin Panel (for reviewers): https://backend-poll-system.onrender.com/admin/

Superuser: victor

Password: munyao20

API Endpoints
Endpoint	Method	Description
/api/	GET	Root API endpoint; lists available endpoints
/api/polls/	GET, POST	List all polls / Create new poll
/api/options/	GET, POST	List all options / Create new option
/api/votes/	GET, POST	List all votes / Submit a vote

Example POST request to create a poll:

POST /api/polls/
{
  "title": "Favorite musician?"
}


Example POST request to add an option:

POST /api/options/
{
  "text": "Adele",
  "poll": 1
}


Example POST request to vote:

POST /api/votes/
{
  "option": 1,
  "user": 1
}

Setup Instructions (Local Testing)

Clone the repository:

git clone <your-repo-link>
cd django_poll_app


Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser (optional, for admin access):

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Access locally:

Admin: http://127.0.0.1:8000/admin/

API: http://127.0.0.1:8000/api/

Notes

The hosted app on Render uses SQLite, which works for single-instance usage.

For production or multiple instances, PostgreSQL is recommended.

The API is browsable via Django REST Framework’s built-in interface.

Swagger docs can be added at /api/docs/ (if configured).

## General info
This is feedback submission form using Python, Flask and PostgreSQL.
The user can submit their name, choose a developer, enter a rating and make a comment.
On successful submit, the user gets a success page.
Information submitted is sent to a database in PostgreSQL. If the user has submitted under the same name before, they cannot submit again.
Information submitted is also sent to an email account - in this case it is mailtrap.

This app uses Python, Flask, SQLAlchemy, Psycopg2 (for PosteSQL) and Gunicorn.
PostgreSQL is used for development database.
Heroku is used for deployment.

Deployed URL:
https://developerfeedback.herokuapp.com/

With help from tutorial by TraversyMedia.

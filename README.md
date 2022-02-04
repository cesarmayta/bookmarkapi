# bookmarkapi
API Rest for Bookmarks
TEST for Keeper Solutions

#HOW TO DEPLOY
1 - clone the repository
2 - create an virtual env and activated
    python -m venv venv
    source venv/scripts/activate
3 - install dependencies
    pip install -r requirements.txt
4 - create database and tables
    python manage.py makemigrations
    python manage.py migrate
5 - create an admin user
    python manage.py createsuperuser
6 - deploy the project
    python manage.py runserver

#PRINCIPAL END POINT
# for see public bookmarks
http://localhost:8000/publicbookmark

#for manage bookmarks

http://localhost:8000/bookmark - ACCEPT GET AND POST METHODS WITH BASIC AUTHENTICATION


http://localhost:8000/bookmark/bookmarkId - ACCEPT PUT AND DELETE METHODS WITH BASIC AUTHENTICATION


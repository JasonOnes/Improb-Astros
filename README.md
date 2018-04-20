# Improb-Astros

To use this application locally. Do the following steps.
1. Install Python and git
2. Clone this repository
3. Install the required packages in requirements.txt. We recommend creating a virtual environment using a package manager like Conda (Miniconda) or PIP.
4. Install PostgreSQL
5. Create a user "improb-astros" with a password and sign-in permissions. 
6. Create a database called "improb-astros"
7. Set up the environment variables for the app's SECRET_KEY, and the database USER, DB_PASSWORD.
8. From a command line, activate the virtual environment and go to the repository top-level directory (with manage.py in it).
9. `python manage.py makemigrations` to create the migration script (there may be no changes detected)
10. `python manage.py migrate` to create the tables in the database
11. `python manage.py runserver` and point your browser to localhost:8000
12. To use the admin page at localhost:8000/admin, you will first need to create a new admin user by running `python manage.py createsuperuser`

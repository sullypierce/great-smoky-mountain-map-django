## The Great Smoky Mountain Map (Server Side)

This is the Django REST server side for the Great Smoky Mountain Map (https://github.com/sullypierce/great-smoky-mountain-map-react).
See React frontend repository for more details.

##To Run

1. `git clone` this repository
2. create and run a python environment
3. run `pip install`
4. create a sqlite3 database file
4. Run `python manage.py makemigrations`
5. Run `python manage.py migrate`
6. Run ``python manage.py loaddata` for the fixtures`
7. Check in settings.py that the correct port is whitelisted for the React app.
8. Run `python manage.py run`

# wine_app: Using Django As An API

Using Django to create a full-stack web application where both the front and back end are coupled together into a single code base can become a monolithic (i.e., huge) application. In some cases, it works, but as applications grow to hundreds of thousands of lines of code it can become a nightmare to debug and add new features.

Enter the concept of microservices and Service Oriented Architecture (SOA). This idea builds off of Single Responsibility code in that one app does one thing. In this, we create web applications that separate the front and back end. Moving forward, we'll use Django as an API to handle reading from / writing to the database and ReactJS to handle all of our front end logic (i.e., what the user sees / interacts with).

Create a Django API that keeps track of different wines and returns JSON instead of HTML.
Using that JSON to populate the frontend with the correct data.

# Set up API

# 1. Set up models

models.py
databases
installed_apps
migrations

# 2. Set up Routes

project/urls.py
app/urls.py

# 3. Set up views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
returns JsonResponse

# 4. Serializers

app/serializers.py
Serializing: Convert data from one format to another. In this case, convert a Django Query object into JSON. to make a query to the Postgres database using Django ORM and then translate its output into JSON.

# 5. Set up Forms

app/forms.py

# 6. Test the api
https://wine-api-1.herokuapp.com/ 

# From the CLI

`
python manage.py python shell_plus
from wines.models import Wine
Wine.objects.all()
Wine.objects.create(wine_name='Vinio', price='50', varietal='Cabernet')
`
Getting Django Ready For Heroku
We have to add a few things to our Django app to make sure it will run properly when we deploy it. The steps that are going to follow is based off of the official docs.

Create a Procfile

The first thing we need to create is a Procfile in our app's root directory (at the same level as manage.py). In this file, we are going to tell Heroku which web server we want to use for our app. Open the file and copy this line of code web: gunicorn INSERT_PROJECT_NAME_HERE.wsgi, being sure to replace "INSERT_PROJECT_NAME_HERE" with whatever the name of your app project is. In our case, it's wine_api.
Gunicorn is the server Heroku recommends we use. Install it with pip install gunicorn.
Django-Heroku

Most of the rest of the setup is done for us by installing a final pip package called django-heroku. Run pip install django-heroku.
Then place import django_heroku at the very top of your settings.py file and django_heroku.settings(locals()) at the bottom of settings.py.
Requirements

The final thing we need to do is create our requirements.txt file in the root (the same level as your venv directory. Heroku will use this to download all our dependencies, including gunicorn and django-heroku.
$ pip freeze > requirements.txt
Create your .gitignore file

You don't need to commit your venv/ or any pycache's, so let's create a .gitignore file and add in venv/ and __pycache__/.

![](header.png)

## Release History

- 0.0.1
  - Work in progress

## Meta

Carole Ouedraogo
[https://github.com/Carole-Ouedraogo/github-link](https://github.com/Carole-Ouedraogo)

## Contributing

1. Fork it (<https://github.com/Carole-Ouedraogo/wine_app/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

# Learn Django
This is a repository where I try to create a project with django and to learn its ways.

## Setup
You have to create a conda environment first
```
conda create --name django
```
and then activate it
```
conda activate django
```

Install the dependencies
```
pip install -r requirements.txt
```

## Django
Create a django project
```
django-admin startproject cfehome
```

And now you can start your server
```
python manage.py runserver
```
After you create a new app with
```
python manage.py startapp visits
```
And declared a new model, to tell the app to be ready to change the database, add your app inside settings.py and do:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Technologies
django, postgresql, neon, railway, tailwindcss, flowbite


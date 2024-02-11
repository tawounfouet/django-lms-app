
```bash
# Create a virtual environment using Pipenv
pipenv lock 

# Activate the virtual environment
pipenv shell

# Install django
pipenv install django 

# Start a new Django project
django-admin startproject project . 

# create new app
python manage.py startapp app

# migrate the database
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run the server
python manage.py runserver 8007
```

```bash
# crispy forms 4 
pipenv install django-crispy-forms

# settings.py
INSTALLED_APPS = [
    ...
    'crispy_forms',
    ...
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```


```bash


```


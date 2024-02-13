
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
python manage.py makemigrations
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


## Font Awesome

```html
https://fontawesome.com/v5/search
```

```js
<script src="https://kit.fontawesome.com/0e5fa0ea8a.js" crossorigin="anonymous"></script>

```

```bash
# python 
https://fontawesome.com/icons/python?f=brands&s=solid
<i class="fa-brands fa-python"></i>
catetory_icon = 'fab fa-python'
```


```bash
pipenv install pillow
```


## Media Files

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
    
```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```python
```

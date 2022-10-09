## virtual env.
    python3 -m venv venv

## install django.
    pip install django

## run server.
    python  manage.py runserver

## interactive console.
    python manage.py shell

## create proyect.
    django-admin startproject fivestars

## create app.
    python manage.py startapp ratings

## create super user.
    python manage.py createsuperuser

## Pasos para hacer el backend. ## On production always debug false.
    views.py -- podemos hacer el helloworld :

        def index(request):
            return HttResponse("hello world)

    modificamos el Url.py y agregamos la url del proyecto enlazandolo con el admin
    Luego agregamos url.py en el app donde incluiremos el path.
            path('', views.index, name='index'),
    en DATABASES podemos manipular el motor de la base de datos.
        django.db.backends.mysql o sqlite3 postgres
    Luego redactamanos los models de la app.
    Django automaticamente coloca las primary keys en las tablas.
    Agregamos en settings.py la installed_app que creamos (django no la agrega automaticamente)

## Migraciones para MOdelos:
    python manage.py makemigrations polls --> convertir en tablas
    python manage.py migrate  ---> ejecut las tablas sql en la base de datos.

    Luego de agregar y acomodar los metodos de nuestros modelos podemos crear el superuser para entrar al administrador de django.

    Luego agregamos en admin.py los modelos :
        Eje:
        from django.contrib import admin
        from .models import Ratings

        admin.site.register(Ratings)
    
    Luego ya podemos crear las views.
**Comandos iniciales y pasos relevantes**

	#Instalación de paquetes
	pip3 install virtualenv
	cd Tarea1
	virtualenv env --python=python3.6
	source ./env/bin/activate
	pip install Django
	pip install psycopg2
	
	
	#Creación del proyecto
	django-admin startproject T1
	cd T1
	python manage.py startapp comments
	brew install postgresql
	
	
	#Creación de db y usuario
	psql
	CREATE USER <user> WITH PASSWORD ‘<password>’;
	CREATE DATABASE <db> WITH OWNER = <user>;
	GRANT ALL PRIVILEGES ON DATABASE data TO <db>;
	
	
	#Configuración db
	DATABASES = {
	    ‘default’ {
	        ‘ENGINE’ ‘django.db.backends.postgresql_psycopg2’,
	        ‘NAME’ ‘<db>’,
	        ‘USER’ ‘<user>’,
	        ‘PASSWORD’ ‘<password>’,
	        ‘HOST’ ‘localhost’,
	        ‘PORT’ ‘’,
	    }
	}
	
	
	#Manejo db
	python manage.py makemigrations
	python manage.py migrate
	python3 manage.py createsuperuser
	python3 manage.py runserver


**Referencias principales**

* Django Tutorials by Max Goodridge: 
https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj

* Creating user, database and adding access on PostgreSQL: 
https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

* Migraciones: 
https://docs.djangoproject.com/en/1.8/intro/tutorial01/

* Views: 
https://docs.djangoproject.com/es/2.1/intro/tutorial03/

* Index View: 
https://stackoverflow.com/questions/5823580/django-form-resubmitted-upon-refresh

* Modelo de comentario: 
https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/

* Create postgres db: 
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

* Get date: 
https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects

* Get user IP: 
https://stackoverflow.com/questions/48277696/get-current-server-ip-or-domain-in-django

* Zona horaria: 
https://docs.djangoproject.com/zh-hans/2.1/_modules/pytz/


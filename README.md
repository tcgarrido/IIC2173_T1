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
	
	
	#Deploy
	sudo apt install python3
	sudo python3 -m http.server 80
	charette17.ing.puc.cl #funciona
	git clone https://github.com/tcgarrido/IIC2173_T1.git Tarea1
	sudo apt install python3-pip
	sudo python3 -m pip install django
	sudo python3 manage.py runserver 80 #error
	sudo python3 -m pip install -r requirements.txt 
	
	

**Referencias principales**

* Django Tutorials by Max Goodridge: 
https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj

* Creating user, database and adding access on PostgreSQL: 
https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

* Migraciones: 
https://docs.djangoproject.com/en/1.8/intro/tutorial01/

* Forms: https://docs.djangoproject.com/en/2.1/topics/forms/

* Forms 2: https://tutorial.djangogirls.org/es/django_forms/

* Views: 
https://docs.djangoproject.com/es/2.1/intro/tutorial03/

* Index View: 
https://stackoverflow.com/questions/5823580/django-form-resubmitted-upon-refresh

* Modelo de comentario: 
https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/

* Adduser server:
https://ubuntuforums.org/showthread.php?t=2130483

* Create postgres db: 
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

* Get date: 
https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects

* Get user IP: 
https://stackoverflow.com/questions/48277696/get-current-server-ip-or-domain-in-django

* Get user IP address: 
https://stackoverflow.com/questions/23463599/how-to-store-ip-address-in-the-database-and-django-admin/23465544

* GenericIPAddressField: 
https://stackoverflow.com/questions/41123659/django-ipv4-only-for-genericipaddressfield

* Zona horaria: 
https://docs.djangoproject.com/zh-hans/2.1/_modules/pytz/

* Commands ssh:
https://documentation.codeship.com/basic/continuous-deployment/deployment-with-ftp-sftp-scp/#run-commands-on-a-remote-server-via-ssh

* Deploy:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#install-the-packages-from-the-ubuntu-repositories

**Vista previa**

![alt text](https://raw.githubusercontent.com/tcgarrido/IIC2173_T1/master/image.png)

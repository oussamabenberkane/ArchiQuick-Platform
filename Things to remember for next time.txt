Install:

cd [folderpath]
pip install Django

pipenv shell
django-admin startproject [projectname] . #the point is to use current directory instead of creating one

#finished with django-admin, using python manage.py from now on


Avtivate venv in vscode:

File -> Preferences -> search for venv -> copy the path of venv (activate.bat) -> double the slashes(//)
-> go to terminal -> type this line of code: "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
-> open a new terminal and ur good to go.

In vscode Terminal from now on:

python manage.py runserver (dont mind the 18 errors) then open an other terminal and type
python manage.py startapp [appname] -> go to settings.py and add new app to INSTALLED_APPS.
 
Create urls.py in our app (we import the views module in it) and add it in main urls.py, 

Create templates folder in app

install and add django-debug-toolbar to INSTALLED_APPS and a bunch of other stuff
look at its documentation and follow the instructions.
pipenv install django-debug-toolbar


DATABASE: (in command line)
cd xampp\mysql\bin
mysql -u root -p    ##mysql -h localhost -u root (without pw)
create database Platform
use [nameofdb]
create table users(id INT NOT NULL AUTO_INCREMENT,
    firstname varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    username varchar(50) NOT NULL,
    telephone varchar(20) NOT NULL UNIQUE,
    email varchar(50) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    primary key (id));

ASSETS:
create template as a dir out there, it will contain all the apps' html
"DIRS": [os.path.join(BASE_DIR,'templates')], 
create static as a dir inside the project forlder, it will contain all the apps' css js images..ect
STATIC_URL = "static/"
STATICFILES_DIRS =[ os.path.join(BASE_DIR,'PlatformDb/static')]

ADMIN:

'''

cd .. #going back to parent directory
open command prompt: ctrl shift c
open vc code "  "  : ctrl shift p
{% LOGIC %}
python manage.py createsuperuser
admin: la_ouss
pw: tooldatabase

Encrypted password:
from django.contrib.auth.hashers import make_password
raw_pass = form.cleaned_data.get('password')
raw_pass = make_password(form.cleaned_data.get('password'))
'''

QUESTIONS:
header and footer css separate


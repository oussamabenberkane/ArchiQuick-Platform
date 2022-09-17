# Steps to follow

install python last version;

open command prompt;

INSIDE COMMAND PROMPT:
cd folderpath (folderpath example: C:\Users\Dell\Desktop\coding\ArchiQuick-platform)
pip install django
pip install pipenv
pipenv shell (this will set up your virtual environment)(the path is C:\Users\Dell\.virtualenvs\NAMEOFVENV)

open folder with vscode editor

IN VSCODE:
1- Activate virtual environment in vscode:
1 -> file from top menu 
2 -> Preferences
3 -> search for venv
4 -> find and copy the path of venv (the location is C:\Users\Dell\.virtualenvs\NAMEOFVENV\Scripts) (choose the activate.bat file)
5 -> double the slashes(C:\\Users\\Dell\\.virtualenvs\\NAMEOFVENV\\Scripts\\activate.bat)
6 -> you're done with this one close it and return to vscode main interface
7 -> go to views on top menu, choose command pallet
8 -> type python interpreter and choose the first one
9 -> click on Enter interpreter path
10 -> go to C:\Users\Dell\.virtualenvs\NAMEOFVENV\Scripts and select python.exe
11 -> all done return to main interface
12 -> go to view on top menu click on terminal
13 -> type this line of code: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser in terminal
14 -> open new terminal and your good to go :)

IN VSCODE TERMINAL:
python manage.py runserver
->you will see url in terminal that looks like: 127.0.0.8000 copy it and paste it in browser to view the platform.
-> you will not be able to create or login to an account given that i don't know how to upload a database yet.

-> if you want to recreate the database here's how:
1-install xampp from browser
2- IN COMMAND PROMPT:
-> cd c/xampp/mysql/bin
-> mysql -h localhost -u root (without password/ by default)  OR ..
.. mysql -u root -p (if you made a password to your mysql server)   
-> create database platform
-> use platform
-> create table users(id INT NOT NULL AUTO_INCREMENT,
    firstname varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    username varchar(50) NOT NULL,
    telephone varchar(20) NOT NULL UNIQUE,
    email varchar(50) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    primary key (id));
-> in vscode terminal:
    -> python manage.py makemigrations
    -> python manage.py migrate


and everything should be working fine ;)
 

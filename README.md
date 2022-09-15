## Steps to follow

install python last version;

open command prompt;

#inside command prompt:
cd folderpath (folderpath example: C:\Users\Dell\Desktop\coding\ArchiQuick-platform)
pip install django
pipenv shell (this will set up your virtual environment)(the path is C:\Users\Dell\.virtualenvs\NAMEOFVENV)

open folder with vscode editor

#in vscode:
1- Activate virtual environment in vscode:
File -> Preferences -> search for venv -> find and copy the path of venv (the location is C:\Users\Dell\.virtualenvs\NAMEOFVENV\Scripts) (chose the activate.bat file)-> double the slashes(C:\\Users\\Dell\\.virtualenvs\\NAMEOFVENV\\Scripts\\activate.bat)-> your done with this one close it and return to vscode main interface
-> go to views on top menu, chose command pallet -> type python interpreter and chose the first one -> click on Enter interpreter path -> go to C:\Users\Dell\.virtualenvs\NAMEOFVENV\Scripts and select python.exe -> all done return to main interface -> go to view on top menu click on terminal -> type this line of code: "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" in terminal -> open new terminal and your good to go :)

#in vscode terminal:
python manage.py runserver
->you will see url in terminal that looks like: 127.0.0.8000 copy it and paste it in browser to view the platform.
-> you will not be able to create or login to an account given that i don't know how to upload a database yet.
-> if you want to you can create it here's how:
1-install xampp from browser
2- #In command Prompt:
cd xampp\mysql\bin
mysql -h localhost -u root (without password, by default) mysql -u root -p (if you made a password to your mysql server)   
create database platform
use platform
create table users(id INT NOT NULL AUTO_INCREMENT,
    firstname varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    username varchar(50) NOT NULL,
    telephone varchar(20) NOT NULL UNIQUE,
    email varchar(50) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    primary key (id));
    
and everything should be working fine ;)
 

from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#   contact interface: chose between create new account and login existing one
def contactaction(request):
    return render(request, 'authentication/contact.html')


#   Logging in existing account
def loginaction(request):

    if request.user.is_authenticated:   #   in case the same url was requested while loged in.
        return HttpResponse(f'You are already active as {user.get_username}')

    if request.method == "POST":    #   post method from form in (authentication/login-page.html)

        #   fetch information from form
        active_user = request.POST['username']
        password = request.POST['password']

        #   connection to mysql database
        m = sql.connect(host="localhost", user="root", password="tool", database="platform")    

        #   setting cursor to manipulate database content
        cursor=m.cursor()   

        #   user variable contains session parameters (username and password)
        user = authenticate(request, username=active_user, password=password)   


        #   using the information from the table 'users'
        c = "select * from users where username='{}' and password='{}'".format(active_user, password)
        cursor.execute(c)

        #    fetching the tuple (username, password) if it exists from db
        t=tuple(cursor.fetchall()) 

        if user is not None and t != ():    #   if the user exists in local database and mysql database

            #   start user session
            login(request, user)    
           
            return redirect('../..') #   main platorm interface while user is now authenticated (profile and logout icons are added to partials/base.html)  
                                                                                 
        else:   #   if the user does not exist in database

            return render(request, 'authentication/error.html')   

    return render(request, 'authentication/login-page.html')
    

#   create account
def signupaction(request):

    if request.method == "POST":    #   post method from form in (authentication/signup-page.html)

        #   connection to mysql database
        m = sql.connect(host="localhost", user="root", password="tool", database="platform")    

        #   setting cursor to manipulate database content
        cursor=m.cursor()   

        #   fetching typed in information from form
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        username = request.POST['username']
        telephone = request.POST['telephone']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['password-confirmation']    #   confirmation variable is not saved in db, only used to check password confirmation

        #   creating a django user.
        p = "select * from users where username='{}' and password='{}'".format(username, password)
        cursor.execute(p)
        #    fetching the duplicate tuple username password if it exists from db
        t=tuple(cursor.fetchall()) 

        msg3= f'hi {username}, it seems like your account exists already in database'   #   in case tuple already exists

        if t==():
            #   creating the django user 
            myUser = User.objects.create_user(username, email, password)    
            myUser.first_name = firstname
            myUser.last_name = lastname
            myUser.save()
        else:
            messages.error(request, msg3)
            redirect ('login')

    
        #   saving the info into user table in mysql database
        c = "insert into users(firstname,lastname,username,telephone,email,password) Values('{}','{}','{}','{}','{}','{}')".format(firstname, lastname, username, telephone, email, password)
        cursor.execute(c)

        msg1= f'hi {username}, your account has been created successfully.'
        msg2 = f'hi {username}, please make sure you double check your password confirmation'

        #   checking password confirmation
        if password == confirmation:    
            m.commit()
            messages.success(request, msg1)
            return redirect('signup')
        else:
            messages.error(request, msg2)
            return redirect('signup')
    
    return render(request, 'authentication/signup-page.html')

#   logout from logout icon in main platform interface (_partials/base.html)

def logoutaction(request):

    logout(request)
    
    return redirect('home')


from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#   contact interface: chose between create new account and login existing one
def contactaction(request):
    return render(request, 'authentication/contact.html')

#   logout from logout logo in main platform inteface (_partials/base.html)
def logoutaction(request):
    global active_user

    logout(request)
    active_user = ''   #    resetting active_user to none
    return redirect('home')


#   Logging in existing account
def loginaction(request):

    global active_user  #   currently active user variable to use in other functions

    if request.user.is_authenticated:   #   in case the same url was requested while loged in.
        return HttpResponse(f'You are already active {active_user}')

    if request.method == "POST":    #   post method from form in (authentication/login-page.html)

        #   fetch information from form
        active_user = request.POST['username']
        password = request.POST['password']

        #   user variable now contains session parameters (username and password)
        user = authenticate(request, username=active_user, password=password)   

        if user is not None:    #   if the user exists in database

            #   start user session
            login(request, user)    

            return render(request, 'main/home.html', #   main platorm interface while user is now authenticated (profile and logout is added to partials/base.html)
            {'username': active_user})  #   {'username': active_user}: use variable in html with {{username}} 
                                                                                 
        else:   #   if the user does not exist in database

            return render(request, 'authentication/error.html')   

    return render(request, 'authentication/login-page.html')
    

#   create account
def signupaction(request):

    if request.method == "POST":    #   post method from form in (authentication/signup-page.html)

        #   connection to mysql database
        m = sql.connect(host="localhost", user="root", password="tool", database="platform")    

        cursor=m.cursor()   #   set cursor to manipulate database content

        #   fetch typed in information from form
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        username = request.POST['username']
        telephone = request.POST['telephone']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['password-confirmation']    #   confirmation variable is not saved in db, only used to check password confirmation

        #   create a django user.
        myUser = User.objects.create_user(username, email, password)    
        myUser.first_name = firstname
        myUser.last_name = lastname
        myUser.save()
        
        #   saving the info into user table in database
        c = "insert into users(firstname,lastname,username,telephone,email,password) Values('{}','{}','{}','{}','{}','{}')".format(firstname, lastname, username, telephone, email, password)
        cursor.execute(c)

        msg1= f'hi {username}, your account has been created successfully'
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


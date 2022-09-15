from django.shortcuts import render

#   main platform interface
def homeaction(request):
    return render(request, 'main/home.html')
    
#   user profile interface
def profileaction(request):
    return render(request, 'main/profile.html')
from django.shortcuts import render

def main_stackaction(request):
    return render(request, 'stack/main_page.html')
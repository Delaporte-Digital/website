from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')
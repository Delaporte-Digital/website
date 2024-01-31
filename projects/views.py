from django.shortcuts import render

# Create your views here.

def projects_list(request):
    return render(request, 'projects/projects_list.html')

def lipiam(request):
    return render(request, 'projects/lipiam.html')
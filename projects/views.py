from django.shortcuts import render


from .models import Projects

# Create your views here.
def projects_list(request):
    projects = Projects.objects.all()
    return render(request, 'projects/projects_list.html', { 'projects': projects })

def lipiam(request):
    return render(request, 'projects/lipiam.html')
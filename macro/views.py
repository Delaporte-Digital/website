from django.shortcuts import render

# Create your views here.
def macro(request):
    return render(request, 'list.html')
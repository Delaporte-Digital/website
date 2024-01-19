from django.shortcuts import render

# Create your views here.
def list_view(request):
    return render(request, 'blog/list.html')
from django.shortcuts import render
import requests
from django.http import JsonResponse

from .forms import SearchForm


# Create your views here.
def data(request):
    return render(request, 'data/list.html')

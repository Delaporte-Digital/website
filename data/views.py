from django.shortcuts import render
import requests

from .forms import SearchForm


# Create your views here.
def data(request):
    search_form = SearchForm()
    query = None
    data = ''
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/autocompletes"

            querystring = search_form.cleaned_data['search']
            # querystring = {"query": request.get('search')}
            print("-------------",querystring)

            headers = {
                "X-RapidAPI-Key": "19dac50c41msh49cc51a67fbc00ap1f76b4jsnddde907b1e2b",
                "X-RapidAPI-Host": "crunchbase-crunchbase-v1.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            print(response)
            return render(request, 'data/list.html', {'data': response})
    else:
        search_form = SearchForm()
    return render(request, 'data/list.html', {'search_form': search_form})
from django.shortcuts import render
import requests

# Create your views here.
def hedge(request):

    url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/autocompletes"

    querystring = {"query":"hedge funds"}

    headers = {
        "X-RapidAPI-Key": "19dac50c41msh49cc51a67fbc00ap1f76b4jsnddde907b1e2b",
        "X-RapidAPI-Host": "crunchbase-crunchbase-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json()['count'])
    return render(request, 'hedge/list.html')
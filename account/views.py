from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Profile

# Create your views here.

def profile(request):
    return render(request, 'profile.html')



def user_page(request, username):
    user_extend = get_object_or_404(Profile, username=username)
    return render(request, 'account/user_page.html', {'user_extend': user_extend})
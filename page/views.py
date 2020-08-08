from django.shortcuts import render
from page import views
#from .models import Word

# Create your views here.
def home(request):
  return render(request, 'home.html')

from django.shortcuts import render
from page import views

from django.http import HttpResponse
from .models import Collect

# Create your views here.
def home(request):
  word=Collect.objects.all() 
  return render(request, 'home.html', {'word':word})

def result(request):
  word=Collect.objects.all()
  str = ''
  for word in words:
    str += "영단어: {} 뜻: {} <br>".format(word.word, word.mean)
  return HttpResponse(str)

#def result(request,word_id):
#  word=get_object_or_404(Collect,pk=word_id)
#  return render(request,'result.html',{'word':word})

from django.shortcuts import render, redirect
from page import views

from django.http import HttpResponse
from .models import Collect

# Create your views here.
def home(request):
  words = Collect.objects.all() # Collect의 객체들을 words 변수에 담아주기
  return render(request, 'home.html')

def result(request):
  return render(request,'result.html',{'words':words})
  str = ''
  for word in words:
    str += "영단어: {} 뜻: {} <br>".format(words.word, words.mean)
  return HttpResponse(str)

#def result(request,word_id):
#  word=get_object_or_404(Collect,pk=word_id)
#  return render(request,'result.html',{'word':word})

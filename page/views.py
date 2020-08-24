from django.shortcuts import render, get_object_or_404
#from page import views
#from django.http import HttpResponse
from .models import Collect

# Create your views here.
def home(request):
  words = Collect.objects.all() # Collect의 객체들을 words 변수에 담아주기 
  #word_list = request.GET['words']
  word_list=[]
  return render(request, 'home.html',{'words':words},{'word_list':word_list})

def result(request,collect_id):
  collect_result = get_object_or_404(Collect, pk=collect_id)
  return render(request,'result.html',{'collect_result':collect_result})

 #str = ''
 #for words in word_list:
 #  str += "영단어: {} 뜻: {} <br>".format(words.word, words.mean)
# return HttpResponse(str)

from django.shortcuts import render

from .models import Question
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list' : latest_question_list           
            }
    return HttpResponse(template.render(context, request))

def detail(request,question_id):
    question =Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request,question_id):
    response = ' you are looking to response of question %s'
    return HttpResponse(response % question_id)

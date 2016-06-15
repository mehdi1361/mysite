from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
# Create your views here.
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#             'latest_question_list' : latest_question_list
#             }
#     return HttpResponse(template.render(context, request))
#
# def detail(request,question_id):
#     try:
# 	    question = get_object_or_404(Question, pk=question_id)
#     except:
# 	    raise Http404("question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#
# def result(request,question_id):
#     try:
# 	    question = get_object_or_404(Question, pk=question_id)
#     except:
# 	    raise Http404("choice does not exist")
#     return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])

	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': question, 'error_message':'you didint select a choice'})
	else:
		selected_choice.vote += 1
		selected_choice.save()
		return HttpResponse(reverse('result', args=(question.id, )))

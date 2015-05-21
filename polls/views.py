# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) 
    
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello world. You are at polls index.")

def detail(request,question_id):
   # try: 
   #     question = Question.objects.get(pk=question_id)
   # except Question.DoesNotExist: 
   #     raise Http404("Question does not exist")
   # return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
   #  response = "You're looking at the results of question %s."
   #  return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from polls.models import Question, Answer

# Create your views here.

def index(request):
    latestsQuestionsList = Question.objects.order_by('-publishDate')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{'latestsQuestionsList':latestsQuestionsList})
    #output = " , ".join( [recentQuestion.questionText for recentQuestion in latestsQuestionsList] )
    return HttpResponse(template.render(context))

def detail(request,questionID):
    return HttpResponse('Question ID: ' + str(questionID))

def results(request,questionID):
    return HttpResponse('Results for queston: ' + str(questionID))

def vote(request,questionID):
    return HttpResponse('Vote for queston: ' + str(questionID))

''' Old version rendering '''
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from polls.models import Question, Answer

# Create your views here.

def index(request):
    latestsQuestionsList = Question.objects.order_by('-publishDate')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{'latestsQuestionsList':latestsQuestionsList})
    #output is even older - it was used for testing. It can be safely deleted.
    #output = " , ".join( [recentQuestion.questionText for recentQuestion in latestsQuestionsList] )
    return HttpResponse(template.render(context))
'''
''' End new version rendering '''

from django.shortcuts import render
from django.http import Http404
from polls.models import Question, Answer

def index(request):
    latestsQuestionsList = Question.objects.order_by('-publishDate')[:5]
    context = {'latestsQuestionsList':latestsQuestionsList}
    return render(request,'polls/index.html',context) #render return a HTTP response.

def detail(request,questionID):
    try:
        question = Question.objects.get(pk=questionID) #Pk as in primary key
    except Question.DoesNotExist:
        raise Http404("This question does not exist.")
    else:
        return render(request,'polls/detail.html' , {'question':question})

def results(request,questionID):
    return HttpResponse('Results for question: ' + str(questionID))

def vote(request,questionID):
    return HttpResponse('Vote for question: ' + str(questionID))

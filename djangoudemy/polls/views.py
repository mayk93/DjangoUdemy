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
''' End old version rendering '''

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Question, Answer

''' Old 2 Index (Old 2 is different from old) '''
''' We replaced the url patterns un url.py (polls application urls) with generic views. '''
''' We now use a class instead of a method '''
''' The index function is used with the old urls in urls.py '''
'''
def index(request):
    latestsQuestionsList = Question.objects.order_by('-publishDate')[:5]
    context = {'latestsQuestionsList':latestsQuestionsList}
    return render(request,'polls/index.html',context) #render return a HTTP response.
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestsQuestionsList'

    def get_queryset(self):
        return Question.objects.order_by('-publishDate')[:5]

''' Old 2 Detail - See Old 2 above index '''
'''
def detail(request,questionID):
    #Django generally provides shortcuts for common tasks, like getting an object or raiseing 404 if not found.
    question = get_object_or_404(Question,pk=questionID)
    # try except block no longer needed because question will either be the search object or a 404 error
    """
    try:
        question = Question.objects.get(pk=questionID) #Pk as in primary key
    except Question.DoesNotExist:
        raise Http404("This question does not exist.")
    else:
    """
    return render(request,'polls/detail.html' , {'question':question})
'''

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

''' Old 2 results '''
'''
def results(request,questionID):
    question = get_object_or_404(Question,pk=questionID)
    context = {'question':question}
    return render(request,'polls/results.html' , context)
'''

class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question

def vote(request,questionID):
    question = get_object_or_404(Question,pk=questionID)
    try:
        '''
        In details.html, the form makes a POST request to the vote view.
        The value of the request is the id (primary key) of the answer.
        Here, we try to get that value by requesting the value associated with 'answer'
        '''
        selectedAnswer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError,Answer.DoesNotExist):
        context = {'question':question , 'error_message' : "You did not select a question."}
        return render(request,'polls/detail.html' , context)
    else:
        selectedAnswer.votes += 1
        selectedAnswer.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

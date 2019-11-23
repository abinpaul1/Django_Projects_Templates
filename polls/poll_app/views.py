from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    qlist = Question.objects.order_by('pub_date')[:5]
    #output = ','.join([q.question_text for q in qlist])
    dict = {'qlist':qlist}
    return render(request,'poll_app/index.html',context=dict)

def detail(request,question_id):
    #try:
    #    question = Question.objects.get_object_or_404(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"poll_app/detail.html",{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'poll_app/results.html',{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'poll_app/detail.html',{'question':question,'error_message':'Selct a choice.',})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_app:results', args=(question.id,)))

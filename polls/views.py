from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    question_list= Question.objects.all()
    choice_list=Choice.objects.all()
    context={'questions': question_list, 'choices': choice_list}
    return render(request, 'polls/home.html', context)
def quiz(request):
    if request.method=='POST':
        total = 0
        for q in Question.objects.all():
            if q.answer==int(request.POST[str(q.id)]):
                total+=1
        return HttpResponse('you score %s.'%total)
        
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
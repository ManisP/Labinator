from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Question, Lab
from django.template import loader
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]


class TestView(generic.ListView):
    template_name = 'polls/test.html'
    context_object_name = 'latest_labs'

    def get_queryset(self):
        return Lab.objects.order_by('pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class LabView(generic.DetailView):
    model = Lab
    template_name = 'polls/lab.html'


def submit(request, lab_id):
    lab = get_object_or_404(Lab, pk=lab_id)
    try:
        student_name = request.POST['student_name']
        student_email = request.POST['student_email']
        input_int = request.POST['input_int']
        input_int = int(input_int)
    except:
        return render(request, 'polls/test.html',{
            'lab': lab,
            'error_message':"Please enter another integer, this was not accepted",
        })
    else:
        lab.submission_set.create(student_name = student_name, student_email = student_email, input_int = input_int)
        return HttpResponseRedirect(reverse('polls:labresults', args=(lab.id,)))





class LabResultsView(generic.DetailView):
    model = Lab
    template_name = 'polls/labresults.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        newchoice_name = request.POST['newchoice_name']
        newchoice_votes = request.POST['newchoice_votes']
        newchoice_votes = int(newchoice_votes)
    except:
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message':"Improper Input.",
        })
    else:
        question.choice_set.create(choice_text = newchoice_name, votes = newchoice_votes)
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

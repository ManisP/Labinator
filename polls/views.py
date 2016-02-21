from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Question
from django.template import loader
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class TestView(generic.ListView):
    template_name = 'polls/test.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]

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

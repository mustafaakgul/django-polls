from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.template import loader
from django.urls import reverse

"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  #Return the last five published questions.
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
"""


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


"""
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
"""


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
"""


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


"""
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


"""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
"""
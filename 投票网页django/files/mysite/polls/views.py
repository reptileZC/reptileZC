from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    # 显示最新的5条问题
    questions = Question.objects.all().order_by('-pub_date')[:5]
    return render(request, "polls/index.html", {'questions': questions})


def detail(request, pk):
    q = get_object_or_404(Question, pk=pk)
    return render(request, "polls/detail.html", {'q': q})


def results(request, pk):
    q = get_object_or_404(Question, pk=pk)
    return render(request, "polls/results.html", {'q': q})


def vote(request, pk):
    """ 更新用户所选择的选项的投票总数 """
    q = get_object_or_404(Question, pk=pk)
    choice_pk = request.POST.get('choice')
    if not choice_pk or not choice_pk.isdigit():
        # 没有有效的choice_pk，出错
        error = "Please select a choice"
        return render(request, "polls/detail.html", {'q': q, 'error': error})
    choice_pk = int(choice_pk)
    choice = get_object_or_404(Choice, pk=choice_pk)
    choice.votes += 1
    choice.save()
    next_url = reverse('polls:results', args=(pk,))
    return HttpResponseRedirect(next_url)

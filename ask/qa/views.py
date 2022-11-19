from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST,require_GET
from django.core.paginator import Paginator
from django.urls import reverse
from qa.models import Question
from qa.models import Answer

require_GET
def question(request, id):
    try:
        post = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.get(question=post)
    except Answer.DoesNotExist:
        answers = None

    return render(request, 'question/question.html', {
        'question': post,
        'answers': answers
    })


require_GET
def newQuestion(request):
    return render(request, 'new/new.html')


@require_POST
def createQuestion(request):
    post = request.POST
    Question.objects.create(title = post.get('title'),text = post.get('text'))
    return HttpResponseRedirect('/')

require_GET
def mainPage(request):
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        raise Http404
    pages = Question.objects.new()
    paginator = Paginator(pages, limit)
    paginator.baseurl = '/?page='
    if page > paginator.num_pages or page < 1: raise Http404
    page = paginator.page(page)
    return render(request,'main/index.html',{
        'page': page,
        'paginator': paginator
    })


require_GET
def popular(request):
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        raise Http404
    pages = Question.objects.popular()
    paginator = Paginator(pages, limit)
    paginator.baseurl = reverse('popular') + '?page='
    if page > paginator.num_pages or page < 1: raise Http404
    page = paginator.page(page)
    return render(request,'popular/popular.html',{
        'page': page,
        'paginator': paginator
    })
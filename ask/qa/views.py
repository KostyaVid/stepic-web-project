from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.urls import reverse
from qa.models import Question
from qa.models import Answer
from qa.forms import AskForm, AnswerForm

def question(request, id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            url = request.path
            return HttpResponseRedirect(url)        
    else:
        form = AnswerForm()
        
    try:
        post = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404

    try:
        answers = Answer.objects.filter(question=post)[:]
    except Answer.DoesNotExist:
        answers = None

    return render(request, 'question/question.html', {
        'question': post,
        'answers': answers,
        'form': form
    })



def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)

    else:
        form = AskForm()
    return render(request, 'ask/ask.html',{
        'form': form
    })

@require_GET
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

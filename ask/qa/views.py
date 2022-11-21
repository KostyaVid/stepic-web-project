from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user
from django.urls import reverse
from qa.models import Question
from qa.models import Answer
from qa.forms import AskForm, AnswerForm, CreateUser, LoginUser

def question(request, id):
    if request.method == 'POST':
        user = get_user(request)
        form = AnswerForm( request.POST)
        if form.is_valid():
            form._user = user
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
        user = get_user(request)
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = user
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


@require_GET
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


def signup(request):
    if request.method == 'GET':
        form = CreateUser()
        return render(request, 'signup/signup.html',{
            'form':form
        })
    form = CreateUser(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return HttpResponseRedirect('/')

    return render(request, 'signup/signup.html',{
            'form':form
        })


def loginPage(request):
    if request.method == 'GET':
        form = LoginUser()
        return render(request, 'login/login.html',{
            'form':form
        })
    form = LoginUser(request.POST)
    if form.is_valid():
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)        
            return HttpResponseRedirect('/')
        else:
            err = u'Неправильный логин или пароль'
            return render(request, 'login/login.html',{
                'form':form,
                'err':err
            })


    return render(request, 'login/login.html',{
            'form':form
        })

@require_POST
def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect('/login/')
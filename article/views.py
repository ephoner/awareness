from django.shortcuts import render, Http404
from .models import Article, Category
# Create your views here.



def home(request):

    return render(request, 'home.html', locals() )


def awareness(request):
    try:
        cate = Category.objects.get(slug="awareness")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())

def concepts(request):
    try:
        cate = Category.objects.get(slug="concepts")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())

def yomedi(request):
    try:
        cate = Category.objects.get(slug="yomedi")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())

def zen(request):
    try:
        cate = Category.objects.get(slug="zen")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())


def qigong(request):
    try:
        cate = Category.objects.get(slug="qigong")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())


def mnemonics(request):
    try:
        cate = Category.objects.get(slug="mnemonics")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())


def books(request):
    try:
        cate = Category.objects.get(slug="books")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())


def media(request):
    try:
        cate = Category.objects.get(slug="media")
    except:
        Http404
    articles = Article.objects.filter(category=cate)

    return render(request, 'acticle_list.html', locals())


def article(request, pid):
    try:
        article = Article.objects.get(id=pid)

    except:
        return Http404

    return render(request, 'acticle.html', locals())

def about(request):

    return render(request, 'about.html', locals())


def donate(request):
    return render(request, 'donate.html', locals())
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.


def articleList(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/articles_list.html',{'articles':articles})

def article_detail(request,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    # print(article)
    return render(request,'articles/article_detail.html',{'article':article})

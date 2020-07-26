from django.http import HttpResponse
from django.shortcuts import render


def homepageFunc(request):
    # return HttpResponse('Homepage')
    return render(request,'homepage.html')


def aboutFunc(request):
    return render(request,'about.html')
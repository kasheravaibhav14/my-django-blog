from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('',views.articleList),
    path('<slug:slug>',views.article_detail, name="slugUrl"),
]

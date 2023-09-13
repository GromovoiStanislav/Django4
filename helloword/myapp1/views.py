from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request,'index.html')


def page_not_found(request, exсeption):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

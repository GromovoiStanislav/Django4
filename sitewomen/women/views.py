from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

# Create your views here.

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
       Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': True},
    {'id': 3, 'title': 'Сандра Баллок', 'content': 'Биография Сандра Баллок', 'is_published': False},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Спортсменки'},
    {'id': 3, 'name': 'Певицы'},
]


def index(request):
    # return HttpResponse("<h1>Старница приложения women</h1>")

    # t = render_to_string('women/index.html')
    # return HttpResponse(t)

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'title': 'О сайте', 'menu': menu}
    return render(request, 'women/about.html', data)


def show_post(request, post_id):
    return HttpResponse(f"<h1>Статья с ID: {post_id}</h1>")


def add_page(request):
    return HttpResponse(f"<h1>Добавить статью</h1>")


def contact(request):
    return HttpResponse(f"<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse(f"<h1>Авторизация</h1>")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    # return HttpResponseNotFound("<h1>Старница не найдена</h1>")
    try:
        print('Страница не найдена')
        return HttpResponseNotFound("<h1>Страница не найдена</h1>")
    except Exception as e:
        print(e)
        return HttpResponseServerError("<h1>Произошла ошибка на сервере</h1>")

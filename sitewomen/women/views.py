from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

# Create your views here.
menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анжелина Джоли', 'content': 'Биография Анжелина Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': True},
    {'id': 3, 'title': 'Сандра Баллок', 'content': 'Биография Сандра Баллок', 'is_published': False},
]


def index(request):
    # return HttpResponse("<h1>Старница приложения women</h1>")

    # t = render_to_string('women/index.html')
    # return HttpResponse(t)

    data = {
        'title': 'главная Страница!',
        'main_title': '',
        'menu': menu,
        'posts': data_db,
        'slug': '"The Main Page!"',
        'sluged': slugify('"The Main Page!"'),
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'women/about.html', data)


def categopies(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categopies_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        # raise Http404()
        # return redirect('/', permanent=True) # 301 or 302
        # return redirect(index)
        # return redirect('home')
        # return redirect('cats', 'music')
        uri = reverse('cats', args=('video',))
        # return redirect(uri)
        # return HttpResponseRedirect(uri) # 302
        return HttpResponsePermanentRedirect('/')  # 301
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exeption):
    # return HttpResponseNotFound("<h1>Старница не найдена</h1>")
    try:
        print('Страница не найдена')
        return HttpResponseNotFound("<h1>Страница не найдена</h1>")
    except Exception as e:
        print(e)
        return HttpResponseServerError("<h1>Произошла ошибка на сервере</h1>")

from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('addpage/', views.add_page, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),




    # path('cats/<int:cat_id>/', views.categopies, name='cats_id'),
    # path('cats/<slug:cat_slug>/', views.categopies_by_slug, name='cats'),
    # # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive, name='archive')
    # path("archive/<year4:year>/", views.archive, name='archive')
]

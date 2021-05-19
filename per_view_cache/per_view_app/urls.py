from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('cache/', cache_page(30)(views.index_view), name="cache"),
    path('home/', views.index_view, name="home"),
    path('none_cache/', views.non_cache_view, name="non"),
]

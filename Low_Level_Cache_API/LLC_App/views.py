from django.shortcuts import render
from django.core.cache import cache


# Create your views here.

# def index(request):
#     mv = cache.get('movie','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','Interstellar',30)
#         mv=cache.get('movie')
#     return render(request, 'LLC_App/index.html',{'mv':mv})


def index(request):
    mv = cache.get_or_set('fees',54000,30,version=2)
    return render(request, 'LLC_App/index.html',{'mv':mv})
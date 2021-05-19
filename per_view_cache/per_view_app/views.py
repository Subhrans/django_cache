from django.shortcuts import render
# from django.views.decorators.cache import cache_page


# Create your views here.
# @cache_page(30)
def index_view(request):
    return render(request, 'app/index.html')


def non_cache_view(request):
    return render(request, 'app/contact.html')

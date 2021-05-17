from django.contrib import admin
from django.urls import path
from app2 import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(30)(views.index_view)),
    path('gomew/',views.index_view, name="gome"),
]

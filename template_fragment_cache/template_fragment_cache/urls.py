from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fragment/',TemplateView.as_view(template_name="app/index.html"),name="index"),
]

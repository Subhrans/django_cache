from django.shortcuts import render


# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'app2/index.html'

def index_view(request):
    return render(request, 'app2/index.html')

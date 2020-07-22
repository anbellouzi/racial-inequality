from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

# Create your views here.
class HomePage(ListView):

    def get(self, request):
        context = {"hi": "world"}
        return render(request, 'main/index.html', context)
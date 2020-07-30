from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

# Create your views here.
class HomePage(ListView):

    def get(self, request):
        context = {"hi": "world"}
        return render(request, 'main/index.html', context)



class AboutPage(ListView):

    def get(self, request):
        context = {"hi": "world"}
        return render(request, 'main/about.html', context)


class StoryPage(ListView):

    def get(self, request):
        context = {"hi": "world"}
        return render(request, 'main/story.html', context)


class RadiumPage(ListView):

    def get(self, request):
        context = {"hi": "world"}
        return render(request, 'main/radium.html', context)

class CitationPage(ListView):

    def get(self, request):
        context = {"hi": "world"}
        return render(request, 'main/citation.html', context)


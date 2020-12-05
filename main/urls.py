"""womenhistory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('1992-twilight/', views.AboutPage.as_view(), name='about'),
    path('13th-alec/', views.StoryPage.as_view(), name='story'),
    path('compare-1992-twilight-vs-13th/', views.RadiumPage.as_view(), name='radium'),
    path('citation/', views.CitationPage.as_view(), name='citation'),
]

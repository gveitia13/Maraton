from django.shortcuts import render
from django.urls import path

urlpatterns = [
    path('', lambda request: render(request, 'pages/start_page.html'), name='index'),

]

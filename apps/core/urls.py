from django.shortcuts import render
from django.urls import path

from apps.core.views.admin.marabana import *

urlpatterns = [
    path('', lambda request: render(request, 'pages/start_page.html')
    if request.user.is_authenticated else render(request, 'pages/start_page.html'), name='index'),
    # Marabana
    path('crear-info-marabana/', MarabanaCreate.as_view(), name='marabana-create'),
    path('eliminar-info-marabana/<int:pk>/', MarabanaDelete.as_view(), name='marabana-delete'),
    path('editar-info-marabana/<int:pk>/', MarabanaUpdate.as_view(), name='marabana-update'),
]

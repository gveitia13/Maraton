from django.shortcuts import render
from django.urls import path

from apps.core.views.admin.extra_info import *
from apps.core.views.admin.marabana import *

urlpatterns = [
    path('', lambda request: render(request, 'pages/start_page.html')
    if request.user.is_authenticated else render(request, 'pages/start_page.html'), name='index'),
    # Marabana
    path('crear-info-marabana/', MarabanaCreate.as_view(), name='marabana-create'),
    path('eliminar-info-marabana/<int:pk>/', MarabanaDelete.as_view(), name='marabana-delete'),
    path('editar-info-marabana/<int:pk>/', MarabanaUpdate.as_view(), name='marabana-update'),
    # Extra Infor
    path('extra-info-list/', ExtraInformationList.as_view(), name='extra-info-list'),
    path('extra-info-create/', ExtraInformationCreate.as_view(), name='extra-info-create'),
    path('extra-info-update/<int:pk>/', ExtraInformationUpdate.as_view(), name='extra-info-update'),
    path('extra-info-delete/<int:pk>/', ExtraInformationDelete.as_view(), name='extra-info-delete'),
]

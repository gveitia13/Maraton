from django.shortcuts import render
from django.urls import path

from apps.core.views.admin.campeonato import *
from apps.core.views.admin.contact import *
from apps.core.views.admin.extra_info import *
from apps.core.views.admin.fotografia import *
from apps.core.views.admin.marabana import *
from apps.core.views.admin.notice import *
from apps.core.views.admin.rule import *

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
    # Rule
    path('rule-list/', RuleList.as_view(), name='rule-list'),
    path('rule-create/', RuleCreate.as_view(), name='rule-create'),
    path('rule-update/<int:pk>/', RuleUpdate.as_view(), name='rule-update'),
    path('rule-delete/<int:pk>/', RuleDelete.as_view(), name='rule-delete'),
    # Campeonato
    path('champion-list/', CampeonatoList.as_view(), name='champion-list'),
    path('champion-create/', CampeonatoCreate.as_view(), name='champion-create'),
    path('champion-update/<int:pk>/', CampeonatoUpdate.as_view(), name='champion-update'),
    path('champion-delete/<int:pk>/', CampeonatoDelete.as_view(), name='champion-delete'),
    # Noticia
    path('notice-list/', NoticeList.as_view(), name='notice-list'),
    path('notice-create/', NoticeCreate.as_view(), name='notice-create'),
    path('notice-update/<int:pk>/', NoticeUpdate.as_view(), name='notice-update'),
    path('notice-delete/<int:pk>/', NoticeDelete.as_view(), name='notice-delete'),
    # Fotografiá
    path('fotografia-list/', FotografiaList.as_view(), name='fotografia-list'),
    path('fotografia-create/', FotografiaCreate.as_view(), name='fotografia-create'),
    path('fotografia-update/<int:pk>/', FotografiaUpdate.as_view(), name='fotografia-update'),
    path('fotografia-delete/<int:pk>/', FotografiaDelete.as_view(), name='fotografia-delete'),
    # Contacto
    path('contact-list/', ContactList.as_view(), name='contact-list'),
    path('contact-create/', ContactCreate.as_view(), name='contact-create'),
    path('contact-update/<int:pk>/', ContactUpdate.as_view(), name='contact-update'),
    path('contact-delete/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),
]

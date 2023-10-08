from django.urls import path

from apps.core.views.campeonato import *
from apps.core.views.category import *
from apps.core.views.contact import *
from apps.core.views.extra_info import *
from apps.core.views.fotografia import *
from apps.core.views.index import IndexView
from apps.core.views.inscription import *
from apps.core.views.marabana import *
from apps.core.views.notice import *
from apps.core.views.rule import *
from apps.core.views.users import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
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
    # Inscription
    path('inscription-list/', InscriptionList.as_view(), name='inscription-list'),
    path('inscription-create/', InscriptionCreate.as_view(), name='inscription-create'),
    path('inscription-delete/<int:pk>/', InscriptionDelete.as_view(), name='inscription-delete'),
    # Category
    path('category-list/', CategoryList.as_view(), name='category-list'),
    path('category-create/', CategoryCreate.as_view(), name='category-create'),
    path('category-delete/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),
    path('category-update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
    # User
    path('user-list/', ListarUsuario.as_view(), name='user-list'),
    path('user-create/', CrearUsuario.as_view(), name='user-create'),
    path('user-delete/<int:pk>/', EliminarUsuario.as_view(), name='user-delete'),
    path('user-update/<int:pk>/', EditarUsuario.as_view(), name='user-update'),
]

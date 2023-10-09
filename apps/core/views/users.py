from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.forms import MyUserForm


class CrearUsuario(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('user-list')
    form_class = MyUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Usuario'
        context['back_url'] = self.success_url
        return context


class EditarUsuario(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('user-list')
    form_class = MyUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Editar Usuario'
        context['back_url'] = self.success_url
        return context


class EliminarUsuario(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Usuario'
        context['back_url'] = self.success_url
        return context


class ListarUsuario(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    template_name = 'user/user-list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(username__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Usuarios'
        context['add_url'] = reverse_lazy('user-create')
        return context

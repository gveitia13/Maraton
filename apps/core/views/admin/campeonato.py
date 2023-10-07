from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Campeonato


class CampeonatoCreate(LoginRequiredMixin, generic.CreateView):
    model = Campeonato
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('champion-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Campeonato'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class CampeonatoUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Campeonato
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('champion-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Campeonato: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class CampeonatoList(LoginRequiredMixin, generic.ListView):
    model = Campeonato
    template_name = 'title_text_base/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Campeonatos'
        context['add_url'] = reverse_lazy('champion-create')
        context['update_url'] = '/champion-update/'
        context['delete_url'] = '/champion-delete/'
        return context


class CampeonatoDelete(LoginRequiredMixin, generic.DeleteView):
    model = Campeonato
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('champion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Campeonato'
        context['back_url'] = self.success_url
        return context

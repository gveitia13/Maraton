from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Inscription


class InscriptionCreate(generic.CreateView):
    model = Inscription
    template_name = 'inscription/create.html'
    success_url = reverse_lazy('inscription-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Inscribirse'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context

    def get_success_url(self):
        success_url = super().get_success_url()
        if self.request.user.is_authenticated:
            return success_url
        return reverse_lazy('index')


class InscriptionList(generic.ListView):
    model = Inscription
    template_name = 'inscription/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Inscripciones'
        context['add_url'] = reverse_lazy('inscription-create')
        context['update_url'] = '/inscription-update/'
        context['delete_url'] = '/inscription-delete/'
        return context


class InscriptionDelete(LoginRequiredMixin, generic.DeleteView):
    model = Inscription
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('inscription-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Inscripción'
        context['back_url'] = self.success_url
        return context

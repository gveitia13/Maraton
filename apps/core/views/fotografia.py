from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Fotografia


class FotografiaCreate(LoginRequiredMixin, generic.CreateView):
    model = Fotografia
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('fotografia-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Fotografía'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class FotografiaUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Fotografia
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('fotografia-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Fotografía: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class FotografiaList(generic.ListView):
    model = Fotografia
    template_name = 'fotografia/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Fotografías'
        context['add_url'] = reverse_lazy('fotografia-create')
        context['update_url'] = '/fotografia-update/'
        context['delete_url'] = '/fotografia-delete/'
        return context


class FotografiaDelete(LoginRequiredMixin, generic.DeleteView):
    model = Fotografia
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('fotografia-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Fotografía'
        context['back_url'] = self.success_url
        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Notice


class NoticeCreate(LoginRequiredMixin, generic.CreateView):
    model = Notice
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('notice-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Noticia'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class NoticeUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Notice
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('notice-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Noticia: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class NoticeList(generic.ListView):
    model = Notice
    template_name = 'notice/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Noticias'
        context['add_url'] = reverse_lazy('notice-create')
        context['update_url'] = '/notice-update/'
        context['delete_url'] = '/notice-delete/'
        return context


class NoticeDelete(LoginRequiredMixin, generic.DeleteView):
    model = Notice
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('notice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Noticia'
        context['back_url'] = self.success_url
        return context

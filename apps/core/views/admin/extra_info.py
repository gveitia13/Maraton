from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import ExtraInformation


class ExtraInformationCreate(LoginRequiredMixin, generic.CreateView):
    model = ExtraInformation
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('extra-info-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Información Extra'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class ExtraInformationUpdate(LoginRequiredMixin, generic.UpdateView):
    model = ExtraInformation
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('extra-info-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Información Extra: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class ExtraInformationList(LoginRequiredMixin, generic.ListView):
    model = ExtraInformation
    # template_name = 'pages/table-list.html'
    template_name = 'extra_info/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Informaciones Extras'
        context['add_url'] = reverse_lazy('extra-info-create')
        return context


class ExtraInformationDelete(LoginRequiredMixin, generic.DeleteView):
    model = ExtraInformation
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('extra-info-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Información Extra'
        context['back_url'] = self.success_url
        return context

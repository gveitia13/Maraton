from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Result


class ResultCreate(LoginRequiredMixin, generic.CreateView):
    model = Result
    template_name = 'result/create-update.html'
    success_url = reverse_lazy('result-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Registrar Resultado de carrera'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class ResultUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Result
    template_name = 'result/create-update.html'
    success_url = reverse_lazy('result-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Resultado: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class ResultList(LoginRequiredMixin, generic.ListView):
    model = Result
    template_name = 'result/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Resultados de Carreras'
        context['add_url'] = reverse_lazy('result-create')
        context['update_url'] = '/result-update/'
        context['delete_url'] = '/result-delete/'
        return context


class ResultDelete(LoginRequiredMixin, generic.DeleteView):
    model = Result
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('result-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Resultado'
        context['back_url'] = self.success_url
        return context

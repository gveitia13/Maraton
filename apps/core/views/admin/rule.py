from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Rule


class RuleCreate(LoginRequiredMixin, generic.CreateView):
    model = Rule
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('rule-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Regla'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class RuleUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Rule
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('rule-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Regla: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class RuleList(LoginRequiredMixin, generic.ListView):
    model = Rule
    template_name = 'title_text_base/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Reglas'
        context['add_url'] = reverse_lazy('rule-create')
        context['update_url'] = '/rule-update/'
        context['delete_url'] = '/rule-delete/'
        return context


class RuleDelete(LoginRequiredMixin, generic.DeleteView):
    model = Rule
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('rule-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Regla'
        context['back_url'] = self.success_url
        return context

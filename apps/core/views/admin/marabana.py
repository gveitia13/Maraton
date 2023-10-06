from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import GeneralInformation


class MarabanaCreate(LoginRequiredMixin, generic.CreateView):
    template_name = 'pages/create-marabana.html'
    model = GeneralInformation
    success_url = reverse_lazy('index')
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        marabana = GeneralInformation.objects.first() if GeneralInformation.objects.exists() else None
        if marabana:
            return redirect(reverse_lazy('marabana-update', kwargs={'pk': marabana.pk}))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'{"Crear"} Información del Marabana'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class MarabanaUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name = 'pages/update-marabana.html'
    model = GeneralInformation
    success_url = reverse_lazy('index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'{"Editar"} Información del Marabana'
        context['back_url'] = self.success_url
        return context


class MarabanaDelete(LoginRequiredMixin, generic.DeleteView):
    model = GeneralInformation
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Información del Marabana'
        context['back_url'] = reverse_lazy('marabana-update', kwargs={'pk': self.get_object().pk})
        return context

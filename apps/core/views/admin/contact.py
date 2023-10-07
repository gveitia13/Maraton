from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Contact


class ContactCreate(LoginRequiredMixin, generic.CreateView):
    model = Contact
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('contact-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Contacto'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class ContactUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Contact
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('contact-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Contacto: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class ContactList(generic.ListView):
    model = Contact
    template_name = 'contact/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Contactos'
        context['add_url'] = reverse_lazy('contact-create')
        context['update_url'] = '/contact-update/'
        context['delete_url'] = '/contact-delete/'
        return context


class ContactDelete(LoginRequiredMixin, generic.DeleteView):
    model = Contact
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('contact-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Contacto'
        context['back_url'] = self.success_url
        return context

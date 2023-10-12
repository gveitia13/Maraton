from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from Maraton import settings
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
        messages.success(self.request,
                         'Su inscripción está pendiente a aprobación. Se le notificará por correo cuando sea aceptada')
        if self.request.user.is_authenticated:
            return success_url
        return reverse_lazy('index')


class InscriptionList(generic.ListView):
    model = Inscription
    template_name = 'inscription/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(name__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Inscripciones'
        context['add_url'] = reverse_lazy('inscription-create')
        context['update_url'] = '/inscription-update/'
        context['delete_url'] = '/inscription-delete/'
        # context['result_create'] = '/result-create/'
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


class InscriptionUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Inscription
    template_name = 'inscription/activate.html'
    success_url = reverse_lazy('inscription-list')
    fields = ['is_active']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Inscripción'
        context['back_url'] = self.success_url
        return context

    def post(self, request, *args, **kwargs):
        inscription: Inscription = self.get_object()
        try:
            send_mail('Inscripción aprobada!',
                      message='Su inscripción ha sido aprobada. Ya puede participar en el Marabana. Éxitos!',
                      recipient_list=[inscription.email], from_email=settings.EMAIL_HOST_USER)
            print('se envio el mail')
        except Exception as e:
            print(str(e))
        return super().post(request, *args, **kwargs)

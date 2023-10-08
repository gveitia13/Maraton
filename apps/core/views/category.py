from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Category


class CategoryCreate(LoginRequiredMixin, generic.CreateView):
    model = Category
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('category-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Categoría'
        context['back_url'] = self.success_url
        context['is_create'] = True
        return context


class CategoryUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Category
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('category-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Categoría: {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class CategoryList(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'title_text_base/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(title__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Categorías'
        context['add_url'] = reverse_lazy('category-create')
        context['update_url'] = '/category-update/'
        context['delete_url'] = '/category-delete/'
        return context


class CategoryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Category
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('category-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Categoría'
        context['back_url'] = self.success_url
        return context

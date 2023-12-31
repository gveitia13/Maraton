from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from apps.core.models import Result, categories


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


class ResultList(generic.ListView):
    model = Result
    template_name = 'result/list.html'
    queryset = Result.objects.all().order_by('-date')

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            qs = qs.filter(name__icontains=self.request.GET.get('search'))
        if self.request.GET.get('year'):
            qs = qs.filter(date__year=self.request.GET.get('year'))
        if self.request.GET.get('category'):
            qs = qs.filter(category=self.request.GET.get('category'))
        return qs

    def post(self, request, *args, **kwargs):
        qs = self.queryset
        year, category = self.request.POST.get('year'), self.request.POST.get('category')
        if year:
            qs = qs.filter(date__year=year)
        if category:
            qs = qs.filter(category=category)
        print(qs)
        if not category and year:
            string = f'Resultados históricos de las carreras del año {year}'
        elif not year and category:
            string = f'Resultados históricos de las carreras de la categoría {dict(categories)[category]}'
        elif not year and not category:
            string = f'Resultados históricos de las carreras'
        else:
            string = f'Resultados históricos de las carreras de la categoría {dict(categories)[category]} del año {year}'
        print(string)

        results = []
        for category, value in categories:
            if qs.filter(category=category).exists():
                results.append({'title': value, 'list': qs.filter(category=category)})

        return render(request, 'result/history.html',
                      context={'object_list': qs,
                               'text': string, 'results': results})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Resultados de Carreras'
        context['add_url'] = reverse_lazy('result-create')
        context['update_url'] = '/result-update/'
        context['delete_url'] = '/result-delete/'
        context['years'] = [i.date.year for i in self.queryset]
        context['categories'] = categories
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

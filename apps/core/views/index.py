from django.views.generic import TemplateView

from apps.core.models import GeneralInformation, Category, ExtraInformation


class IndexView(TemplateView):
    template_name = 'pages/start_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['marabana'] = GeneralInformation.objects.first() if GeneralInformation.objects.exists() else None
        context['category_list'] = Category.objects.all()
        context['text'] = 'Marabana 2023'
        context['extra_info_list'] = ExtraInformation.objects.all()
        return context

from apps.core.models import GeneralInformation


class GlobalContext:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.marabana = GeneralInformation.objects.first() if GeneralInformation.objects.exists() else None

        response = self.get_response(request)
        return response

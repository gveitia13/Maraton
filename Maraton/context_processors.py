from apps.core.models import GeneralInformation


def mi_variable_global(request):
    # Obtén la variable global desde la solicitud (request)
    marabana = GeneralInformation.objects.first() if GeneralInformation.objects.exists() else None

    # Define un diccionario con la variable que deseas agregar al contexto
    context = {
        'marabana': marabana,
    }

    return context

from django.http import HttpResponse


def home(request):
    """Display the required assignment message."""
    return HttpResponse("Ddamulira says Hello!")
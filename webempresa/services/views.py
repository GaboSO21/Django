from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    servicios = Service.objects.all()
    context = {'services': servicios}
    return render(request, 'services/services.html', context)


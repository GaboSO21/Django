from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def page(request, pk):
    page = get_object_or_404(Page, id=pk)
    context = {'page': page}
    return render(request, 'pages/sample.html', context)

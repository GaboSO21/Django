from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def about(request):
    context = {}
    return render(request, 'core/about-me.html', context)

def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)

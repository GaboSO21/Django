from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # mandar email
            return redirect(reverse('contact')+'?ok')

    context = {'form': contact_form}
    return render(request, 'contact/contact.html', context)

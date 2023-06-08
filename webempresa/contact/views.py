from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.mail import EmailMessage
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
            # Enviar email y redirect
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',# asunto,
                f'De: {name} <{email}>\n\nEscribio:\n\n{content}',# cuerpo,
                'no-contestar@inbox.mailtrap.io',# email_origen,
                ['gso2090@gmail.com'],# email_destino,
                reply_to=[email]
            )

            try:
                email.send()
                # Todo ha ido bien
                return redirect(reverse('contact')+'?ok')

            except: 
                # Algo no ha salido bien
                return redirect(reverse('contact')+'?fail')


    context = {'form': contact_form}
    return render(request, 'contact/contact.html', context)

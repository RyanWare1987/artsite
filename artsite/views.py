from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_number = request.POST.get('contact_number', '')
            form_content = request.POST.get('content', '')

            #Here we email the profile with the contact info
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_number': contact_number,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content, "Your Website" +'',
                ['ryan.ware1987@gmail.com'],
                headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
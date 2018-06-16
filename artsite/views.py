from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import ContactForm

def index(request):
    """
    Simple handler for the index page
    """
    return render(request, 'index.html')

def about(request):
    """
    Simple handler for the about page
    """
    return render(request, 'about.html')

def contact(request):
    """
    This is the handler for the Contact Us Page, where we us a
    bootstrap contact form, for a user to enter details and a 
    comment which will user sendgrid to fire an email over into
    a specified inbox, with information for which I can reply to.
    """
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_number = request.POST.get('contact_number', '')
            form_content = request.POST.get('content', '')

            """
            Here we ensure the correct values are assigned
            to each form input
            """
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_number': contact_number,
                'form_content': form_content,
            }
            content = template.render(context)

            """
            Here the email is sent to a 
            designated email address via
            sendgrid
            """
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
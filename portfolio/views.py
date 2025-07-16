from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    form = ContactForm(request.POST or None)
    success = False

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        send_mail(
            subject=f"Contact Form Submission from {name}",
            message=message,   
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_TO_EMAIL],
            fail_silently=False,
        )
        success = True
        form = ContactForm()
    return render(request, "contact.html", {
        'form': form,
        'success': success
    })

from .models import ContactMessage  # Import the model

def contact(request):
    form = ContactForm(request.POST or None)
    success = False

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email (optional for now)
        send_mail(
            subject=f"Contact Form Submission from {name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        success = True
        form = ContactForm()

    return render(request, "contact.html", {
        'form': form,
        'success': success
    })

def robots_txt(request):
    content = loader.render_to_string("robots.txt")
    return HttpResponse(content, content_type="text/plain")


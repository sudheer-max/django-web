from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    title = 'Write to us:'
    form = ContactForm(request.POST)
    confirm_message = None
    

    if form.is_valid():
        form.save()
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        subject = 'Message from intellect innovation'
        message = form.cleaned_data['message']
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, email_to, fail_silently=True)
        title = 'Thanks for the message!!'
        confirm_message = 'Thanks for the message, We will get right back to your shorly!!!'
        form = None
        
    context = {'title' : title,'form' : form, 'confirm_message' : confirm_message, }
    template = 'contact.html'
    return render(request, template, context)
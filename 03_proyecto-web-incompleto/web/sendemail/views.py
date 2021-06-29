from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from sendemail.forms import ContactForm

# Create your views here.
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_Email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message,from_email,['jackson1reyes2@gmail.com'],fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request,'email.html',{'form':form})

def successView(request):
    return HttpResponse('Enviado! Gracias por el mensaje.')
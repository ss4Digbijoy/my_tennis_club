from django.shortcuts import render
from django.http import HttpResponse
from .forms import contfr
from django.conf import settings
from django.core.mail import send_mail
def members(request):
    print(request.user)
    return HttpResponse("Hello world!")

def Nav(request):
    return render(request,'Nav.html', {})
def About(request):
    return render(request, "About2.html",{})
def Contact(request):
    if request.method=="POST":
        form=contfr(request.POST)
        if form.is_valid():
            Name=form.cleaned_data["Name"]
            email=form.cleaned_data["email"]
            msg=form.cleaned_data["msg"]
            subject = f'CLIENT NAME: {Name}'
            message = f'from: {email}\n{msg}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER, ]
            send_mail( subject, message, email_from, recipient_list )
            form=contfr()
            return render(request,"Contact.html",{'form':form, 'done':"done"})
        else:
            return render(request,"Contact.html",{'form':form})
        
    form=contfr()
    return render(request,"Contact.html",{'form':form})
def pot(request):
    return render(request,"ngal2.html", {})
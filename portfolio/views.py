from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        phnumber = request.POST.get("phone")
        ext = request.POST.get("country_code")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        query = Contact(name=name,email=email,phone=phnumber,ext=ext,subject=subject,description=message)
        query.save()

        # Send email notification to yourself
        send_mail(
            subject=f'New Contact Form Submission: {subject}',
            message=f'Name: {name}\nEmail: {email}\nPhone: {ext} {phnumber}\n\nMessage:\n{message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Your email to receive the contact form submission
            fail_silently=False,
        )

        messages.success(request,"Thank you! Your email has been sent. I will respond shortly.")
        return redirect("/contact")
    return render(request,'contact.html')

def resume(request):
    return render(request,'resume.html')


def services(request):
    return render(request,'services.html')
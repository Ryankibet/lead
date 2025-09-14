from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def features(request):
    return render(request, "features.html")

def portfolio(request):
    return render(request, "portfolio.html")

def pricing(request):
    return render(request, "pricing.html")

def services(request):
    return render(request, "services.html")

def testimonials(request):
    return render(request, "teastimonials.html")

def team(request):
    return render(request, "team.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save directly to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent. Thank you!")
        return redirect("leadpage:contact")

    return render(request, "contact.html")


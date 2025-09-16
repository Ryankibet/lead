from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ContactMessage
from .forms import ContactForm


# ---------------------------
# Static Pages
# ---------------------------
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
    return render(request, "testimonials.html")

def team(request):
    return render(request, "team.html")

# ---------------------------
# CONTACT FORM (CREATE)
@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save(commit=False)
            if request.user.is_authenticated:
                contact_msg.user = request.user
            contact_msg.save()
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect("leadpage:messages_list")
    else:
        form = ContactMessage()
    return render(request, "contact.html", {"form": form})

# ---------------------------
# LIST (READ)
# ---------------------------
@login_required
def contact_messages_list(request):
    if request.user.is_staff or request.user.is_superuser:
        msgs = ContactMessage.objects.all().order_by("-created_at")
    else:
        msgs = ContactMessage.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "messages_list.html", {"messages": msgs})

# ---------------------------
# UPDATE
# ---------------------------
def contact_message_update(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=message)  # ✅ correct
        if form.is_valid():
            form.save()
            messages.success(request, "Message updated successfully.")
            return redirect("leadpage:messages_list")
    else:
        form = ContactForm(instance=message)  # ✅ correct

    return render(request, "contact_form.html", {"form": form})

# ---------------------------
# DELETE
# ---------------------------
@login_required
def contact_message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)

    # Only allow owner or admin
    if not (request.user == msg.user or request.user.is_staff):
        messages.error(request, "You do not have permission to delete this message.")
        return redirect("leadpage:messages_list")

    if request.method == "POST":
        msg.delete()
        messages.success(request, "Message deleted successfully.")
        return redirect("leadpage:messages_list")

    return render(request, "message_confirm_delete.html", {"object": msg})

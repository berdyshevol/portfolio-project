from django.shortcuts import redirect, render

from projects.models import Project

from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    return render(request, "core/home.html", {"featured_projects": featured_projects})


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:contact_thanks")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})


def contact_thanks(request):
    return render(request, "core/contact_thanks.html")

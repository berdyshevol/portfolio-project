from django.shortcuts import render

from .models import Education, Experience


def show(request):
    return render(
        request,
        "resume/show.html",
        {
            "experiences": Experience.objects.all(),
            "education": Education.objects.all(),
        },
    )

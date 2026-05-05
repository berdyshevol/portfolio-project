from django.shortcuts import get_object_or_404, render

from .models import Project


def project_list(request):
    return render(request, "projects/list.html", {"projects": Project.objects.all()})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "projects/detail.html", {"project": project})

from django.http import HttpResponse


def project_list(request):
    return HttpResponse("projects")


def project_detail(request, slug):
    return HttpResponse(f"project {slug}")

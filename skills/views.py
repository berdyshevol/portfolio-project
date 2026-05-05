from django.http import HttpResponse


def skill_list(request):
    return HttpResponse("skills")

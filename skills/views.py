from collections import OrderedDict

from django.shortcuts import render

from .models import Skill


def skill_list(request):
    grouped = OrderedDict()
    for skill in Skill.objects.all():
        grouped.setdefault(skill.category, []).append(skill)

    label_lookup = dict(Skill.CATEGORY_CHOICES)
    grouped_skills = [
        {"key": key, "label": label_lookup[key], "skills": skills}
        for key, skills in grouped.items()
    ]
    return render(request, "skills/list.html", {"grouped_skills": grouped_skills})

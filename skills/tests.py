from django.test import TestCase

from skills.models import Skill


class SkillModelTest(TestCase):
    def test_str_returns_name(self):
        skill = Skill.objects.create(name="Python", category="lang", order=1)
        self.assertEqual(str(skill), "Python")

    def test_default_proficiency(self):
        skill = Skill.objects.create(name="Python", category="lang")
        self.assertEqual(skill.proficiency, 3)

    def test_ordering_by_category_then_order_then_name(self):
        Skill.objects.create(name="React", category="frontend", order=1)
        Skill.objects.create(name="Python", category="lang", order=2)
        Skill.objects.create(name="JavaScript", category="lang", order=1)
        names = list(Skill.objects.values_list("name", flat=True))
        self.assertEqual(names, ["React", "JavaScript", "Python"])


from django.urls import reverse


class SkillsUrlTest(TestCase):
    def test_list_url_resolves(self):
        self.assertEqual(reverse("skills:list"), "/skills/")

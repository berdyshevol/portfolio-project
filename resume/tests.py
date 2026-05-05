from datetime import date

from django.test import TestCase

from resume.models import Education, Experience


class ExperienceModelTest(TestCase):
    def test_str_returns_role_at_company(self):
        exp = Experience.objects.create(
            company="Acme",
            location="Remote",
            role="Engineer",
            start_date=date(2024, 1, 1),
            description="Did things.",
            bullets="- shipped",
            order=1,
        )
        self.assertEqual(str(exp), "Engineer at Acme")

    def test_is_current_when_end_date_null(self):
        exp = Experience.objects.create(
            company="Acme",
            location="Remote",
            role="Engineer",
            start_date=date(2024, 1, 1),
            end_date=None,
            description=".",
            bullets=".",
        )
        self.assertTrue(exp.is_current)

    def test_ordering_by_order_then_start_date_desc(self):
        a = Experience.objects.create(
            company="A", location=".", role="r", start_date=date(2020, 1, 1),
            description=".", bullets=".", order=1,
        )
        b = Experience.objects.create(
            company="B", location=".", role="r", start_date=date(2024, 1, 1),
            description=".", bullets=".", order=0,
        )
        self.assertEqual(list(Experience.objects.all()), [b, a])


class EducationModelTest(TestCase):
    def test_str_returns_degree_at_institution(self):
        edu = Education.objects.create(
            institution="Baylor",
            degree="MSIS",
            location="Waco, TX",
            start_date=date(2024, 8, 1),
            end_date=date(2026, 7, 1),
            order=0,
        )
        self.assertEqual(str(edu), "MSIS at Baylor")


from django.urls import reverse


class ResumeUrlTest(TestCase):
    def test_show_url_resolves(self):
        self.assertEqual(reverse("resume:show"), "/resume/")


class ResumeShowViewTest(TestCase):
    def test_returns_200_and_template(self):
        response = self.client.get(reverse("resume:show"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "resume/show.html")

    def test_context_contains_experiences_and_education(self):
        Experience.objects.create(
            company="A", location=".", role="Engineer",
            start_date=date(2024, 1, 1), description=".", bullets="-", order=0,
        )
        Education.objects.create(
            institution="Baylor", degree="MSIS",
            start_date=date(2024, 8, 1), end_date=date(2026, 7, 1), order=0,
        )
        response = self.client.get(reverse("resume:show"))
        self.assertEqual(len(response.context["experiences"]), 1)
        self.assertEqual(len(response.context["education"]), 1)


class InitialResumeFixtureTest(TestCase):
    fixtures = ["initial_resume.json"]

    def test_loads_two_experiences(self):
        self.assertEqual(Experience.objects.count(), 2)

    def test_loads_three_education_entries(self):
        self.assertEqual(Education.objects.count(), 3)

    def test_acuity_present_and_current(self):
        acuity = Experience.objects.get(company="Acuity PPM")
        self.assertTrue(acuity.is_current)

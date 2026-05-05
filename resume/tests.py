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

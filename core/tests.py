from django.test import TestCase

from core.models import ContactMessage


class ContactMessageModelTest(TestCase):
    def test_str_returns_subject_and_email(self):
        msg = ContactMessage.objects.create(
            name="Jane",
            email="jane@example.com",
            subject="Hello",
            body="Test body",
        )
        self.assertEqual(str(msg), "Hello — jane@example.com")

    def test_default_unread(self):
        msg = ContactMessage.objects.create(
            name="Jane",
            email="jane@example.com",
            subject="Hello",
            body="Test body",
        )
        self.assertFalse(msg.is_read)

    def test_ordering_newest_first(self):
        first = ContactMessage.objects.create(
            name="A", email="a@x.com", subject="1", body="."
        )
        second = ContactMessage.objects.create(
            name="B", email="b@x.com", subject="2", body="."
        )
        self.assertEqual(list(ContactMessage.objects.all()), [second, first])


from django.urls import reverse


class CoreUrlTest(TestCase):
    def test_home_url_resolves(self):
        self.assertEqual(reverse("core:home"), "/")

    def test_about_url_resolves(self):
        self.assertEqual(reverse("core:about"), "/about/")

    def test_contact_url_resolves(self):
        self.assertEqual(reverse("core:contact"), "/contact/")


from projects.models import Project


class HomeViewTest(TestCase):
    def test_home_returns_200(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)

    def test_home_uses_correct_template(self):
        response = self.client.get(reverse("core:home"))
        self.assertTemplateUsed(response, "core/home.html")

    def test_home_includes_featured_projects(self):
        Project.objects.create(
            title="A", slug="a", summary="s", business_problem=".",
            tools_used=".", key_features=".", role_contribution=".",
            biggest_challenge=".", what_learned=".", is_featured=True,
        )
        Project.objects.create(
            title="B", slug="b", summary="s", business_problem=".",
            tools_used=".", key_features=".", role_contribution=".",
            biggest_challenge=".", what_learned=".", is_featured=False,
        )
        response = self.client.get(reverse("core:home"))
        featured = list(response.context["featured_projects"])
        self.assertEqual([p.title for p in featured], ["A"])


class AboutViewTest(TestCase):
    def test_about_returns_200(self):
        response = self.client.get(reverse("core:about"))
        self.assertEqual(response.status_code, 200)

    def test_about_uses_correct_template(self):
        response = self.client.get(reverse("core:about"))
        self.assertTemplateUsed(response, "core/about.html")

from django.test import TestCase

from projects.models import Project


class ProjectModelTest(TestCase):
    def _make(self, **overrides):
        defaults = dict(
            title="Chatbot",
            slug="chatbot",
            summary="An AI chatbot.",
            business_problem="Users want fast answers.",
            tools_used="Python, OpenAI",
            key_features="- Streaming\n- Memory",
            role_contribution="Sole developer",
            biggest_challenge="Latency",
            what_learned="Prompt engineering",
            category="ai",
            order=1,
        )
        defaults.update(overrides)
        return Project.objects.create(**defaults)

    def test_str_returns_title(self):
        project = self._make()
        self.assertEqual(str(project), "Chatbot")

    def test_default_not_featured(self):
        self.assertFalse(self._make().is_featured)

    def test_ordering_by_order_then_title(self):
        b = self._make(title="B", slug="b", order=2)
        a = self._make(title="A", slug="a", order=1)
        c = self._make(title="C", slug="c", order=1)
        self.assertEqual(list(Project.objects.all()), [a, c, b])


from django.urls import reverse


class ProjectsUrlTest(TestCase):
    def test_list_url_resolves(self):
        self.assertEqual(reverse("projects:list"), "/projects/")

    def test_detail_url_resolves(self):
        url = reverse("projects:detail", args=["chatbot"])
        self.assertEqual(url, "/projects/chatbot/")


class ProjectsListViewTest(TestCase):
    def test_list_returns_200(self):
        response = self.client.get(reverse("projects:list"))
        self.assertEqual(response.status_code, 200)

    def test_list_uses_correct_template(self):
        response = self.client.get(reverse("projects:list"))
        self.assertTemplateUsed(response, "projects/list.html")

    def test_list_orders_projects(self):
        Project.objects.create(
            title="B", slug="b", summary="s", business_problem=".",
            tools_used=".", key_features=".", role_contribution=".",
            biggest_challenge=".", what_learned=".", order=2,
        )
        Project.objects.create(
            title="A", slug="a", summary="s", business_problem=".",
            tools_used=".", key_features=".", role_contribution=".",
            biggest_challenge=".", what_learned=".", order=1,
        )
        response = self.client.get(reverse("projects:list"))
        titles = [p.title for p in response.context["projects"]]
        self.assertEqual(titles, ["A", "B"])

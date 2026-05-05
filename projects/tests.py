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

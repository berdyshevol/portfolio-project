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

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("lang", "Programming Languages"),
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("testing", "Testing"),
        ("db", "Databases"),
        ("cloud", "Cloud"),
        ("tools", "Tools / Integrations"),
        ("practices", "Engineering Practices"),
    ]

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveSmallIntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]
        unique_together = [("name", "category")]

    def __str__(self):
        return self.name

from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    bullets = models.TextField(help_text="One achievement per line, prefix with - ")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.role} at {self.company}"

    @property
    def is_current(self):
        return self.end_date is None


class Education(models.Model):
    institution = models.CharField(max_length=120)
    degree = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-end_date"]

    def __str__(self):
        return f"{self.degree} at {self.institution}"

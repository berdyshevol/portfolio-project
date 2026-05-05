from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("ai", "AI / Agent"),
        ("ml", "Machine Learning"),
        ("media", "Media / Generative"),
        ("workflow", "Workflow / Automation"),
        ("web", "Web App"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=300)
    business_problem = models.TextField()
    tools_used = models.CharField(max_length=300)
    key_features = models.TextField(help_text="One bullet per line, prefix with - ")
    role_contribution = models.TextField()
    biggest_challenge = models.TextField()
    what_learned = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="ai")
    order = models.PositiveSmallIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("projects:detail", args=[self.slug])

    def tool_chips(self):
        return [t.strip() for t in self.tools_used.split(",") if t.strip()]

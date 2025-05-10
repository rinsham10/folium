from django.db import models
from django.utils.text import slugify
import uuid


class Portfolio(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    skills = models.TextField(blank=True)  # Comma-separated skills

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_id = uuid.uuid4().hex[:6]
            self.slug = f"{base_slug}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    project_duration = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    stack = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_desc = models.TextField(blank=True)
    duration = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Education(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    edu_desc = models.TextField(blank=True)
    edu_duration = models.CharField(max_length=100, blank=True)
    edu_location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.school}"

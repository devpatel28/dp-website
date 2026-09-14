from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=120, default="Dev Nareshkumar Patel")
    title = models.CharField(max_length=150, default="Junior Software Developer")
    headline = models.CharField(
        max_length=255,
        default="Computer Science student passionate about Python, full-stack web development, and IoT engineering."
    )
    bio = models.TextField(
        default=(
            "Aspiring Junior Software Developer currently pursuing a Bachelor of Computer Science "
            "at Trent University with a strong background in Electronics Engineering from Seneca College. "
            "Experienced in building Python and IoT automation solutions, deploying enterprise systems at Compugen, "
            "and developing responsive web applications with Django and React."
        )
    )
    phone = models.CharField(max_length=30, default="+1 (416) 721-0524")
    email = models.EmailField(default="dnhp281999@gmail.com")
    location = models.CharField(max_length=100, default="Ontario, Canada")
    linkedin_url = models.URLField(default="https://linkedin.com/in/dev-n-patel-2aug1999/")
    github_url = models.URLField(default="https://github.com/devpatel28")
    status_text = models.CharField(max_length=100, default="Available for Junior Software Developer Roles")

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('lang', 'Languages'),
        ('db', 'Databases'),
        ('devops', 'Tools & DevOps'),
        ('cert', 'Certifications'),
    ]

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lang')
    proficiency = models.PositiveSmallIntegerField(default=85, help_text="Proficiency percentage (e.g. 85)")
    icon_name = models.CharField(max_length=50, blank=True, help_text="Lucide or FontAwesome icon class/name")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=150)
    tagline = models.CharField(max_length=255, blank=True)
    technologies = models.CharField(max_length=255, help_text="Comma-separated tech stack, e.g. Python, Django, Docker")
    description = models.TextField()
    bullet_points = models.TextField(help_text="Bullet points separated by new lines")
    github_url = models.URLField(blank=True, default="https://github.com/devpatel28")
    live_demo_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

    def get_bullet_list(self):
        return [line.strip() for line in self.bullet_points.splitlines() if line.strip()]


class Experience(models.Model):
    role = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=120, default="GTA, Canada")
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    is_current = models.BooleanField(default=False)
    bullet_points = models.TextField(help_text="Bullet points separated by new lines")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.role} at {self.company}"

    def get_bullet_list(self):
        return [line.strip() for line in self.bullet_points.splitlines() if line.strip()]


class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    location = models.CharField(max_length=120, default="Ontario, Canada")
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    coursework = models.TextField(help_text="Comma-separated or bullet list of relevant coursework")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    def get_course_list(self):
        return [c.strip() for c in self.coursework.split(',') if c.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

from django.test import TestCase, Client
from django.urls import reverse
from resume.models import Profile, Skill, Project, Experience, Education, ContactMessage
from resume.forms import ContactForm


class ResumeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            full_name="Dev Nareshkumar Patel",
            title="Junior Software Developer",
            email="dnhp281999@gmail.com",
            phone="+1 (416) 721-0524",
            linkedin_url="https://linkedin.com/in/dev-n-patel-2aug1999/",
            github_url="https://github.com/devpatel28",
        )
        self.skill = Skill.objects.create(
            name="Python",
            category="lang",
            proficiency=95,
            order=1,
        )
        self.project = Project.objects.create(
            title="Motion Detector",
            technologies="Raspberry Pi, Python",
            description="Real-time IoT alert appliance",
            bullet_points="Processed PIR sensor interrupts\nConnected via LTE",
            github_url="https://github.com/devpatel28",
            order=1,
        )

    def test_resume_view_status_code(self):
        response = self.client.get(reverse('resume:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dev Nareshkumar Patel")
        self.assertContains(response, "Motion Detector")
        self.assertContains(response, "Python")

    def test_contact_form_submission(self):
        data = {
            'name': "Recruiter Jane",
            'email': "recruiter@techcompany.com",
            'subject': "Junior Developer Interview",
            'message': "Hi Dev, we loved your portfolio and would like to set up an interview.",
        }
        response = self.client.post(reverse('resume:home'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, "Recruiter Jane")
        self.assertEqual(msg.email, "recruiter@techcompany.com")

    def test_model_methods(self):
        tech_list = self.project.get_tech_list()
        self.assertEqual(tech_list, ["Raspberry Pi", "Python"])
        bullets = self.project.get_bullet_list()
        self.assertEqual(len(bullets), 2)

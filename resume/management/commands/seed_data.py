from django.core.management.base import BaseCommand
from resume.models import Profile, Skill, Project, Experience, Education


class Command(BaseCommand):
    help = "Seeds database with Dev Patel's exact resume data"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding Dev Patel's resume data..."))

        # Profile
        profile, _ = Profile.objects.update_or_create(
            id=1,
            defaults={
                'full_name': "Dev Patel",
                'title': "Junior Software Developer",
                'headline': "Computer Science student passionate about Python, full-stack web development, and IoT engineering.",
                'bio': (
                    "Aspiring Junior Software Developer pursuing a Bachelor of Computer Science at Trent University "
                    "with a technical foundation in Electronics Engineering from Seneca College. Proven hands-on experience "
                    "in software deployment, IoT automation, and real-time web applications using Python, Django, React, and Docker. "
                    "Driven by solving practical engineering problems and shipping clean, maintainable code."
                ),
                'phone': "+1 (416) 721-0524",
                'email': "dnhp281999@gmail.com",
                'location': "Ontario, Canada",
                'linkedin_url': "https://linkedin.com/in/dev-n-patel-2aug1999/",
                'github_url': "https://github.com/devpatel28",
                'status_text': "Open to Junior Software Developer & Co-op Roles",
            }
        )
        self.stdout.write(self.style.SUCCESS(f"Profile updated: {profile.full_name}"))

        # Education
        Education.objects.all().delete()
        educations = [
            {
                'institution': "Trent University",
                'degree': "Bachelor of Computer Science",
                'location': "Ontario, Canada",
                'start_date': "Sep 2023",
                'end_date': "Aug 2026",
                'coursework': "Applied AI & Machine Learning, LLM & Natural Language Processing, Data Mining, Data Structures & Algorithms, Software Design & Modelling, Systems Programming, Database Management Systems",
                'order': 1,
            },
            {
                'institution': "Seneca College",
                'degree': "Electronics Engineering Technician",
                'location': "Ontario, Canada",
                'start_date': "Jan 2018",
                'end_date': "Aug 2020",
                'coursework': "Programming Using C, Micro-controller Concepts, Computer Networks",
                'order': 2,
            },
        ]
        for edu_data in educations:
            Education.objects.create(**edu_data)
        self.stdout.write(self.style.SUCCESS("Education entries seeded."))

        # Skills
        Skill.objects.all().delete()
        skills = [
            # Web Development
            ('HTML5 & CSS3', 'web', 95, 1),
            ('JavaScript (ES6+)', 'web', 90, 2),
            ('React.js', 'web', 85, 3),
            ('Django', 'web', 88, 4),
            ('Node.js', 'web', 80, 5),

            # Languages
            ('Python', 'lang', 95, 1),
            ('C', 'lang', 85, 2),
            ('C++', 'lang', 80, 3),
            ('Java', 'lang', 80, 4),
            ('SQL', 'lang', 85, 5),

            # Databases
            ('PostgreSQL', 'db', 88, 1),
            ('MySQL', 'db', 85, 2),
            ('SQLite', 'db', 90, 3),

            # Tools & DevOps
            ('Git & GitHub', 'devops', 92, 1),
            ('Docker', 'devops', 85, 2),
            ('Google Colab', 'devops', 88, 3),
            ('Linux / Bash', 'devops', 82, 4),
            ('VS Code', 'devops', 95, 5),

            # Certifications
            ('Complete Python Mastery (Code With Mosh)', 'cert', 100, 1),
            ('Intro to Generative AI', 'cert', 100, 2),
        ]
        for name, category, proficiency, order in skills:
            Skill.objects.create(
                name=name,
                category=category,
                proficiency=proficiency,
                order=order,
            )
        self.stdout.write(self.style.SUCCESS("Skills seeded."))

        # Projects
        Project.objects.all().delete()
        projects = [
            {
                'title': "Motion Detector",
                'tagline': "Real-time IoT alert appliance using Raspberry Pi and LTE telemetry",
                'technologies': "Raspberry Pi, Python, PIR sensor, SMTP, TRM240 LTE",
                'description': "An embedded IoT security application that detects movement in real time and automatically dispatches alert notifications over cellular network without relying on local Wi-Fi.",
                'bullet_points': (
                    "Developed a Python-based event listener to process PIR sensor interrupts and integrated SMTP libraries for automated alert dispatching within 5 minutes of detection.\n"
                    "Connected the Raspberry Pi to the internet using a TRM240 LTE modem to establish an independent network connection, ensuring continuous real-time environment monitoring."
                ),
                'github_url': "https://github.com/devpatel28",
                'live_demo_url': "",
                'is_featured': True,
                'order': 1,
            },
            {
                'title': "Temperature-Controlled Home Automation",
                'tagline': "Full-stack smart climate control with real-time multi-user WebSocket sync",
                'technologies': "Arduino, React.js, Node.js, WebSockets, Digital Thermometer",
                'description': "A smart home automation prototype featuring an Arduino hardware controller and a responsive mobile web interface with synchronized real-time sensor streaming.",
                'bullet_points': (
                    "Architected an Arduino-based system with a React.js/Node.js mobile interface, implementing a real-time data pipeline to synchronize temperature states across multiple concurrent users via WebSocket.\n"
                    "Engineered automated control logic to process ambient data from a digital thermometer, bypassing manual inputs to maintain precise climate conditions."
                ),
                'github_url': "https://github.com/devpatel28",
                'live_demo_url': "",
                'is_featured': True,
                'order': 2,
            },
            {
                'title': "Developer Resume & Portfolio Web Platform",
                'tagline': "Dynamic, containerized full-stack web application built with Django & Docker",
                'technologies': "Python, Django, Docker, PostgreSQL/SQLite, HTML5, CSS3, JavaScript",
                'description': "A professional developer portfolio and interactive resume platform engineered with Django MVC architecture, featuring database-driven content management, contact processing, and Docker containerization.",
                'bullet_points': (
                    "Engineered relational database models for skills, projects, and work history, manageable directly through an authenticated Django Admin panel.\n"
                    "Designed a responsive, modern frontend featuring dark/light theme persistence, recruiter-friendly print/PDF export, and CSRF-protected contact forms.\n"
                    "Containerized the application with Docker and Docker Compose for production-grade reliability and reproducible developer setup."
                ),
                'github_url': "https://github.com/devpatel28",
                'live_demo_url': "",
                'is_featured': True,
                'order': 3,
            },
        ]
        for proj in projects:
            Project.objects.create(**proj)
        self.stdout.write(self.style.SUCCESS("Projects seeded."))

        # Experience
        Experience.objects.all().delete()
        experiences = [
            {
                'role': "Deployment Tech",
                'company': "Compugen",
                'location': "GTA, Canada",
                'start_date': "Jan 2024",
                'end_date': "Current",
                'is_current': True,
                'bullet_points': (
                    "Automated the configuration of 45 to 50 client laptops using deployment scripts and executed the on-site setup for Hamilton Health Sciences, resulting in seamless hardware transitions across departments.\n"
                    "Installed 12 complete Point of Sale (POS) and payment systems daily for The Beer Store, integrating all necessary hardware to ensure retail locations were immediately operational.\n"
                    "Resolved 5 critical hardware/software issues for Canadian Bank Note by diagnosing network protocol and registry conflicts, ensuring zero downtime for secure printing operations."
                ),
                'order': 1,
            },
            {
                'role': "Smart-Home Security Technician",
                'company': "Telus",
                'location': "GTA, Canada",
                'start_date': "Jan 2023",
                'end_date': "May 2023",
                'is_current': False,
                'bullet_points': (
                    "Diagnosed and resolved complex hardware and software failures for smart-home security systems within 30-45 minute windows, leveraging systematic troubleshooting procedures to isolate network vulnerabilities.\n"
                    "Debugged device connectivity issues across 1 to 3 residential properties daily, ensuring reliable system integration and sustained operational readiness for end-users."
                ),
                'order': 2,
            },
        ]
        for exp in experiences:
            Experience.objects.create(**exp)
        self.stdout.write(self.style.SUCCESS("Experience seeded."))

        self.stdout.write(self.style.SUCCESS("Successfully populated all of Dev Patel's resume data!"))


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Education, ContactMessage
from .forms import ContactForm


def resume_view(request):
    # Fetch or initialize default profile
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Dev Patel")
    elif profile.full_name != "Dev Patel":
        profile.full_name = "Dev Patel"
        profile.save()

    # Fetch categorized skills
    skills_web = Skill.objects.filter(category='web')
    skills_lang = Skill.objects.filter(category='lang')
    skills_db = Skill.objects.filter(category='db')
    skills_devops = Skill.objects.filter(category='devops')
    skills_cert = Skill.objects.filter(category='cert')

    # Fetch other sections
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            
            # Send email notification to Dev Patel if mail settings are configured
            try:
                from django.core.mail import send_mail
                subject = f"[Portfolio Contact] {contact_msg.subject} from {contact_msg.name}"
                body = (
                    f"New message received on your portfolio website:\n\n"
                    f"Name: {contact_msg.name}\n"
                    f"Email: {contact_msg.email}\n"
                    f"Subject: {contact_msg.subject}\n\n"
                    f"Message:\n{contact_msg.message}\n"
                )
                send_mail(
                    subject,
                    body,
                    None,
                    [profile.email],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(
                request,
                f"Thank you, {contact_msg.name}! Your message has been sent to Dev Patel ({profile.email}). Dev will respond shortly."
            )
            return redirect('/#contact')
        else:
            messages.error(request, "Please correct the errors in the contact form below.")

    context = {
        'profile': profile,
        'skills_web': skills_web,
        'skills_lang': skills_lang,
        'skills_db': skills_db,
        'skills_devops': skills_devops,
        'skills_cert': skills_cert,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
        'form': form,
    }

    return render(request, 'resume/index.html', context)


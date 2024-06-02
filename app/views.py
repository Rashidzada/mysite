from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
def index(request):
    user_profile = UserProfile.objects.first()  # Fetch the first UserProfile
    skills = Skill.objects.all()
    education_list = Education.objects.all()
    professional_experience_list = ProfessionalExperience.objects.all()
    resume = Resume.objects.first()  # Fetch the first Resume
    projects = Project.objects.all()
    services = Service.objects.all()
    social_media_links = SocialMedia.objects.all()
    google_maps_url = GoogleMapsURL.objects.first()
    
    context = {
        'user_profile': user_profile,
        'skills': skills,
        'education_list': education_list,
        'professional_experience_list': professional_experience_list,
        'resume': resume,
        'projects': projects,
        'services': services,
        'social_media_links': social_media_links,
        'google_maps_url': google_maps_url
    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('index')
    return render(request, 'index.html', context)

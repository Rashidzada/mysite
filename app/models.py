from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=100, blank=True, choices=(('male', 'Male'), ('female', 'Female')), default='Male')
    address = models.CharField(max_length=255, blank=True)  # Increased length for potentially longer addresses
    picture = models.ImageField(upload_to='profile_images/', blank=True)
    skills = models.ManyToManyField('Skill')  # Renamed for consistency
    education = models.ManyToManyField('Education')
    professional_experience = models.ManyToManyField('ProfessionalExperience')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15,blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'


class Skill(models.Model):
    skill_name = models.CharField(max_length=200, unique=True)
    years_of_experience = models.FloatField(blank=True, default=0.0)  # Improved data type for experience
    proficiency_level = models.CharField(max_length=50, blank=True, choices=(
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')
    ))  # Added proficiency level for clearer representation

    def __str__(self):
        return self.skill_name


class Education(models.Model):
    degree_name = models.CharField(max_length=255, unique=True)  # Increased length for potentially longer degree names
    started_at = models.DateField()
    ended_at = models.DateField(null=True, blank=True)
    institute = models.CharField(max_length=255)
    grade = models.CharField(max_length=1, blank=True, default='A')
    division = models.CharField(max_length=20, blank=True, default='First', choices=(
        ('first', 'First'),
        ('second', 'Second'),
        ('third', 'Third')
    ))

    def __str__(self):
        return self.degree_name


class ProfessionalExperience(models.Model):
    company_name = models.CharField(max_length=200)  # Added company name field
    job_title = models.CharField(max_length=200)  # Added job title field
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.company_name} - {self.job_title}'


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.FileField(blank=True, upload_to='resume_files/')

    def __str__(self):
        return f'{self.user.username} Resume'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"



class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_link = models.URLField()

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    whatsapp_number = models.CharField(max_length=20,default='+923470983567')

    def __str__(self):
        return self.title



class SocialMedia(models.Model):
    platform_choices = [
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
        ('WhatsApp', 'WhatsApp'),
        ('YouTube', 'YouTube'),
        ('Pinterest', 'Pinterest'),
        ('TikTok', 'TikTok'),
        ('Snapchat', 'Snapchat'),
        ('GitHub', 'GitHub'),
        # Add more platforms as needed
    ]
    platform = models.CharField(max_length=20, choices=platform_choices)
    link = models.URLField()

    def __str__(self):
        return f"{self.platform} - {self.link}"


class GoogleMapsURL(models.Model):
    location_name = models.CharField(max_length=233,blank=True)
    url = models.URLField()

    def __str__(self):
        return self.location_name

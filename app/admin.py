from django.contrib import admin
from .models import *
from django.core.mail import send_mail
from mysite import settings
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'get_skills', 'get_education', 'get_experience')
    readonly_fields = ('get_skills', 'get_education', 'get_experience')

    def get_skills(self, obj):
        return ", ".join([str(skill) for skill in obj.skills.all()])
    get_skills.short_description = 'Skills'

    def get_education(self, obj):
        return ", ".join([str(edu) for edu in obj.education.all()])
    get_education.short_description = 'Education'

    def get_experience(self, obj):
        return ", ".join([str(exp) for exp in obj.professional_experience.all()])
    get_experience.short_description = 'Professional Experience'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'years_of_experience', 'proficiency_level')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_name', 'started_at', 'ended_at', 'institute', 'grade', 'division')

@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title', 'start_date', 'end_date')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass  # No additional fields for now


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'responded', 'response')
    list_filter = ('responded',)
    search_fields = ('email', 'subject')
    actions = ['mark_as_responded']

    def mark_as_responded(self, request, queryset):
        queryset.update(responded=True)
    mark_as_responded.short_description = "Mark selected messages as responded"

    def save_model(self, request, obj, form, change):
        if 'response' in form.changed_data:
            # Here you can integrate the logic to send an email to the user
            subject = f"Response to your message: {obj.subject}"
            message = f"Dear {obj.name},\n\nWe have responded to your message From  Go-Green:\n\n{obj.response}"
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [obj.email]
            
            # Send email
            send_mail(subject, message, email_from, recipient_list)
        super().save_model(request, obj, form, change)





admin.site.register(Project)

admin.site.register(Service)
admin.site.register(SocialMedia)
admin.site.register(GoogleMapsURL)
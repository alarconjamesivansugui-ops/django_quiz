from django.shortcuts import render
from .models import PersonalInformation, Project

def project_list_view(request):
    personal_info = PersonalInformation.objects.first()
    projects = Project.objects.all()

    context = {
        'personal_info': personal_info,
        'projects': projects
    }

    return render(request, 'portfolio/project_list.html', context)
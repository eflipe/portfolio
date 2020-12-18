from django.shortcuts import render
from projects.models import ProjectModel


def project_index(request):
    projects = ProjectModel.objects.all().order_by('-created_on')
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = ProjectModel.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

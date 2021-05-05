from django.shortcuts import render
from projects.models import ProjectModel
from django.core.mail import send_mail


def project_index(request):
    if request.method == "GET":
        subject = "Te visitaron"
        message = f"META: \nHEADERS: {request.headers} \nHOST: {request.get_host()}\n\n"
        send_mail(subject, message, 'heyheymycode@gmail.com',
                  ['heyheymycode@gmail.com'])

    projects = ProjectModel.objects.all().order_by('-id')
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

from django.contrib import admin
from projects.models import ProjectModel


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectModel, ProjectAdmin)

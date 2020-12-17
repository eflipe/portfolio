from django.db import models


class ProjectModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    techno = models.CharField(blank=True, max_length=100)
    # image = models.FilePathField(path="/img")  # , height_field=, width_field=
    repo = models.URLField(blank=True)
    sitio_web = models.URLField(blank=True)

    def __str__(self):
        return self.title

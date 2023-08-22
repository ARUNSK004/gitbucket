from django.db import models

# Create your models here.
class RepositoriesData(models.Model):
    repositories_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    update_text = models.DateTimeField(auto_now_add=True)
class ProjectData(models.Model):
    project_text = models.CharField(max_length=200)
    key_text = models.CharField(max_length=200)
    descriptions_text = models.CharField(max_length=200)


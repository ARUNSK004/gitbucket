from django.shortcuts import render, redirect
from .models import *
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def gitbucket(request):
    template = loader.get_template('gitbucket.html')
    return HttpResponse(template.render())

def repositories_page(request):
    input_data = RepositoriesData.objects.all()
    return render(request, 'repositories.html', {'input_data': input_data})
def project_page(request):
    input_data =ProjectData.objects.all()
    return render(request, 'projects.html', {'input_data': input_data})
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def addproject(request):
    x = request.POST.get('projectname','')
    y = request.POST.get('key','')
    z = request.POST.get('description','')
    member=ProjectData(project_text=x,key_text =y,descriptions_text=z)
    member.save()
    return HttpResponseRedirect(reverse('project'))
def addrepositories(request):
    x = request.POST.get('repositories','')
    y = request.POST.get('description','')
    member=RepositoriesData(repositories_text=x,description_text=y)
    member.save()
    return HttpResponseRedirect(reverse('repositories'))
def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())
def createproject(request):
    template = loader.get_template('createproject.html')
    return HttpResponse(template.render({},request))
def createrepositories(request):
    template = loader.get_template('createrepositories.html')
    return HttpResponse(template.render({},request))

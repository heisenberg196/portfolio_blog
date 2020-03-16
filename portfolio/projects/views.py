from django.shortcuts import render
from .models import Project

def index(request):
    all_projects = Project.objects.all()
    context = {
        'projects' : all_projects
    }
    return render(request, "project_index.html", context)

def detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project' : project
    }
    return render(request, "project_detail.html", context)

from pickle import FALSE
from django.shortcuts import render, redirect
from .models import Project, Tag
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects

# Create your views here.

def projects(request):
    if request.method == "GET":
        projects, search_query = searchProjects(request)
        context = {'projects':projects, 'search_query':search_query}
    else:
        projects = Project.objects.all()
        context = {'projects': projects}
        
    return render(request, 'projects/projects_list.html', context)


# class ProjectListView(ListView):
#     model = Project
#     template_name = "projects/projects_list.html"




# def project(request, pk):
#     projectObj = Project.objects.get(id=pk)
#     return render(request, 'projects/single-project.html', {'project' : projectObj})


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/single_project.html"


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_create.html', context)


# class ProjectCreateView(LoginRequiredMixin, CreateView):
#     form_class = ProjectForm
#     model = Project
#     template_name = "projects/project_create.html"
#     success_url = reverse_lazy("list_projects")


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_update.html', context)


# class ProjectUpdateView(LoginRequiredMixin, UpdateView):
#     form_class = ProjectForm
#     model = Project
#     template_name = "projects/project_update.html"
#     success_url = reverse_lazy('list_projects')


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'project': project}
    return render(request, 'users/delete_template.html', context)


# class ProjectDeleteView(LoginRequiredMixin, DeleteView):
#     model = Project
#     template_name = "projects/delete_template.html"
#     success_url = reverse_lazy('list_projects')
from django.urls import path
from . import views
from .views import (    
    projects,
    ProjectDetailView,
    createProject, 
    deleteProject,
    updateProject,
    # ProjectCreateView,
    # ProjectUpdateView,
    # ProjectDeleteView,
    # ProjectListView,
)

urlpatterns = [
    path('', views.projects, name="list_projects"),
    path('project/<str:pk>/', ProjectDetailView.as_view(), name='project'),
    path('create-project/', views.createProject, name='create_project'),
    path('update-project/<str:pk>/', views.updateProject, name='update_project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete_project'),
]
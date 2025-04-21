from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('project/', views.project, name='project'),
    path('task/', views.task, name='task'),

    path('employee/<int:id>/', views.delete_employee, name='employee_delete'),
    path('project/<int:id>/', views.delete_project, name='project_delete'),
    path('task/<int:id>/', views.delete_task, name='task_delete'),

    path('employee/edit/<int:id>/', views.update_employee, name='employee_edit'),
    path('project/edit/<int:id>/', views.update_project, name='project_edit'),
    path('task/edit/<int:id>/', views.update_task, name='task_edit'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('delete/<int:pk>', views.delete, name='delete_employee'),
    path('department/<int:pk>/<slug:slug>', views.department_details, name='department_details'),
    path('forms/', views.forms_demo, name='forms_demo')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('delete/<int:pk>', views.delete, name='delete_employee'),
    path('department/<int:pk>/<slug:slug>', views.department_details, name='department_details'),
    path('forms_register/', views.forms_register, name='forms_register'),
    path('forms_login/', views.forms_login, name='forms_login'),
    path('model_forms/', views.model_forms, name='model_forms'),
]
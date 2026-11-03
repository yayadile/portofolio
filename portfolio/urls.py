from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lang/<str:code>/', views.set_lang, name='set_lang'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
]

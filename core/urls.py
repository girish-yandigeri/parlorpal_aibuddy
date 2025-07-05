# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('ai/', views.ai_suggestions_view, name='ai_suggestions'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('logout/', views.logout_view, name='logout'),
    path('ai-suggestions/', views.ai_suggestions_view, name='ai_suggestions'),
    path('generate-poster/', views.generate_poster_view, name='generate_poster'),

]

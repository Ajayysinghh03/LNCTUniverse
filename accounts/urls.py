from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('profile/', views.student_profile, name='student_profile'),
     path('dashboard/', views.dashboard, name='student_dashboard'),
]

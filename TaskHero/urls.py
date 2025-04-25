from django.urls import path
from . import views

app_name = 'TaskHero'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
]

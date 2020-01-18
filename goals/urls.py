from django.urls import path
from . import views

urlpatterns = [
    path('', views.allgoals, name='allgoals'),
    path('<int:goal_id>/', views.detail, name='goal_detail'),
]
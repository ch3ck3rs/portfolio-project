from django.urls import path
from . import views

urlpatterns = [
    path('sup', views.sup_home, name='sup_home'),
    # path('<int:blog_id>/', views.detail, name='blog_detail'),
]
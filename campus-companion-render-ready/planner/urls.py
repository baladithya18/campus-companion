from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<str:model>/add/', views.add_item, name='add_item'),
    path('assignment/<int:pk>/toggle/', views.toggle_assignment, name='toggle_assignment'),
    path('<str:model>/<int:pk>/delete/', views.delete_item, name='delete_item'),
]

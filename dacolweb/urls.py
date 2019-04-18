from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_general, name='dataset_general'),
	path('dataset/<str:uuid>/', views.dataset_detail, name='dataset_detail'),
]
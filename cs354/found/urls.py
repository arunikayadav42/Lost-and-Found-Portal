from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('<int:pk>/delete/', FoundDeleteView.as_view(), name="found_delete"),
    path('<int:pk>/edit/', FoundUpdateView.as_view(), name="found_edit"),
    path('create/', FoundCreateView.as_view(), name="found_create"),
    path('<int:pk>/', views.FoundDetail, name="found_detail"),
    path('', FoundListView.as_view(), name="found_list"),
] 
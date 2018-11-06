from django.urls import path
from .views import FoundListView, FoundCreateView, FoundDeleteView, \
                    FoundDetailView, FoundUpdateView
from . import views

urlpatterns = [
    path('<int:pk>/delete/', FoundDeleteView.as_view(), name="found_delete"),
    path('<int:pk>/edit/', FoundUpdateView.as_view(), name="found_edit"),
    path('<int:pk>/comment/', views.add_comment_to_found, 
         name="add_comment_to_found"),
    path('create/', FoundCreateView.as_view(), name="found_create"),
    path('<int:pk>/', FoundDetailView.as_view(), name="found_detail"),
    path('', FoundListView.as_view(), name="found_list"),
]
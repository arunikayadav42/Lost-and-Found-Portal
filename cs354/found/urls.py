from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('<int:pk>/delete/', FoundDeleteView.as_view(), name="found_delete"),
    path('<int:pk>/edit/', FoundUpdateView.as_view(), name="found_edit"),
    path('create/', FoundCreateView.as_view(), name="found_create"),
    path('<int:pk>/', views.FoundDetail, name="found_detail"),
    path('', FoundListView.as_view(), name="found_list"),
    path('<int:pk>/item_claim', views.claim_the_item, name="item_claimed"),
    path('<int:pk>/claim_approved', views.claim_approved, name="claim_approved"),
    path('<int:pk>/suggested_items', views.Suggested_Items, name="found_item_suggestions"),
] 
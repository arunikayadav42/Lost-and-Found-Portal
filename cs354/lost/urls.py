from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('<int:pk>/delete/', LostDeleteView.as_view(), name="lost_delete"),
    path('<int:pk>/edit/', LostUpdateView.as_view(), name="lost_edit"),
    path('create/', LostCreateView.as_view(), name="lost_create"),
    path('<int:pk>/', views.LostDetail, name="lost_detail"),
    path('', LostListView.as_view(), name="lost_list"),
    path('<int:pk>/item_found', views.item_found, name="item_found"),
    path('<int:pk>/suggested_items', views.Suggested_Items, name="lost_item_suggestions"),
    path('<int:pk>/confirm_item_received', views.item_claimed, name="lost_item_received"),
] 
from django.urls import path
from .views import LostListView, LostCreateView, LostDeleteView, \
                    LostDetailView, LostUpdateView
from . import views

urlpatterns = [
    path('<int:pk>/delete/', LostDeleteView.as_view(), name="lost_delete"),
    path('<int:pk>/edit/', LostUpdateView.as_view(), name="lost_edit"),
    path('<int:pk>/comment/', views.add_comment_to_lost, 
         name="add_comment_to_lost"),
    path('create/', LostCreateView.as_view(), name="lost_create"),
    path('<int:pk>/', LostDetailView.as_view(), name="lost_detail"),
    path('', LostListView.as_view(), name="lost_list"),
]
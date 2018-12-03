from django.urls import path

from .views import SignUpView, UserProfile, UserDetailView
from . import views

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('login/profile/', UserProfile.as_view(), name='userprofile'),
	path('login/profile/edit/', views.edit_profile, name='editprofile'),
	path('<slug:slug>/', UserDetailView.as_view(), name="profile_detail"),
]	
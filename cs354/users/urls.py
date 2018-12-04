from django.urls import path
from .views import SignUpView, UserProfile, ProfileUpdateView, UserDetailView
from . import views

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('login/profile/', UserProfile.as_view(), name='userprofile'),
	path('login/profile/edit/', ProfileUpdateView.as_view(), name='editprofile'),
	path('profile/<slug:slug>/', UserDetailView.as_view(), name="profile_detail"),
	
]	
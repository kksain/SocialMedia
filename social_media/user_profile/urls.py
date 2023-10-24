from django.urls import path, include
from user_profile.views import UserProfileView, SignUpView  # Import SignUpView

urlpatterns = [
    path('profile/', UserProfileView.as_view()),  
    path('signup/', SignUpView.as_view())
]

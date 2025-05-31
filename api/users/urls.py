from django.urls import path
from .views import UserInfoView, UserRegistrationView

# URL's are going to start with api/users

urlpatterns = [
    path('user-info/',UserInfoView.as_view(), name='user-info'),
    path('register/', UserRegistrationView.as_view(), name='register-user')
]

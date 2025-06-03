from django.urls import path
from .views import UserInfoView, UserRegistrationView, LoginView, LogoutView

# URL's are going to start with api/users

urlpatterns = [
    path('user-info/',UserInfoView.as_view(), name='user-info'),
    path('register/', UserRegistrationView.as_view(), name='register-user'),
    path('login/',LoginView.as_view(), name='login-user'),
    path('logout/',LogoutView.as_view(), name='logout-user')
]

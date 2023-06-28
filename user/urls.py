from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import UserCreateView, UserGetView, UserPostsAPIView


urlpatterns = [
    path('get_user/<int:pk>/', UserGetView.as_view(), name='get-user'),
    path('get_user/<int:pk>/posts/', UserPostsAPIView.as_view(), name='get-user-post'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from users.views import (UserListView,
                         UserDetailView,
                         UserDeleteView,
                         UserUpdateView,
                         UserCreateView)

urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

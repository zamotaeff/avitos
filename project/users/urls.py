from django.urls import path

from users.views import (UserListView,
                         UserDetailView,
                         UserDeleteView,
                         UserUpdateView,
                         UserCreateAPIView)

urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateAPIView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view())
]

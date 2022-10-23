from django.urls import path

from users.views import (UserListView,
                         UserDetailView,
                         UserCreateView,
                         UserDeleteView,
                         UserUpdateView)

urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view())
]

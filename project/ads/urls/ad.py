from django.urls import path

from ads.views.ad import (
    AdUploadImageView
)

urlpatterns = [
    path('<int:pk>/upload_image/', AdUploadImageView.as_view())
]

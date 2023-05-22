from django.urls import path
from .views import UploadedFileViewSet

urlpatterns = [
    path('uploaded-files/', UploadedFileViewSet.as_view({'post': 'create'}), name='uploadedfile-list'),
]

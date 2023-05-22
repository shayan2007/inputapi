from django.urls import include, path
from rest_framework import routers
from file_upload_api.myapp.views import UploadedFileViewSet

router = routers.DefaultRouter()
router.register('uploaded-files', UploadedFileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

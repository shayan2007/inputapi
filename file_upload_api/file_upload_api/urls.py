from django.urls import include, path
from rest_framework import routers
from myapp.views import UploadedFileViewSet

router = routers.DefaultRouter()
router.register('uploaded-files', UploadedFileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

from django.urls import path
from .views import FileUploadView, DownloadPDFView # Add DownloadPDFView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('download-pdf/', DownloadPDFView.as_view(), name='download-pdf'), # Add this
]
from django.urls import path

from .views import excel_upload

urlpatterns = [
    path('upload/', excel_upload, name='upload'),
]

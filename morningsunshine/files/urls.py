from django.urls import path

from . import views

app_name = "files"
urlpatterns = [
    path("", views.index, name="files"),
    path("upload/", views.upload, name="upload"),
    path("upload/upload-success/", views.upload, name="upload_success"),
]
from django.contrib import admin
from django.urls import path
from transcoder import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('upload', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),
    path('videos/<int:pk>/', views.view_video, name='view_video'),
]
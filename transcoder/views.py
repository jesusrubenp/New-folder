from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VideoUploadForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video uploaded successfully!')
            return redirect('video_list')  # Cambia 'video_list' por el nombre de la vista que muestra la lista de videos
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def view_video(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'view_video.html', {'video': video})

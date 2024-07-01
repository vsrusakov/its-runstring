from django.shortcuts import render
from django.http import FileResponse
from video_maker.maker import get_bvideo
from .models import Video
import os

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')

def send_video(request):

    text = request.GET.get('text', 'Hello, World!')
    fps = int(request.GET.get('fps', 24))
    name = request.GET.get('name', 'my_video')
    path_to_save = os.path.join('.', 'video_maker', 'videos')

    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        user_ip = xff.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    Video(user_ip=user_ip, text=text, fps=fps).save()

    video = get_bvideo(text, fps, path_to_save, name)

    return FileResponse(video, content_type='video/mp4', as_attachment=True)

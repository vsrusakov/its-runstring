from django.shortcuts import render
from django.http import FileResponse
from video_maker.maker import get_bvideo

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')

def send_video(request):

    text = request.GET.get('text', 'Hello, World!')
    fps = int(request.GET.get('fps', 24))
    name = request.GET.get('name', 'my_video')
    path_to_save = './video_maker/videos'

    video = get_bvideo(text, fps, path_to_save, name)
    return FileResponse(video, content_type='video/mp4', as_attachment=True)

import cv2
import numpy as np
import os


def get_bvideo(text, fps, path_to_save, name):
    video_path = os.path.join(path_to_save, name + ".mp4")
    font_face = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 10.0
    thickness = 14
    fourcc = cv2.VideoWriter.fourcc('m', 'p', '4', 'v')

    # определяем размеры и цвет фонового изображения (background image)
    (width, higth), _ = cv2.getTextSize(text, font_face, font_scale, thickness)
    bg_w, bg_h = higth + width, 2 * higth
    bg_img = np.zeros((bg_h, bg_w, 3), np.uint8)
    bg_img[:,:,0] = 153 # blue channel 
    bg_img[:,:,2] = 153 # red channel 

    # накладываем текст на фоновое изображение и приводим к нужному размеру
    org = (int(higth / 2), int(3 * higth / 2))
    img_w_text = cv2.putText(bg_img, text, org, font_face, font_scale, (255, 255, 255), thickness)
    target_img = cv2.resize(img_w_text, (max(100, int(100 * bg_w / bg_h)), 100))

    # создаем VideoWriter и записываем кадры
    num_frames = fps * 3
    step = max(0, (int(100 * bg_w / bg_h) - 100) / num_frames)
    video = cv2.VideoWriter(video_path, fourcc, fps, (100, 100))

    for i in range(num_frames):
        window_start = round(step * i)
        frame = target_img[:,window_start:window_start + 100]
        video.write(frame)

    video.release()

    return open(video_path, "rb")

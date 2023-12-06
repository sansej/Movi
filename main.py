from audio import AudioEditor
from subtitle import SubtitleEditor, len_simbols
from video import VideoEditor, AudioFileClip
from image import ImageEditor
from youtube import post_shorts
import os 
from moviepy.editor import VideoFileClip
# import pyttsx3
from pydub import AudioSegment
import fnmatch
import wave
import numpy as np
import time
from PIL import Image
import cv2
key = 'MVsaiNhymA81LvKqS9oezJeEpyZ2pYDtq9zFFQvnuWPwCMPmhiOLaI88'

CLIP_NAME = 'Lava'

def create_shorts_ru():
        count = 1
        text=''
        folder_image = f'image\\{CLIP_NAME}'
        folter_image_crop = f'image_crop\\{CLIP_NAME}'
        folter_image_resize = f'image_resize\\{CLIP_NAME}'
        folder_video = f'video\\{CLIP_NAME}'
        folder_final = f'final\\{CLIP_NAME}'
        voice = f'audio\\sound_{CLIP_NAME}.mp3'
        audio_file = f'audio\\voice_{CLIP_NAME}_ru.mp3'
        video_sound = f'video\\{CLIP_NAME}\\video_sound_{CLIP_NAME}.mp4'
        image_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png','10.png','11.png','12.png','13.png','14.png']

        try:
            with open(f'text\\{CLIP_NAME}_ru.txt', 'r', encoding='UTF-8') as file:
                text = file.read()
                file.close()
        except:
            exit('Error: Reading error')

        # try:
        #     if os.path.exists(audio_file):
        #         print(f"File {audio_file} exists.")
        #     else:
        #         AudioEditor.create_voice(text=text,output_file=audio_file)
        # except:
        #     exit('Error: Failed to create sound')
        # ----------------------------------------------------------------------------------------
        # try:
        #     AudioEditor.change_speed(input_path=voice, output_path=audio_file, speed=1.08)
        # except:
        #     exit('Error: Failed to create final audio')
        # ---------------------------------------------------------------------------------------------
        if not os.path.exists(folter_image_crop):
            os.makedirs(folter_image_crop)
            print(f"Folder {folter_image_crop} created")
        else:
            print(f"Folder {folter_image_crop} already exists")

        if not os.path.exists(folter_image_resize):
            os.makedirs(folter_image_resize)
            print(f"Folder {folter_image_resize} created")
        else:
            print(f"Folder {folter_image_resize} already exists")

        try:
            for file in os.listdir(folder_image):
                if any(fnmatch.fnmatch(file, img) for img in image_list):
                    try:
                        file_name = file.split('.')
                        ImageEditor.resize(input_path=f'{folder_image}\\{file}', output_path=f'{folter_image_resize}\\{file_name[0]}.{file_name[1]}')
                        print(f'{file} resize')
                        ImageEditor.crop_image(input_path=f'{folter_image_resize}\\{file_name[0]}.{file_name[1]}', output_path=f'{folter_image_crop}\\{file_name[0]}.{file_name[1]}')
                        print(f'{file} crop')
                    except FileNotFoundError:
                        print(f'{file} not found')
                    except FileExistsError:
                        print(f'{file_name[0]}.{file_name[1]} already exists')
                    except Exception as e:
                        print(f'Error: {e}')
        except:
            exit('Error: Failed to crop image')

        if not os.path.exists(folder_video):
            os.makedirs(folder_video)
            print(f"Folder {folder_video} created")
        else:
            print(f"Folder {folder_video} already exists")

        try:
            count = 1
            for file in os.listdir(folter_image_crop):
                if file.endswith(f".jpg"):
                    file_name = file.split('.')
                    if count%3!=0:
                        rev = False
                    else:
                        rev = True
                    if os.path.exists(f'{folder_video}\\{file_name[0]}.mp4'):
                        print(f"File {folder_video}\\{file_name[0]}.mp4 found in the folder.")
                    else:
                        ImageEditor.ken_burns_effect_video(image_path=f'{folter_image_crop}\\{file}', output_path=f'{folder_video}\\{file_name[0]}.mp4', duration=5, reverse=rev)
                    count += 1
        except:
            exit('Error: Failed to create video')

        if not os.path.exists(folder_final):
            os.makedirs(folder_final)
            print(f"Folder {folder_final} created")
        else:
            print(f"Folder {folder_final} already exists")

        # -------------------------------------------------------------------- CREATE VIDEO -----------------------------------------------------------------------------
        
        current_file = ''
        for i in range(1,15):
            file = f"{i}.mp4"
            if i==1:
                current_file = file
            else:
                clip1 = VideoFileClip(f"{folder_video}\\{current_file}")
                clip2 = VideoFileClip(f"{folder_video}\\{file}")
                if os.path.exists(f"{folder_video}\\1-{i}.mp4"):
                    print(f"File {folder_video}\\1-{i}.mp4 found in the folder.")
                else:
                    result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.6)
                    result_clip.write_videofile(f"{folder_video}\\1-{i}.mp4", codec="libx264", audio_codec=None)
                    result_clip.close()
                clip1.close()
                clip2.close()
                current_file = f'1-{i}.mp4'

        # ------------------------------------------------------------- END ----------------------------------------------------------------------------

        try:
            if os.path.exists(f'{folder_video}\\1-14_crop.mp4'):
                print(f"File 1-14_crop.mp4 found in the folder.")
            else:
                VideoEditor.crop(video_path=f'{folder_video}\\1-14.mp4', output_path= f'{folder_video}\\1-14_crop.mp4', audio_path = audio_file)
        except:
            exit(f'Error: Failed to crop video 1-14_crop.mp4')

        try:
            if os.path.exists(video_sound):
                print(f"File {video_sound} found in the folder.")
            else:
                video = f"{folder_video}\\1-14_crop.mp4"
                result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
        except:
            exit('Error: Failed to create video video_sub')
        
        try:
            if text!='':
                sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
                sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black',font='Segoe-UI-Bold')
            else:
                exit(f'Error: File {CLIP_NAME}.txt is empty')
        except:
            exit('Error: Failed to create subtitles')

        try:
            if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}.mp4'):
                print(f"File final_video_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip = VideoFileClip(video_sound)
                result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
                result_clip.write_videofile(f'{folder_video}\\final_video_{CLIP_NAME}.mp4', codec="libx264", audio_codec=None)
                clip.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video video_sub')

        try:
            if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}.mp4'):
                VideoEditor.crop(video_path=f'{folder_video}\\final_video_{CLIP_NAME}.mp4', output_path= f'{folder_video}\\final_video_crop_{CLIP_NAME}.mp4')
            else:
                print(f"File final_video_{CLIP_NAME}.mp4 not found in the folder.")
        except:
            exit(f'Error: Failed to crop video final_video_{CLIP_NAME}.mp4')
        print('Successfully!')

def create_shorts_en():
    text=''
    audio_file = f'audio\\voice_{CLIP_NAME}_en.mp3'
    video_sound = f'video\\{CLIP_NAME}\\video_sound_{CLIP_NAME}_en.mp4'
    folder_video = f'video\\{CLIP_NAME}'

    try:
        with open(f'text\\{CLIP_NAME}_en.txt', 'r', encoding='UTF-8') as file:
            text = file.read()
            file.close()
    except:
        exit('Error: Reading error')

    try:
        if os.path.exists(audio_file):
            print(f"File {audio_file} exists.")
        else:
            AudioEditor.create_voice(text=text,output_file=audio_file)
    except:
        exit('Error: Failed to create sound')   

    try:
        if os.path.exists(f'{folder_video}\\1-14.mp4'):
            VideoEditor.crop(video_path=f'{folder_video}\\1-14.mp4', output_path= f'{folder_video}\\1-14_crop.mp4', audio_path=audio_file)
        else:
            print(f"File 1-14_crop.mp4 not found in the folder.")
    except:
        exit(f'Error: Failed to crop video 1-14.mp4')
    
    try:
        if os.path.exists(video_sound):
            print(f"File {video_sound} found in the folder.")
        else:
            video = f"{folder_video}\\1-14_crop.mp4"
            result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
    except:
        exit('Error: Failed to create video video_sub')
        
    try:
        if text!='':
            sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
            sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black', font='Arial-Rounded-MT-Bold')
        else:
            exit(f'Error: File {CLIP_NAME}.txt is empty')
    except:
        exit('Error: Failed to create subtitles')
            
    try:
        if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4'):
            print(f"File final_video_en.mp4 found in the folder.")
        else:
            clip = VideoFileClip(video_sound)
            result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
            result_clip.write_videofile(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4', codec="libx264", audio_codec=None)
            clip.close()
            result_clip.close()
    except:
        exit('Error: Failed to create video final_video_en.mp4')

    print('Successfully!')

def chromoKey():

    # Определение диапазона цветов хромакея (зеленого фона)
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([90, 255, 255])

    # Загрузка видеофайлов
    cap_chromakey = cv2.VideoCapture('mrSim.mp4')
    cap_background = cv2.VideoCapture('video\\Comet\\78_Comet.mp4')

    # # Определение параметров видео (ширина, высота и частота кадров)
    # width_chromakey = int(cap_chromakey.get(3))
    # height_chromakey = int(cap_chromakey.get(4))
    # # print(width_chromakey,height_chromakey)

    # width_background = int(cap_background.get(3))
    # height_background = int(cap_background.get(4))
    # # print(width_background,height_background)

    # fps = int(cap_chromakey.get(5))

    # # Определение кодека и создание объекта VideoWriter
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Используйте 'mp4v' для кодирования в MP4
    # out = cv2.VideoWriter('output_with_background.mp4', fourcc, fps, (width_background, height_background))

    # while cap_chromakey.isOpened() and cap_background.isOpened():
    #     ret_chromakey, frame_chromakey = cap_chromakey.read()
    #     ret_background, frame_background = cap_background.read()

    #     if not ret_chromakey or not ret_background:
    #         break

    #     # Преобразование изображения в цветовое пространство HSV
    #     hsv = cv2.cvtColor(frame_chromakey, cv2.COLOR_BGR2HSV)

    #     # Создание маски хромакея
    #     mask = cv2.inRange(hsv, lower_green, upper_green)

    #     # Инвертирование маски
    #     inverted_mask = cv2.bitwise_not(mask)

    #     # Применение инвертированной маски к кадру хромакея
    #     chromakey_result = cv2.bitwise_and(frame_chromakey, frame_chromakey, mask=inverted_mask)

    #     # Применение маски к заднему фону
    #     background_result = cv2.bitwise_and(frame_background, frame_background, mask=mask)

    #     # Изменение размеров кадра хромакея
    #     chromakey_result = cv2.resize(chromakey_result, (width_background, height_background))

    #     # Сложение двух кадров
    #     result = cv2.addWeighted(chromakey_result, 1, background_result, 1, 0, dtype=cv2.CV_8U)

    #     # Запись обработанного кадра в видеофайл
    #     out.write(result)

    #     # Отображение результата
    #     cv2.imshow('With Background', result)

    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         break

    # cap_chromakey.release()
    # cap_background.release()
    # out.release()
    # cv2.destroyAllWindows()

        # Определение параметров видео (ширина, высота и частота кадров)
    width = int(cap_chromakey.get(3))
    height = int(cap_chromakey.get(4))
    fps = int(cap_chromakey.get(5))

    # Определение кодека и создание объекта VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Используйте 'mp4v' для кодирования в MP4
    out = cv2.VideoWriter('output_with_background_chromakey.mp4', fourcc, fps, (width, height))

    # Определение начального и конечного кадра для применения хромакея
    start_frame = 100
    end_frame = 200

    frame_number = 0

    while cap_chromakey.isOpened() and cap_background.isOpened():
        ret_chromakey, frame_chromakey = cap_chromakey.read()
        ret_background, frame_background = cap_background.read()

        if not ret_chromakey or not ret_background:
            break

        # Преобразование изображения в цветовое пространство HSV
        hsv = cv2.cvtColor(frame_chromakey, cv2.COLOR_BGR2HSV)

        # Создание маски хромакея
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Инвертирование маски
        inverted_mask = cv2.bitwise_not(mask)

        # Применение инвертированной маски к кадру хромакея
        chromakey_result = cv2.bitwise_and(frame_chromakey, frame_chromakey, mask=inverted_mask)

        # Применение маски к заднему фону
        background_result = cv2.bitwise_and(frame_background, frame_background, mask=mask)

        # Изменение размеров кадра хромакея
        chromakey_result = cv2.resize(chromakey_result, (width, height))

        # Сложение двух кадров только в заданном промежутке
        if start_frame <= frame_number <= end_frame:
            result = cv2.addWeighted(chromakey_result, 1, background_result, 1, 0, dtype=cv2.CV_8U)
        else:
            result = frame_background

        # Запись обработанного кадра в видеофайл
        out.write(result)

        # Отображение результата
        cv2.imshow('With Background Chromakey', result)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        frame_number += 1

    cap_chromakey.release()
    cap_background.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    start_time = time.time()

    # create_shorts_ru()
    # create_shorts_en()


    # len = len_simbols('text\\voice_Lava_en.txt')
    # print(len)
    # clip = AudioFileClip('audio\\Lava.mp3').duration
    # print(clip)

    chromoKey()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time/60} минут")

    # ImageEditor.get_pexels_images(api_key=key,save_path=f'image\\{CLIP_NAME}')




if __name__ == "__main__":
    main()
from audio import AudioEditor
from subtitle import SubtitleEditor, len_simbols
from video import VideoEditor, AudioFileClip
from image import ImageEditor
from youtube import post_shorts
import os 
from moviepy.editor import VideoFileClip, VideoClip, ImageClip, CompositeVideoClip, TextClip, concatenate_videoclips
# from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
# import pyttsx3
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import fnmatch
import wave
import numpy as np
import time
from PIL import Image
import cv2
key = 'MVsaiNhymA81LvKqS9oezJeEpyZ2pYDtq9zFFQvnuWPwCMPmhiOLaI88'

CLIP_NAME = 'Aurora'
CLIP_NAME_RU = "Северное\nсияние"
SECOND_FRAME_RU = "Интересные факты"
SECOND_FRAME_EN = 'Interesting Facts'

def create_shorts_ru():
        count = 1
        text=''
        folder_image = f'image\\{CLIP_NAME}'
        folter_image_crop = f'image_crop\\{CLIP_NAME}'
        folter_image_resize = f'image_resize\\{CLIP_NAME}'
        folder_video = f'video\\{CLIP_NAME}'
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
            video = VideoClip(make_frame=make_frame_ru, duration=0.1)
            video.write_videofile(f'video\\{CLIP_NAME}\\{CLIP_NAME}_ru.mp4', fps=30, codec="libx264")
        except:
            print('Ошибка создания Заставки!')

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
                    result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
                    result_clip.write_videofile(f"{folder_video}\\1-{i}.mp4", codec="libx264", audio_codec=None, fps=30)
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
                print('Создан файл 1-14_crop.mp4')
        except:
            exit(f'Error: Failed to crop video 1-14_crop.mp4')
        
        try:
            if os.path.exists(f'video\\{CLIP_NAME}\\chromo_{CLIP_NAME}_ru.mp4'):
                print(f"File chromo_{CLIP_NAME}_ru.mp4 found in the folder.")
            else:
                VideoEditor.chromoKey(input_path=f'{folder_video}\\1-14_crop.mp4', output_path=f'video\\{CLIP_NAME}\\chromo_{CLIP_NAME}_ru.mp4')
                print('Создано видео с хромакеем')
        except:
            exit('Ошибка создания видео с хромакеем!')

        try:
            if os.path.exists(video_sound):
                print(f"File {video_sound} found in the folder.")
            else:
                video = f'video\\{CLIP_NAME}\\chromo_{CLIP_NAME}_ru.mp4'
                result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
                print(f'Создан файл video_sound_{CLIP_NAME}.mp4')
        except:
            exit('Ошибка создания видео со звуком!')
        
        try:
            if text!='':
                sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
                sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black',font='Segoe-UI-Bold')
                print('Созданы субтитры')
            else:
                exit(f'Error: File {CLIP_NAME}.txt is empty')
        except:
            exit('Ошибка создания субтитров!')

        try:
            if os.path.exists(f'{folder_video}\\sub_video_{CLIP_NAME}_ru.mp4'):
                print(f"File sub_video_{CLIP_NAME}_ru.mp4 found in the folder.")
            else:
                clip = VideoFileClip(video_sound)
                result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
                result_clip.write_videofile(f'{folder_video}\\sub_video_{CLIP_NAME}_ru.mp4', codec="libx264", audio_codec=None, fps=30)
                clip.close()
                result_clip.close()
                print(f'Создано видео с субтитрами sub_video_{CLIP_NAME}_ru.mp4')
        except:
            exit('Ошибка создания видео с субтитрами!')

        try:
            if os.path.exists(f'video\\{CLIP_NAME}\\main_frame_ru.mp4'):
                print(f"File main_frame_ru.mp4 found in the folder.")
            else:
                video1 = VideoFileClip(f'video\\{CLIP_NAME}\\{CLIP_NAME}_ru.mp4')
                video2 = VideoFileClip(f'{folder_video}\\sub_video_{CLIP_NAME}_ru.mp4')
                final_clip = concatenate_videoclips([video1, video2])
                final_clip.write_videofile(f'video\\{CLIP_NAME}\\main_frame_ru.mp4', codec="libx264", audio_codec="aac", fps=30)
                video1.close()
                video2.close()
                print(f'Создано видео с заставкой main_frame_ru.mp4')
        except:
            exit('Ошибка обьединения Заставки с видео!')

        try:
            if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}_ru.mp4'):
                print(f"File final_video_{CLIP_NAME}_ru.mp4 found in the folder.")
            else:
                VideoEditor.crop(video_path=f'video\\{CLIP_NAME}\\main_frame_ru.mp4', output_path= f'{folder_video}\\final_video_{CLIP_NAME}_ru.mp4')
                print(f'Создано финальное видео final_video_{CLIP_NAME}_ru.mp4')
        except:
            exit(f'Ошибка создания финального видео final_video_{CLIP_NAME}_ru.mp4!')
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
        video = VideoClip(make_frame=make_frame_en, duration=0.1)
        video.write_videofile(f'video\\{CLIP_NAME}\\{CLIP_NAME}_en.mp4', fps=24, codec="libx264")
    except:
        exit('Ошибка создания Заставки!')

    try:
        if os.path.exists(f'{folder_video}\\1-14.mp4'):
            VideoEditor.crop(video_path=f'{folder_video}\\1-14.mp4', output_path= f'{folder_video}\\1-14_crop_en.mp4', audio_path=audio_file)
            print('Создано видео 1-14_crop_en.mp4')
        else:
            print(f"File 1-14_crop.mp4 not found in the folder.")
    except:
        exit(f'Error: Failed to crop video 1-14.mp4')

    try:
        if os.path.exists(f'video\\{CLIP_NAME}\\chromo_{CLIP_NAME}_en.mp4'):
            print(f"File chromo_{CLIP_NAME}_en.mp4 found in the folder.")
        else:
            VideoEditor.chromoKey(input_path=f'{folder_video}\\1-14_crop_en.mp4', output_path=f'video\\{CLIP_NAME}\\chromo_{CLIP_NAME}_en.mp4')
            print('Создано видео с хромакеем')
    except:
            exit('Ошибка создания видео с хромакеем!')
    
    try:
        if os.path.exists(video_sound):
            print(f"File {video_sound} found in the folder.")
        else:
            video = f'video\\{CLIP_NAME}\\chromo_{CLIP_NAME}_en.mp4'
            result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
            print(f'Создано видео со звуком {video_sound}')
    except:
        exit('Error: Failed to create video video_sub')
        
    try:
        if text!='':
            sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
            sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black', font='Arial-Rounded-MT-Bold')
            print(f'Созданы субтитры на английском')
        else:
            exit(f'Error: File {CLIP_NAME}.txt is empty')
    except:
        exit('Error: Failed to create subtitles')
            
    try:
        if os.path.exists(f'{folder_video}\\sub_video_{CLIP_NAME}_en.mp4'):
            print(f"File sub_video_en.mp4 found in the folder.")
        else:
            clip = VideoFileClip(video_sound)
            result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
            result_clip.write_videofile(f'{folder_video}\\sub_video_{CLIP_NAME}_en.mp4', codec="libx264", audio_codec=None)
            print(f'Создано видео с субтитрами на английском')
            clip.close()
            result_clip.close()
    except:
        exit('Error: Failed to create video final_video_en.mp4')

    try:
        video1 = VideoFileClip(f'video\\{CLIP_NAME}\\{CLIP_NAME}_en.mp4')
        video2 = VideoFileClip(f'video\\{CLIP_NAME}\\sub_video_{CLIP_NAME}_en.mp4')
        final_clip = concatenate_videoclips([video1, video2])
        final_clip.write_videofile(f'video\\{CLIP_NAME}\\main_frame_en.mp4', codec="libx264", audio_codec="aac")
        video1.close()
        video2.close()
        print(f'Создано видео с заставкой main_frame_en.mp4')
    except:
        exit('Ошибка обьединения Заставки с видео!')

    try:
        if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4'):
            print(f"File final_video_{CLIP_NAME}_en.mp4 found in the folder.")
        else:
            VideoEditor.crop(video_path=f'video\\{CLIP_NAME}\\main_frame_en.mp4', output_path= f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4')
            print(f'Создано финальное видео final_video_{CLIP_NAME}_en.mp4')
    except:
        exit(f'Ошибка создания финального видео final_video_{CLIP_NAME}_en.mp4!')

    print('ОТЛИЧНАЯ РАБОТА!')

def make_frame_en(t):
    image_path = f'image_crop\\{CLIP_NAME}\\1.jpg'
    image_clip = ImageClip(image_path)
    subtitle_clip_line1 = TextClip(CLIP_NAME, fontsize=24, color='white', stroke_color='black',stroke_width=3, font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    subtitle_clip_line3 = TextClip(SECOND_FRAME_EN, fontsize=24, color='white', stroke_color='black',stroke_width=1,font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    position_line1 = ('center', 'center' )
    position_line3 = ('center', image_clip.size[1]-500)
    video_clip = CompositeVideoClip([image_clip, subtitle_clip_line1.set_position(position_line1).set_duration(image_clip.duration), subtitle_clip_line3.set_position(position_line3).set_duration(image_clip.duration)])
    video_clip = video_clip.set_duration(10)  # Установите нужную продолжительность
    return video_clip.get_frame(t)

def make_frame_ru(t):
    image_path = f'image_crop\\{CLIP_NAME}\\1.jpg'
    image_clip = ImageClip(image_path)
    subtitle_clip_line1 = TextClip(CLIP_NAME_RU, fontsize=24, color='white', stroke_color='black',stroke_width=3, font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    subtitle_clip_line3 = TextClip(SECOND_FRAME_RU, fontsize=24, color='white', stroke_color='black',stroke_width=1,font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    position_line1 = ('center', 'center' )
    position_line3 = ('center', image_clip.size[1]-500)
    video_clip = CompositeVideoClip([image_clip, subtitle_clip_line1.set_position(position_line1).set_duration(image_clip.duration), subtitle_clip_line3.set_position(position_line3).set_duration(image_clip.duration)])
    video_clip = video_clip.set_duration(10)  # Установите нужную продолжительность
    return video_clip.get_frame(t)

def process_audio_file(audio_file_path):
    # Получение текста из аудио файла
    audio_text = 'в этот период аврора может проявляться в виде круговых образов, называемых "Кольца Кроули". Полярные сияния весной и о́сенью возникают заметно чаще'
    if audio_text is not None:
        # Получение длительности аудио файла
        audio = AudioSegment.from_file(audio_file_path, format="mp3")
        audio_duration = len(audio) / 1000  # преобразование миллисекунд в секунды
        # Извлечение времени начала и конца каждого слова
        word_timings = extract_word_timings(audio_text, audio_duration)
        return word_timings
    return None

def extract_word_timings(audio_text, audio_duration):
    # Определение времени начала и конца каждого слова на основе текста и длительности аудио
    word_timings = []
    words = audio_text.split()
    word_start = 0
    word_end = 0
    for word in words:
        word_duration = len(word) / len(audio_text) * audio_duration
        word_end = word_start + word_duration
        word_timings.append({"word": word, "start": word_start, "end": word_end})
        word_start = word_end
    return word_timings

def main():
    start_time = time.time()

    # create_shorts_ru()
    # create_shorts_en()


    # len = len_simbols('text\\Aurora_ru.txt')
    # print(len)
    # clip = AudioFileClip('audio\\voice_Aurora_ru.mp3').duration
    # print(clip)

    audio_file_path = "test.mp3"
    result = process_audio_file(audio_file_path)
    if result is not None:
        for item in result:
            print(f"Слово: {item['word']}, Начало: {item['start']:.2f} сек., Конец: {item['end']:.2f} сек.")


    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time/60} минут")

    # ImageEditor.get_pexels_images(api_key=key,save_path=f'image\\{CLIP_NAME}')
    'в этот период аврора может проявляться в виде круговых образов, называемых "Кольца Кроули". Полярные сияния весной и о́сенью возникают заметно чаще'
  


if __name__ == "__main__":
    main()
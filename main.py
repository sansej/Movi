from audio import AudioEditor
from subtitle import SubtitleEditor, len_simbols
from video import VideoEditor, AudioFileClip
from image import ImageEditor
from youtube import post_shorts
# import speech_recognition as sr
from pytube import YouTube
import os 
from moviepy.editor import VideoFileClip, VideoClip, ImageClip, CompositeVideoClip, TextClip, concatenate_videoclips
# from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
# import pyttsx3
from pydub import AudioSegment, silence
# from vosk import Model, KaldiRecognizer
import fnmatch
import wave
import numpy as np
import keyboard
import mouse
import json 
import time
from datetime import datetime, timedelta
from PIL import Image
import cv2
key = 'MVsaiNhymA81LvKqS9oezJeEpyZ2pYDtq9zFFQvnuWPwCMPmhiOLaI88'

PROJECT_NAME = 'KuiperBelt'
CLIP_NAME_EN = "Kuiper\nBelt"
CLIP_NAME_RU = "Пояс\nКойпера" #для разделения слов использовать \n
SECOND_FRAME_RU = "Интересные факты"
SECOND_FRAME_EN = 'Interesting Facts'

def create_shorts_ru():
        count = 1
        text=''
        folder_source = f'{PROJECT_NAME}\\RU\\source'
        folter_image_crop = f'{PROJECT_NAME}\\RU\\image_crop'
        folter_image_resize = f'{PROJECT_NAME}\\RU\\image_resize'
        folder_video = f'{PROJECT_NAME}\\RU\\video'
        voice = f'{PROJECT_NAME}\\RU\\voice_{PROJECT_NAME}_ru.mp3'
        audio_file = f'{PROJECT_NAME}\\RU\\{PROJECT_NAME}_ru.mp3'
        video_sound = f'{folder_video}\\video_sound_{PROJECT_NAME}.mp4'
        # image_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png','10.png','11.png','12.png','13.png','14.png']

        try:
            with open(f'{PROJECT_NAME}\\RU\\{PROJECT_NAME}_ru.txt', 'r', encoding='UTF-8') as file:
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
            print("Папка image_crop создана")
        else:
            print("Папка image_crop уже существует")

        if not os.path.exists(folter_image_resize):
            os.makedirs(folter_image_resize)
            print("Папка image_resize создана")
        else:
            print("Папка image_resize уже существует")

        if not os.path.exists(folder_video):
            os.makedirs(folder_video)
            print("Папка video создана")
        else:
            print("Папка video уже существует")

        try:
            for file in os.listdir(folder_source):
                # if any(fnmatch.fnmatch(file, img) for img in image_list):
                if file.endswith('.jpg'):
                    try:
                        file_name = file.split('.')
                        ImageEditor.resize(input_path=f'{folder_source}\\{file}', output_path=f'{folter_image_resize}\\{file_name[0]}.{file_name[1]}')
                        print(f'{file} resize')
                        ImageEditor.crop_image(input_path=f'{folter_image_resize}\\{file_name[0]}.{file_name[1]}', output_path=f'{folter_image_crop}\\{file_name[0]}.{file_name[1]}')
                        print(f'{file} crop')
                    except FileNotFoundError:
                        print(f'{file} не найден')
                    except FileExistsError:
                        print(f'{file_name[0]}.{file_name[1]} уже существует')
                    except Exception as e:
                        print(f'Error: {e}')
                elif file.endswith('.mp4'):
                    if not os.path.exists(f'{folder_video}\\{file}'):
                        VideoEditor.cut_resize_crop(video_path=f'{folder_source}\\{file}',output_path=f'{folder_video}\\{file}')
                    else:
                        print(f"{file} уже существует")
                else:
                    print('Неверный формат исходного файла!')
        except Exception as e:
            exit(f'Ошибка: {e}')

        try:
            video = VideoClip(make_frame=make_frame_ru, duration=0.1)
            video.write_videofile(f'{folder_video}\\frame_{PROJECT_NAME}_ru.mp4', fps=30, codec="libx264")
        except Exception as e:
            print(f'Ошибка: {e}')

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
                        print(f"Файл {file_name[0]}.mp4 существует!")
                    else:
                        ImageEditor.ken_burns_effect_video(image_path=f'{folter_image_crop}\\{file}', output_path=f'{folder_video}\\{file_name[0]}.mp4', duration=5, reverse=rev)
                    count += 1
        except:
            exit('Ошибка: Видео не создано')

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
                    print(f"Файл {folder_video}\\1-{i}.mp4 существует!")
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
                print("Файл 1-14_crop.mp4 существует!")
            else:
                VideoEditor.crop(video_path=f'{folder_video}\\1-14.mp4', output_path= f'{folder_video}\\1-14_crop.mp4', audio_path = f'{PROJECT_NAME}\\RU\\{PROJECT_NAME}_ru.mp3')
                print('Создан файл 1-14_crop.mp4')
        except Exception as e:
            exit(f'Ошибка: {e}')
        
        try:
            if os.path.exists(f'{folder_video}\\chromo_{PROJECT_NAME}_ru.mp4'):
                print(f"Файл chromo_{PROJECT_NAME}_ru.mp4 найден")
            else:
                VideoEditor.chromoKey(input_path=f'{folder_video}\\1-14_crop.mp4', output_path=f'{folder_video}\\chromo_{PROJECT_NAME}_ru.mp4')
                print('Создано видео с хромакеем')
        except:
            exit('Ошибка создания видео с хромакеем!')

        try:
            if os.path.exists(video_sound):
                print(f"Файл {video_sound} найден")
            else:
                video = f'{folder_video}\\chromo_{PROJECT_NAME}_ru.mp4'
                result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
                print(f'Создан файл video_sound_{PROJECT_NAME}.mp4')
        except:
            exit('Ошибка создания видео со звуком!')
        
        try:
            if text!='':
                sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
                sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black',font='Segoe-UI-Bold')
                print('Созданы субтитры')
            else:
                exit(f'Ошибка: {PROJECT_NAME}.txt пуст')
        except:
            exit('Ошибка создания субтитров!')

        try:
            if os.path.exists(f'{folder_video}\\sub_video_{PROJECT_NAME}_ru.mp4'):
                print(f"sub_video_{PROJECT_NAME}_ru.mp4 существует!")
            else:
                clip = VideoFileClip(video_sound)
                result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
                result_clip.write_videofile(f'{folder_video}\\sub_video_{PROJECT_NAME}_ru.mp4', codec="libx264", audio_codec=None, fps=30)
                clip.close()
                result_clip.close()
                print(f'Создано видео с субтитрами sub_video_{PROJECT_NAME}_ru.mp4')
        except:
            exit('Ошибка создания видео с субтитрами!')

        try:
            if os.path.exists(f'{folder_video}\\{PROJECT_NAME}_ru.mp4'):
                print(f"{PROJECT_NAME}_ru.mp4 существует!")
            else:
                video1 = VideoFileClip(f'{folder_video}\\frame_{PROJECT_NAME}_ru.mp4')
                video2 = VideoFileClip(f'{folder_video}\\sub_video_{PROJECT_NAME}_ru.mp4')
                final_clip = concatenate_videoclips([video1, video2])
                final_clip.write_videofile(f'{PROJECT_NAME}\\{PROJECT_NAME}_ru.mp4', codec="libx264", audio_codec="aac", fps=30)
                video1.close()
                video2.close()
                print(f'Создано видео с заставкой {PROJECT_NAME}_ru.mp4')
        except:
            exit('Ошибка обьединения Заставки с видео!')

        try:
            if os.path.exists(f'{folder_video}\\final_{PROJECT_NAME}_ru.mp4'):
                print(f"final_{PROJECT_NAME}_ru.mp4 существует!")
            else:
                VideoEditor.crop(video_path=f'{PROJECT_NAME}\\{PROJECT_NAME}_ru.mp4', output_path= f'{PROJECT_NAME}\\final_{PROJECT_NAME}_ru.mp4')
                print(f'Создано финальное видео final_{PROJECT_NAME}_ru.mp4')
        except:
            exit(f'Ошибка создания финального видео final_{PROJECT_NAME}_ru.mp4!')
        print(f'Успешно создано final_{PROJECT_NAME}_ru.mp4')

def create_shorts_en():
    text=''
    audio_file = f'{PROJECT_NAME}\\EN\\{PROJECT_NAME}_en.mp3'
    folder_video = f'{PROJECT_NAME}\\EN\\video'
    video_sound = f'{folder_video}\\video_sound_{PROJECT_NAME}_en.mp4'

    if not os.path.exists(folder_video):
            os.makedirs(folder_video)
            print("Папка video создана")
    else:
        print("Папка video уже существует!")

    try:
        with open(f'{PROJECT_NAME}\\EN\\{PROJECT_NAME}_en.txt', 'r', encoding='UTF-8') as file:
            text = file.read()
            file.close()
    except:
        exit('Ошибка: Чтение файла')

    try:
        if os.path.exists(audio_file):
            print(f"{audio_file} существует!")
        else:
            AudioEditor.create_voice(text=text,output_file=audio_file)
    except:
        exit(f'Ошибка: Создание {PROJECT_NAME}_en.mp3')   

    try:
        video = VideoClip(make_frame=make_frame_en, duration=0.1)
        video.write_videofile(f'{folder_video}\\frame_{PROJECT_NAME}_en.mp4', fps=24, codec="libx264")
    except:
        exit('Ошибка создания Заставки!')

    try:
        if os.path.exists(f'{folder_video}\\1-14.mp4'):
            VideoEditor.crop(video_path=f'{folder_video}\\1-14.mp4', output_path= f'{folder_video}\\1-14_crop_en.mp4', audio_path=audio_file)
            print('Создано видео 1-14_crop_en.mp4')
        else:
            print("1-14_crop.mp4 не найден")
    except:
        exit('Ошибка: Не создано 1-14_crop.mp4')

    try:
        if os.path.exists(f'{folder_video}\\chromo_{PROJECT_NAME}_en.mp4'):
            print(f"chromo_{PROJECT_NAME}_en.mp4 существует!")
        else:
            VideoEditor.chromoKey(input_path=f'{PROJECT_NAME}\\RU\\video\\1-14_crop.mp4', output_path=f'{folder_video}\\chromo_{PROJECT_NAME}_en.mp4')
            print('Создано видео с хромакеем')
    except:
            exit('Ошибка создания видео с хромакеем!')
    
    try:
        if os.path.exists(video_sound):
            print(f"{video_sound} существует!")
        else:
            video = f'{folder_video}\\chromo_{PROJECT_NAME}_en.mp4'
            result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
            print(f'Создано видео со звуком {video_sound}')
    except:
        exit(f'Ошибка: Создание {video_sound}')
        
    try:
        if text!='':
            sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
            sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black', font='Arial-Rounded-MT-Bold')
            print(f'Созданы субтитры на английском')
        else:
            exit(f'Ошибка: {PROJECT_NAME}.txt пуст')
    except:
        exit('Ошибка: Создание субтитров')
            
    try:
        if os.path.exists(f'{folder_video}\\sub_video_{PROJECT_NAME}_en.mp4'):
            print("sub_video_en.mp4 существует")
        else:
            clip = VideoFileClip(video_sound)
            result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
            result_clip.write_videofile(f'{folder_video}\\sub_video_{PROJECT_NAME}_en.mp4', codec="libx264", audio_codec=None)
            print(f'Создано видео с субтитрами на английском')
            clip.close()
            result_clip.close()
    except:
        exit('Ошибка: Создание final_video_en.mp4')

    try:
        video1 = VideoFileClip(f'{folder_video}\\frame_{PROJECT_NAME}_en.mp4')
        video2 = VideoFileClip(f'{folder_video}\\sub_video_{PROJECT_NAME}_en.mp4')
        final_clip = concatenate_videoclips([video1, video2])
        final_clip.write_videofile(f'{PROJECT_NAME}\\{PROJECT_NAME}_en.mp4', codec="libx264", audio_codec="aac")
        video1.close()
        video2.close()
        print(f'Создано видео с заставкой {PROJECT_NAME}_en.mp4')
    except:
        exit('Ошибка обьединения Заставки с видео!')

    try:
        if os.path.exists(f'{PROJECT_NAME}\\final_{PROJECT_NAME}_en.mp4'):
            print(f"final_{PROJECT_NAME}_en.mp4 существует!")
        else:
            VideoEditor.crop(video_path=f'{PROJECT_NAME}\\{PROJECT_NAME}_en.mp4', output_path= f'{PROJECT_NAME}\\final_{PROJECT_NAME}_en.mp4')
            print(f'Создано финальное видео final_{PROJECT_NAME}_en.mp4')
    except:
        exit(f'Ошибка создания финального видео final_{PROJECT_NAME}_en.mp4!')

    print('ОТЛИЧНАЯ РАБОТА!')

def make_frame_en(t):
    image_path = f'{PROJECT_NAME}\\RU\\image_crop\\frame.jpg'
    image_clip = ImageClip(image_path)
    subtitle_clip_line1 = TextClip(CLIP_NAME_EN, fontsize=24, color='white', stroke_color='black',stroke_width=3, font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    subtitle_clip_line3 = TextClip(SECOND_FRAME_EN, fontsize=24, color='white', stroke_color='black',stroke_width=1,font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    position_line1 = ('center', 'center' )
    position_line3 = ('center', image_clip.size[1]-400)
    video_clip = CompositeVideoClip([image_clip, subtitle_clip_line1.set_position(position_line1).set_duration(image_clip.duration), subtitle_clip_line3.set_position(position_line3).set_duration(image_clip.duration)])
    video_clip = video_clip.set_duration(10)  # Установите нужную продолжительность
    return video_clip.get_frame(t)

def make_frame_ru(t):
    image_path = f'{PROJECT_NAME}\\RU\\image_crop\\frame.jpg'
    image_clip = ImageClip(image_path)
    subtitle_clip_line1 = TextClip(CLIP_NAME_RU, fontsize=24, color='white', stroke_color='black',stroke_width=3, font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    subtitle_clip_line3 = TextClip(SECOND_FRAME_RU, fontsize=24, color='white', stroke_color='black',stroke_width=1,font='Segoe-UI-Bold', size=(image_clip.size[0]*3/4, None))
    position_line1 = ('center', 'center' )
    position_line3 = ('center', image_clip.size[1]-400)
    video_clip = CompositeVideoClip([image_clip, subtitle_clip_line1.set_position(position_line1).set_duration(image_clip.duration), subtitle_clip_line3.set_position(position_line3).set_duration(image_clip.duration)])
    video_clip = video_clip.set_duration(10)  # Установите нужную продолжительность
    return video_clip.get_frame(t)

# def transcribe_audio(file_path):
#     recognizer = sr.Recognizer()

#     # Загрузка аудио файла
#     audio = AudioSegment.from_file(file_path, format="mp3")

#     # Сохранение аудио во временный WAV-файл
#     temp_wav_file = "temp_audio.wav"
#     audio.export(temp_wav_file, format="wav")

#     # Преобразование временного WAV-файла в текст
#     with sr.AudioFile(temp_wav_file) as source:
#         audio_text = recognizer.record(source)

#     try:
#         text = recognizer.recognize_google(audio_text, language="ru-RU")
#         return text
#     except sr.UnknownValueError:
#         print("Речь не распознана")
#         return None
#     except sr.RequestError as e:
#         print(f"Ошибка сервиса распознавания речи: {e}")
#         return None

# def extract_word_timings(audio_text, audio_file_path):
#     # Определение времени начала и конца каждого слова на основе текста и длительности аудио

#     # Получение времени молчания (пауз) в аудио
#     audio = AudioSegment.from_file(audio_file_path, format="mp3")
#     audio_duration = len(audio) / 1000  # преобразование миллисекунд в секунды
#     # Сохранение аудио во временный WAV-файл
#     # temp_wav_file = "temp_audio.wav"
#     # audio.export(temp_wav_file, format="wav")
#     # recognizer = sr.Recognizer()

#     silent_ranges = silence.detect_silence(audio, min_silence_len=530, silence_thresh=-40)

#     # Перевод в миллисекунды
#     silent_ranges = [(start / 1000, stop / 1000) for start, stop in silent_ranges]
#     print(silent_ranges)

#     tim = 0
#     for item in silent_ranges:
#         tim = tim + item[1]-item[0]
#     print(tim)
#     word_timings = []
#     words = audio_text.split()

#     word_start = 0
#     word_end = 0

#     for word in words:
#         word_duration = len(word) / len(audio_text) * audio_duration
#         word_end = word_start + word_duration
#         word_timings.append({"word": word, "start": word_start, "end": word_end})
#         word_start = word_end + tim/(len(words)-1)

#     return word_timings



def download_youtube_video(url, output_path='downloads', resolution = 'highest'):
    try:
        # Создаем объект YouTube
        yt = YouTube(url)

        # Получаем список видеопотоков
        streams = yt.streams.filter(file_extension='mp4')

        # Если выбрано конкретное разрешение, выбираем соответствующий поток
        if resolution != 'highest':
            streams = streams.filter(res=resolution)
        
        # Получаем видеопоток
        video = streams.first()

        # Проверяем, доступен ли видеопоток
        if video is None:
            print("Не удалось найти видео с выбранным разрешением.")
            return

        # Создаем папку для сохранения видео, если ее нет
        import os
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Скачиваем видео
        print(f"Загрузка видео ({resolution} разрешение): {yt.title}")
        video.download(output_path)
        print("Загрузка завершена!")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

def get_video_resolution(video_path):
    # Открываем видеофайл
    cap = cv2.VideoCapture(video_path)

    # Получаем разрешение видео
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Закрываем видеофайл
    cap.release()
    print(width, height)

    return width, height

def reresolution(video_path,output_path):

    cap = cv2.VideoCapture(video_path)

    # Получаем текущее разрешение видео
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Вычисляем новое разрешение с сохранением соотношения сторон
    new_width, new_height = 720, int(720 / width * height)

    # Указываем кодек и новое разрешение
    fourcc = cv2.VideoWriter_fourcc(*'MP4V') #MP4V X264
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (new_width, new_height))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Изменяем разрешение кадра
        frame_resized = cv2.resize(frame, (new_width, new_height))

        # Записываем измененный кадр в выходное видео
        out.write(frame_resized)

    # Освобождаем ресурсы
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def split_video(input_video_path, output_video_path, start_time, end_time, resolution=(720,1280)):
    """
    Изменяет разрешение видео и обрезает его, чтобы подогнать под заданные размеры.

    :param input_video_path: Путь к входному видеофайлу.
    :param output_folder: Папка для сохранения выходных видеофайлов.
    :param start_time: Начальное время сегмента (в секундах).
    :param end_time: Конечное время сегмента (в секундах).
    :param target_height: Высота кадра для выходного видео.
    :param target_width: Ширина кадра для выходного видео.
    """

    # Открываем видеофайл
    video_capture = cv2.VideoCapture(input_video_path)

    # Получаем информацию о видео
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Вычисляем кадры, соответствующие началу и концу сегмента
    start_frame = int(start_time * fps)
    end_frame = min(int(end_time * fps), total_frames)

    # Перемещаем указатель видео на начальный кадр
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Читаем первый кадр, чтобы получить размеры
    ret, frame = video_capture.read()
    if not ret:
        return

    # Изменяем разрешение до высоты 1280, сохраняя соотношение сторон
    aspect_ratio = frame.shape[1] / resolution[1]
    print('aspect_ratio ',aspect_ratio)
    target_width = int(frame.shape[0] / aspect_ratio)
    # target_hight = int(resolution[1] * aspect_ratio)
    print('target_width ',target_width)
    # print('target_hight ',target_hight)

    # resized_frame = cv2.resize(frame, (target_width, resolution[1]))

    # Создаем VideoWriter для записи выходного видео
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Выбираем кодек (можно использовать другие)
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (target_width, resolution[1]))
    # Записываем измененные и обрезанные кадры в выходное видео
    for frame_num in range(start_frame, end_frame):
        ret, frame = video_capture.read()
        if not ret:
            break
        frame = cv2.resize(frame, (target_width, resolution[1]))

        # Обрезаем кадр до указанной ширины
        crop_start = int((frame.shape[1] - target_width) / 2)
        crop_end = crop_start + target_width
        frame = frame[:, crop_start:crop_end, :]

        video_writer.write(frame)
    print(f'Создан {output_video_path}')

    # Освобождаем ресурсы
    video_capture.release()
    video_writer.release()

def run_timer():
    class Timer:
        def __init__(self):
            self.start_time = None
            self.is_running = False
            self.timestamps = []

        def start_stop_timer(self):
            if not self.is_running:
                print("Таймер запущен")
                self.start_time = time.time()
            else:
                elapsed_time = time.time() - self.start_time
                print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} сек")
            self.is_running = not self.is_running

        def record_timestamp(self):
            if self.is_running:
                elapsed_time = round(time.time() - self.start_time,3)
                self.timestamps.append(elapsed_time)
                print(f"Время: {elapsed_time:.2f} сек")

    timer = Timer()

    keyboard.add_hotkey('space', timer.start_stop_timer)
    mouse.on_click(timer.record_timestamp)

    print("Нажми 'Пробел' чтобы запустить/остановить таймер")
    print("Кликни левой кнопкой мыши, чтобы записать время")

    keyboard.wait('esc')  # Wait for 'Esc' key to exit

    # Save timestamps to a file
    filename = 'timestamps.json'
    with open(filename, 'w') as file:
        json.dump(timer.timestamps, file)

    print(f"Timestamps saved to {filename}.")

def process_json_file(duration=5, json_file='timestamps.json'):
    with open(json_file, 'r') as file:
        json_array = json.load(file)
    result = []
    segment = None
    for start_time_seconds in json_array:
        if type(start_time_seconds) == str:
            tm = start_time_seconds.split(':')
            start_time_seconds = int(tm[0])*60+int(tm[1])
            try:
                segment = int(tm[2])
            except:
                segment = None
        end_time_seconds = start_time_seconds + duration
        result.append((start_time_seconds, round(end_time_seconds,3),segment))

    return result

def main():
    start_time = time.time()

    # create_shorts_ru() 
    # create_shorts_en()


    # download_youtube_video(url='https://www.youtube.com/watch?v=J8lJtgyAcIA') #рабочий вариант
    # run_timer()


    segments = process_json_file()
    name = len(os.listdir('SEGMENTS'))
    for i,segment in enumerate(segments,start=1):
        seg = (segment[0],segment[1])
        new_name = name + i
        VideoEditor.cut_resize_crop(video_path='downloads\\49.mp4',output_path=f'SEGMENTS\\{new_name}.mp4',start_end=seg,part_0_9=segment[2])



    # print(len_simbols(f'{PROJECT_NAME}\\EN\\{PROJECT_NAME}_en.txt'))
    # print(len_simbols(f'{PROJECT_NAME}\\RU\\{PROJECT_NAME}_ru.txt'))

 

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time/60} минут")

    # ImageEditor.get_pexels_images(api_key=key,save_path=f'image\\{PROJECT_NAME}')
  


if __name__ == "__main__":
    main()
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
from audio import AudioEditor
from subtitle import SubtitleEditor
import cv2
import numpy as np
import shutil
import os

class VideoEditor:

    def create_transition(video_files, subtitles_clip=None, overlap = 1, resize = False):
        """
        Parameters
        -----------
        clips_path - path to source first video ``*.MP4``

        subtitles_clip - 

        output_file - path to final video ``*.MP4``

        overlap - transition time in ``seconds``, default ``1s``

        resize - Error ``False`` | crop to min resolution ``True`` (if different resolutions)

        """
        if subtitles_clip:
            final_clip = CompositeVideoClip(video_files + subtitles_clip)
        else:
            files_array = [video_files[0].crossfadeout(overlap),video_files[1].set_start(video_files[0].duration - overlap).crossfadein(overlap)]
            final_clip = CompositeVideoClip(files_array)
        return final_clip

    def combinate(video_path, audio_path, output_path, crop=False):
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        video_durasion = video_clip.duration
        audio_durasion = audio_clip.duration
        video_clip = video_clip.set_audio(audio_clip)
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        video_clip.close()
        audio_clip.close()

    def crop(video_path,  output_path, duration=None, audio_path=None, start_end=None):
        """
        Parameters
        -----------
        video_path - видео файл ``*.MP4``

        output_path - итоговый файл ``*.MP4``

        duration - длительность в ``секундах``, по умолчанию ``60сек``

        """
        video_clip = VideoFileClip(video_path)

        if audio_path and duration or audio_path and start_end or duration and start_end:
            print('Невозможно использовать два параметра одновременно!')
            return

        if audio_path:
            audio_clip = AudioFileClip(audio_path)
            if video_clip.duration>audio_clip.duration:
                trimmed_video = video_clip.subclip(0, audio_clip.duration)
                trimmed_video.write_videofile(output_path, codec='libx264', audio_codec=None)
                video_clip.close()
                trimmed_video.close()
                audio_clip.close()
                return
            else:
                shutil.copy(video_path, output_path)
                return
        
        elif duration:
            if video_clip.duration<=duration:
                print('Обрезка не требуется')
                return
            else:
                cropped_clip = video_clip.subclip(0, duration)
                cropped_clip.write_videofile(output_path, codec='libx264', audio_codec=None)
                video_clip.close()
                cropped_clip.close()
                return
            
        elif start_end:
            start,end = start_end
            if video_clip.duration<=start or video_clip.duration<end:
                print('Параметры start или end некорректны')
                return
            else:
                cropped_clip = video_clip.subclip(start, end)
                cropped_clip.write_videofile(output_path, codec='libx264', audio_codec=None)
                video_clip.close()
                cropped_clip.close()
                return
            
    def chromoKey(input_path, output_path, start_time=50, chromo_path='mrSim_30fps.mp4'):
        lower_green = np.array([40, 50, 50]) # Определение диапазона цветов хромакея (зеленого фона)
        upper_green = np.array([90, 255, 255])
        cap_chromakey = cv2.VideoCapture(chromo_path)
        cap_background = cv2.VideoCapture(input_path)       
        # Определение параметров видео (ширина, высота и частота кадров)
        width = int(cap_chromakey.get(3))
        height = int(cap_chromakey.get(4))
        fps = int(cap_chromakey.get(5))
        frame_count = int(cap_chromakey.get(cv2.CAP_PROP_FRAME_COUNT))
        # Определение кодека и создание объекта VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Используйте 'mp4v' для кодирования в MP4
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        # Определение времени для применения хромакея в секундах
        chromakey_start_time_seconds = start_time  # время начала хромакея в секундах
        # Перевод времени из секунд в кадры
        chromakey_start_frame = int(chromakey_start_time_seconds * fps)
        frame_number = 0
        print('Создаю видео с хромакеем. Ждите...')
        while cap_background.isOpened():
            ret_background, frame_background = cap_background.read()
            if not ret_background:
                break
            # Применение маски к заднему фону
            background_result = frame_background.copy()
            # Случай, когда нужно применить хромакей
            if chromakey_start_frame <= frame_number < chromakey_start_frame + frame_count:
                ret_chromakey, frame_chromakey = cap_chromakey.read()
                if not ret_chromakey:
                    return
                # Преобразование изображения в цветовое пространство HSV
                hsv = cv2.cvtColor(frame_chromakey, cv2.COLOR_BGR2HSV)
                # Создание маски хромакея
                mask = cv2.inRange(hsv, lower_green, upper_green)
                # Инвертирование маски
                inverted_mask = cv2.bitwise_not(mask)
                # Применение инвертированной маски к кадру хромакея
                chromakey_result = cv2.bitwise_and(frame_chromakey, frame_chromakey, mask=inverted_mask)
                # Изменение размеров кадра хромакея
                chromakey_result = cv2.resize(chromakey_result, (width, height))
                # Сложение двух кадров
                result = cv2.addWeighted(chromakey_result, 1, background_result, 1, 0, dtype=cv2.CV_8U)
                # Запись обработанного кадра в видеофайл
                out.write(result)
            else:
                # В этом случае, если время для хромакея еще не наступило
                # или оно уже прошло, просто записываем фоновый кадр
                out.write(background_result)
            frame_number += 1
        cap_chromakey.release()
        cap_background.release()
        out.release()
        cv2.destroyAllWindows()
            
    def change_video_fps(input_video_path, output_video_path, target_fps=30):
        # Открываем видеофайл
        cap = cv2.VideoCapture(input_video_path)

        # Получаем текущее FPS
        current_fps = cap.get(cv2.CAP_PROP_FPS)

        if current_fps != target_fps:

            # Получаем размер кадра
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Создаем объект VideoWriter для записи видео
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Вы можете изменить формат на другой, если нужно
            out = cv2.VideoWriter(output_video_path, fourcc, target_fps, (frame_width, frame_height))

            # Читаем кадры из видео и записываем их с новым FPS
            while True:
                ret, frame = cap.read()

                if not ret:
                    break

                # Записываем кадр в выходное видео
                out.write(frame)

            # Закрываем видеофайлы
            cap.release()
            out.release()

            print(f"Видео успешно создано с целевым FPS: {target_fps}")
        else:
            print(f"FPS в норме!")

    def segment_video(input_file, output_file, start_time, end_time):
        cap = cv2.VideoCapture(input_file)

        # Получаем информацию о видео
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Вычисляем кадры для начала и конца сегмента
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)

        # Проверяем, что конечный кадр не превышает общее количество кадров
        end_frame = min(end_frame, total_frames - 1)

        # Устанавливаем указатель видео на начальный кадр
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        # Создаем объект VideoWriter для записи сегмента
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

        # Считываем и записываем кадры в сегмент
        for frame_number in range(start_frame, end_frame + 1):
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break

        # Закрываем видеофайлы
        cap.release()
        out.release()

        print(f"Создан {output_file}")

    def crop_resolution(input_file, output_file, target_resolution=(720, 1280)):
        # Load the video clip
        video_clip = VideoFileClip(input_file)
        w,h = video_clip.size

        # Trim the video
        x1 = int((w-target_resolution[0])/2)
        y1 = int((h-target_resolution[1])/2)
        # Resize the video
        resized_clip = video_clip.crop(x1=x1, y1=y1, x2=target_resolution[0]+x1, y2=target_resolution[1]+y1)

        # Write the result to a file
        resized_clip.write_videofile(output_file, codec="libx264", audio_codec=None)

        # Close the clips
        video_clip.close()
        resized_clip.close()
        print(f"Создан {output_file}")

    def change_resolution(input_video, output_video, new_resolution):
        # Load the video
        clip = VideoFileClip(input_video)
        w,h=clip.size

        i = h/new_resolution[1]
        resolution = (int(w/i), new_resolution[1])

        # Change the resolution
        new_clip = clip.resize(newsize=resolution)

        # Save the modified video
        new_clip.write_videofile(output_video, codec="libx264", audio_codec=None)

    def cut_resize_crop(video_path,output_path,start_end=None,target_resolution=(720,1280), part_0_9 = None):
        try:
            video_clip = VideoFileClip(video_path)
            w,h=video_clip.size
            if target_resolution!=video_clip.size:
                if h>=target_resolution[1]:
                    i = h/target_resolution[1]
                    target_width = int(w/i)
                    w_part = target_width/10
                    resolution = (target_width, target_resolution[1])
                   
                    if part_0_9 == None:
                        x1 = int((resolution[0]-target_resolution[0])/2)
                        y1 = int((resolution[1]-target_resolution[1])/2)
                        x2 = x1 + target_resolution[0]
                        y2 = y1 + target_resolution[1]
                    else:
                        x1 = w_part*part_0_9
                        y1 = int((resolution[1]-target_resolution[1])/2)
                        x2 = x1 + target_resolution[0]
                        y2 = y1 + target_resolution[1]
                        if part_0_9 == 0:
                            x1,x2,y1,y2 = (0,target_resolution[0],0,target_resolution[1])
                        elif part_0_9 == 9:
                            x1,x2,y1,y2 = (target_width-target_resolution[0],target_width,0,target_resolution[1])

                    cropped_clip = video_clip
                    if start_end != None:
                        start,end = start_end
                        cropped_clip = video_clip.subclip(start, end)

                    res_clip = cropped_clip.resize(newsize=resolution)
                    resized_clip = res_clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
                    resized_clip.write_videofile(output_path, fps = 30, codec='libx264', audio_codec=None, audio=False)
                    video_clip.close()
                    cropped_clip.close()
                    res_clip.close()
                    resized_clip.close()
                    print(f'Создано {output_path}')
                else:
                    print('Разрешение слишком мало!')
            else:
                print('Преобразование не требуется')
        except Exception as e:
            print(f'Ошибка: {e}')

        

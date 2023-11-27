# import soundfile as sf
# import scipy.io.wavfile as wav
# from mutagen.mp3 import MP3 
# import tempfile
# import moviepy
# import speech_recognition as sr
# from moviepy.video.tools.subtitles import file_to_subtitles
# from pydub.silence import split_on_silence
# from googletrans import Translator
# from moviepy.editor import concatenate_audioclips
# import vosk
# import json
# import wave
# import sys
# import librosa.display
import matplotlib.pyplot as plt
# import librosa
import requests
# from PIL import Image
import imageio 
import os 
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
import numpy
import imageio
from elevenlabs import generate, save, set_api_key
import moviepy.editor as mp
from pydub import AudioSegment
import pysrt
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


# set_api_key(os.environ.get("ELEVEN_KEY"))
# deepgramapiKey=set_api_key(os.environ.get("DEEPGRAM_API_KEY"))

# def crop_image(input_path, output_path, resolution = (720, 1280)):
#     original_image = Image.open(input_path).crop()
#     target_width, target_height = resolution
#     if original_image.width >= target_width and original_image.height >= target_height:
#         crop_box = ((original_image.width - target_width) // 2, (original_image.height - target_height) // 2,
#                         (original_image.width + target_width) // 2, (original_image.height + target_height) // 2)
#         cropped_image = original_image.crop(crop_box)
#         cropped_image.save(output_path)
#         print(f"Image cropped ({cropped_image.width} {cropped_image.height}) and saved to {output_path}")
#         return
#     else:
#         print(f"Image resolution ({original_image.width}x{original_image.height}) is less than {target_width}x{target_height}.")

# def ken_burns_effect_video(image_path, output_path, duration=10, zoom_factor=1.4, reverse=False, fps=30):
#     img = Image.open(image_path)
#     new_width = (img.width // 16) * 16
#     new_height = (img.height // 16) * 16
#     img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
#     frames = []
#     long = duration * fps
#     for i in range(long):
#         current_zoom = 1 + (zoom_factor - 1) * i / long
#         position = (
#             (img.width - img.width * current_zoom) / 2,
#             (img.height - img.height * current_zoom) / 2
#         )
#         frame = img.resize((int(img.width * current_zoom), int(img.height * current_zoom)), Image.Resampling.LANCZOS)
#         canvas = Image.new("RGB", img.size, "black")
#         canvas.paste(frame, box=(int(position[0]), int(position[1])))
#         frames.append(canvas)
#     if reverse:
#         frames = frames[::-1]
#     with imageio.get_writer(output_path, fps=fps) as writer:
#         for frame in frames:
#             frame_array = numpy.array(frame)
#             writer.append_data(frame_array)
#     print(f'{output_path} video file created')

# def create_transition(clip1_path, clip2_path, output_file = 'output_video.mp4', overlap = 1, resize = False):
#     clip1 = mp.VideoFileClip(clip1_path)
#     clip2 = mp.VideoFileClip(clip2_path)
#     if clip1.size!=clip2.size:
#         if resize:
#             common_height = min(clip1.size[1], clip2.size[1])
#             clip1 = clip1.resize(height=common_height)
#             clip2 = clip2.resize(height=common_height)
#         else:
#             print("Warning: The incoming videos have different resolutions.")
#             return
#     final_clip = mp.CompositeVideoClip([clip1.crossfadeout(overlap), clip2.set_start(clip1.duration - overlap).crossfadein(overlap)])
#     final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
#     final_clip.close()

# def voice(voice="Fin", output_file = 'out.wav', text=''):
#     audio = generate(
#     text=text,
#     voice = voice,
#     model="eleven_multilingual_v2"
#     )
#     save(audio, output_file)

# def combinate(video_path, audio_path, output_path = 'video_with_voice.mp4', crop=False):
#     video_clip = mp.VideoFileClip(video_path)
#     audio_clip = mp.AudioFileClip(audio_path)
#     video_durasion = video_clip.duration
#     audio_durasion = audio_clip.duration
#     # if video_durasion!=audio_durasion:
#     #     print('Files have different durations!')
#     #     if crop and video_durasion>audio_durasion:
#     #         trimmed_video = video_clip.subclip(0, audio_durasion)
#     #         trimmed_video = trimmed_video.set_audio(audio_clip)
#     #         trimmed_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
#     #         video_clip.close()
#     #         trimmed_video.close()
#     #         audio_clip.close()
#     #         return
#     #     if crop and video_durasion<audio_durasion:
#     #         trimmed_audio = audio_clip.subclip(0, video_durasion)
#     #         video_clip = video_clip.set_audio(trimmed_audio)
#     #         video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
#     #         audio_clip.close()
#     #         trimmed_audio.close()
#     #         video_clip.close()
#     #         return
#     # else:
#     video_clip = video_clip.set_audio(audio_clip)
#     video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
#     video_clip.close()
#     audio_clip.close()

# def change_speed(input_path, output_path, format = 'wav', speed = 1.07):
#     sound = AudioSegment.from_file(input_path)
#     so = sound.speedup(playback_speed = speed)
#     so.export(output_path, format = format)

# def subtitle_generator():
#     # Замените этот список субтитрами вашими значениями
#     subtitles = [(0, 5, "Привет, это субтитр 1."),
#                  (7, 12, "Это субтитр 2."),
#                  (15, 20, "И это субтитр 3.")]
#     change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
#     generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=60, color='white')
#     video_clip = mp.VideoFileClip("video\\2_tr.mp4")
#     subtitles = SubtitlesClip('subtitles.srt', generator)
#     subtitles = subtitles.set_pos(('center', 'center'))
#     video_with_subtitles = mp.CompositeVideoClip([video_clip, subtitles])
#     video_with_subtitles.write_videofile("video\\final_sub.mp4", codec="libx264", audio_codec="aac")


# def textclip():
#     subtitles = [(0, 5, "Привет, это субтитр 1."),
#                  (7, 12, "Это субтитр 2."),
#                  (15, 20, "И это субтитр 3.")]
#     change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
#     video_clip = mp.VideoFileClip("video\\2_tr.mp4")
#     text_clip = TextClip('subtitles', fontsize=80, color='white',font='Georgia-Regular')
#     text_clip = text_clip.set_duration(video_clip.duration)
#     video_with_text = mp.CompositeVideoClip([video_clip, text_clip.set_pos(('center', 'center'))])
#     video_with_text.write_videofile("video\\final_sub.mp4", codec="libx264", audio_codec="aac")

# def audio_to_subtitle_v3(audio_file_path, output_subtitle_path, language='ru'):
#     vosk_model_path = "C:\\Users\sansej\\AppData\\Roaming\\Python\\Python312\\site-packages\\vosk-model-ru-0.42"
#     vosk_model = vosk.Model(vosk_model_path)
#     audio = AudioSegment.from_file(audio_file_path)
#     temp_wav_path = "temp.wav"
#     audio.export(temp_wav_path, format="wav")
#     with wave.open(temp_wav_path, 'rb') as wf:
#         sample_rate = wf.getframerate()
#         recognizer = vosk.KaldiRecognizer(vosk_model, sample_rate)
#     with open(temp_wav_path, 'rb') as audio_file:
#         audio_data = audio_file.read()
#         recognizer.AcceptWaveform(audio_data)
#     result = json.loads(recognizer.FinalResult())
#     recognized_text = result['text']
#     subtitles = [(0, len(recognized_text.split()), recognized_text)]
#     srt_content = create_srt(subtitles)
#     with open(output_subtitle_path, "w", encoding="utf-8") as file:
#         file.write(srt_content)
#     os.remove(temp_wav_path)

# def create_srt(subtitles):
#     srt_content = ""
#     for i, (start_time, end_time, text) in enumerate(subtitles, start=1):
#         srt_content += f"{i}\n{format_time(start_time)} --> {format_time(end_time)}\n{text}\n\n"
#     return srt_content

# def format_time(milliseconds):
#     seconds, milliseconds = divmod(milliseconds, 1000)
#     minutes, seconds = divmod(seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def convert_to_srt(data, output_filename):
    def format_time(seconds):
        # Convert seconds to hours, minutes, seconds, milliseconds format
        hours, remainder = divmod(seconds, 3600)
        print(hours, remainder)
        minutes, remainder = divmod(remainder, 60)
        print(minutes, remainder)
        seconds, milliseconds = divmod(remainder, 1)
        print(seconds, milliseconds)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(milliseconds*1000):03d}"

    with open(output_filename, 'w', encoding='UTF-8') as f:
        for i, entry in enumerate(data, start=1):
            start_time = format_time(entry['start'])
            print(start_time)
            end_time = format_time(entry['end'])
            print(end_time)
            subtitle_text = entry['punctuated_word']
            print(subtitle_text)
            f.write(f"{i}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{subtitle_text}\n\n")

# def getDeepgramTranscription(p_url):
#     url = "https://api.deepgram.com/v1/listen?smart_format=true&language=ru&model=whisper-medium"
#     payload = {
#         "url": p_url
#     }
#     headers = {
#         "Authorization": 'Token ' + str(deepgramapiKey),
#         "content-type": "application/json"
#     }
#     response = requests.request("POST", url, headers=headers, json=payload)
#     output = response.json()
#     print(output)
#     return output

def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000


def create_subtitle_clips(subtitles, videosize,fontsize=80, font='Arial', color='yellow', debug = False):
    subtitle_clips = []
    change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time
        video_width, video_height = videosize
        text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color,size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = 'center'
        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.set_position(text_position))
    return subtitle_clips

# def mfccs():
#     audio_path = 'out.wav'
#     audio_signal, sampling_rate = librosa.load(audio_path)
#     mfccs = librosa.feature.mfcc(y=audio_signal, sr=sampling_rate)
#     print(mfccs)

def detect_audio_segments(audio_file_path, silence_threshold=-40, min_silence_duration=1000):
    # Загрузка аудиофайла
    audio = AudioSegment.from_file(audio_file_path)

    # Преобразование в numpy array для удобства работы
    audio_array = numpy.array(audio.get_array_of_samples())

    # Определение отрезков с звуком
    sound_segments = []
    is_sound = False
    start_time = 0

    for i, sample in enumerate(audio_array):
        if sample > silence_threshold:
            if not is_sound:
                start_time = i
                is_sound = True
        else:
            if is_sound:
                end_time = i
                is_sound = False
                duration = end_time - start_time
                if duration > min_silence_duration:
                    start_time_sec = start_time / audio.frame_rate
                    end_time_sec = end_time / audio.frame_rate
                    start_time_formatted = format_seconds(start_time_sec)
                    end_time_formatted = format_seconds(end_time_sec)
                    sound_segments.append((start_time_formatted, end_time_formatted))

    return sound_segments

def format_seconds(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    microseconds = int((seconds % 1) * 1e6)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{microseconds:06d}"

# def segment_audio_by_threshold(audio_signal, threshold=0.05, min_segment_length=1000):
#     """
#     Сегментация аудиосигнала на отдельные сегменты на основе пороговой обработки.
    
#     Параметры:
#     - audio_signal: массив значений аудиосигнала
#     - threshold: пороговое значение для определения паузы
#     - min_segment_length: минимальная длина сегмента, чтобы исключить короткие шумовые периоды
    
#     Возвращает:
#     - segments: список кортежей, представляющих сегменты (начальный индекс, конечный индекс)
#     """
#     above_threshold = audio_signal > threshold
#     segment_starts = numpy.where(numpy.diff(above_threshold.astype(int)) == 1)[0]
#     segment_ends = numpy.where(numpy.diff(above_threshold.astype(int)) == -1)[0]

#     # Удаление коротких сегментов
#     valid_segments = [(start, end) for start, end in zip(segment_starts, segment_ends) if end - start > min_segment_length]

#     return valid_segments

# def to_normalized_array(audio_chunk, fs, librosa_fs):
#    samples = audio_chunk.get_array_of_samples()
#    arr = numpy.array(samples).astype(numpy.float32) / numpy.iinfo(numpy.int16).max
#    return librosa.core.resample(arr, fs, librosa_fs)

def segment_audio_by_threshold(audio_signal, threshold=0.05, min_segment_length=1000):
    above_threshold = audio_signal > threshold
    segment_starts = numpy.where(numpy.diff(above_threshold.astype(int)) == 1)[0]
    segment_ends = numpy.where(numpy.diff(above_threshold.astype(int)) == -1)[0]

    # Удаление коротких сегментов
    valid_segments = [(start, end) for start, end in zip(segment_starts, segment_ends) if end - start > min_segment_length]

    return valid_segments

def srt_format_time(segment):
    start_time = int(segment[0])
    end_time = int(segment[1])

    start_hours, start_remainder = divmod(start_time, 3600)
    start_minutes, start_seconds = divmod(start_remainder, 60)
    start_seconds, start_microseconds = divmod(int((start_seconds - int(start_seconds)) * 1e6), 1e6)

    end_hours, end_remainder = divmod(end_time, 3600)
    end_minutes, end_seconds = divmod(end_remainder, 60)
    end_seconds, end_microseconds = divmod(int((end_seconds - int(end_seconds)) * 1e6), 1e6)

    formatted_time = "{:02d}:{:02d}:{:02d},{:06d} - {:02d}:{:02d}:{:02d},{:06d}".format(
        start_hours, start_minutes, int(start_seconds), int(start_microseconds),
        end_hours, end_minutes, int(end_seconds), int(end_microseconds)
    )

    return formatted_time

def main():
    # crop_image(input_path='ntc.jpg', output_path='crop_ntc.jpg')
    # crop_image(input_path='wosp.jpg', output_path='crop_wosp.jpg')
    # ken_burns_effect_video(image_path='crop_ntc.jpg', output_path='crop_ntc.mp4', duration=5)
    # ken_burns_effect_video(image_path='crop_wosp.jpg', output_path='crop_wosp.mp4', duration=5)
    # create_transition(clip1_path='crop_ntc.mp4', clip2_path='crop_wosp.mp4')
    text = '''Юпи́тер – самая крупная планета в Солнечной системе. Её масса в 318 раз больше массы Земли,
    а объем в 1300 раз больше. Если бы Юпи́тер был ещё чуть-чуть массивнее, он мог бы стать звездой,
    так как в его ядре происходит процесс термоядерного синтеза, подобный тому, что происходит в звёздах.
    На Юпи́тере есть впечатляющее магнитное поле, превосходящее магнитное поле любой другой планеты
    в Солнечной системе. Это поле создает мощные радиальные лучи, наблюдаемые в районе полюсов. Эти
    светящиеся лучи делают Юпи́тер еще более удивительным объектом для наблюдения. У Юпи́тера более 80
    известных спутников. Самый известный из них – Ганимед, самый крупный спутник в Солнечной системе.
    Ещё один известный спутник Юпи́тера – Ио – известен своими вулканическими извержениями и
    ярко-красными пя́тнами на поверхности.'''
    # voice(text=text)
    # change_speed(input_path='out.wav', output_path='final.wav')
    # combinate(video_path='video\\9_tr.mp4', audio_path='final.wav',output_path='video\\final.mp4')
    # subtitle_generator()
    # textclip()
    # create_srt()

    # Example usage
    # audio_file_path = "final.wav"  # Replace with your audio file path
    # output_subtitle_path = "output.srt"  # Replace with your desired output subtitle file path
    # audio_to_subtitle_v3(audio_file_path, output_subtitle_path)

    count = 1
    folder_image = 'image'
    folter_image_crop = 'image_crop'
    folder_video = 'video'
    folder_transition = 'transition'
    # for file in os.listdir(folder_image):
    #     if file.endswith(".jpg") or file.endswith(".png"):
    #         crop_image(input_path=f'{folder_image}\\{file}', output_path=f'{folter_image_crop}\\{count}.jpg')
    #         count += 1

    # count = 1
    # for file in os.listdir(folter_image_crop):
    #     if count%3!=0:
    #         rev = False
    #     else:
    #         rev = True
    #     ken_burns_effect_video(image_path=f'{folter_image_crop}\\{file}', output_path=f'{folder_video}\\{count}.mp4', duration=7, reverse=rev)
    #     count += 1

    # count = 1
    # file_name = ''
    # for file in os.listdir(folder_video):
    #     if count==1:
    #         file_name = file
    #     else:
    #         create_transition(clip1_path=f'{folder_video}\\{file_name}', clip2_path=f'{folder_video}\\{file}',output_file=f'{folder_video}\\{count}_tr.mp4',overlap=0.75)
    #         file_name = f'{count}_tr.mp4'
    #     count += 1

    # srtfilename = "sub.srt"
    # mp4filename = "video_with_voice.mp4"
    # video = VideoFileClip(mp4filename)
    # subtitles = pysrt.open(srtfilename)
    # begin,end= mp4filename.split(".mp4")
    # output_video_file = begin+'_sub'+".mp4"
    # print ("Output file name: ",output_video_file)
    # subtitle_clips = create_subtitle_clips(subtitles,video.size)
    # final_video = CompositeVideoClip([video] + subtitle_clips)
    # final_video.write_videofile(output_video_file)

    # mp3url = "https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav"
    # # print(output)
    # subtitle_data = output['results']['channels'][0]['alternatives'][0]['words']
    # filename = os.path.basename(mp3url)
    # name, extension = os.path.splitext(filename)
    # output_filename = name + ".srt"
    # convert_to_srt(subtitle_data,output_filename)

    # mfccs()

    # # Пример использования
    # audio_path = 'out.wav'
    # audio_signal, sampling_rate = librosa.load(audio_path)
    # # Применение пороговой обработки
    # threshold = 0.1
    # min_segment_length = 25
    # segments = segment_audio_by_threshold(audio_signal, threshold, min_segment_length)
    # # Вывод результатов
    # for start, end in segments:
    #     print(f"Сегмент: {start} - {end} (Длительность: {end - start} сэмплов)")


    # data_array = [
    #     [0.16253968, 0.60371882],
    #     [1.04489796, 1.4860771],
    #     [1.50929705, 2.78639456],
    #     [2.83283447, 3.4829932],
    #     [3.50621315, 3.64553288],
    #     [3.71519274, 4.01705215],
    #     [4.06349206, 5.24770975],
    #     [5.4799093, 5.64244898],
    #     [5.71210884, 6.01396825],
    #     [6.08362812, 6.29260771],
    #     [6.31582766, 7.70902494]
    # ]

    # # Преобразование массива
    # formatted_times = [srt_format_time(segment) for segment in data_array]

    # # Вывод результатов
    # for i, time in enumerate(formatted_times, start=1):
    #     print("Segment {}: {}".format(i, time))

    # value = 57.70902494
    # seconds, microseconds = divmod(int(value * 1e6), 1e6)
    # hours, remainder = divmod(seconds, 3600)
    # minutes, seconds = divmod(remainder, 60)
    # formatted_time = "{:02d}:{:02d}:{:02d},{:06d}".format(
    #     int(hours), int(minutes), int(seconds), int(microseconds)
    # )
    # print("Formatted time: {}".format(formatted_time))

    # Пример использования
    audio_file_path = 'final.wav'
    segments = detect_audio_segments(audio_file_path)

    print("Отрезки с звуком:")
    for segment in segments:
        print(f"Начало: {segment[0]}, Конец: {segment[1]}")



if __name__ == "__main__":
    main()
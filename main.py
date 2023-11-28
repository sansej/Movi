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
# import unicodedata
# import math
from audio import AudioEditor
# import matplotlib.pyplot as plt
# import librosa
# import requests
# from PIL import Image
# import imageio 
# from subtitle import SubtitleEditor
# import os 
# from moviepy.video.tools.subtitles import SubtitlesClip
# from moviepy.config import change_settings
import numpy
# import imageio
# from elevenlabs import generate, save, set_api_key
# import moviepy.editor as mp
# from pydub import AudioSegment
# import pysrt
# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


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

    AudioEditor.to_subtitle_file(audio_file_path='crop.mp3', subtitle_file='sub.srt', text=text)
    # a = SubtitleEditor.split_text(text, 64)
    # print(a)

    

if __name__ == "__main__":
    main()
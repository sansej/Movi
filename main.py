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
from subtitle import SubtitleEditor
from video import VideoEditor
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
import moviepy.editor as mp
# from pydub import AudioSegment
import pysrt
from moviepy.editor import VideoFileClip, CompositeVideoClip, AudioFileClip, concatenate_videoclips


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

    # text = 'Привет! Сегодня расскажу об очень интерестном и прекрасном явлении, таком как северное сияние.'
    # VideoEditor.combinate(video_path="output_video.mp4", audio_path='crop.mp3', output_path= 'video_with_crop_mp3.mp4')
    # video1 = mp.VideoFileClip("video_with_crop_mp3.mp4")
    # sub = AudioEditor.to_subtitle(audio_file_path='crop.mp3', text=text)
    # sub_clip = SubtitleEditor.create_subtitle_clips(sub,video1.size,fontsize=70,background='black')
    # final_video = mp.CompositeVideoClip([video1] + sub_clip)
    # final_video.write_videofile('output_video_file_crop_mp3.mp4')

    

    # def create_composite_video(video_clips, subtitles_clip, audio_file, transition_duration=1):

    #     # Загрузка аудио файла
    #     audio = AudioFileClip(audio_file)

    #     # Создание списка видео с переходами
    #     clips_with_transitions = []
    #     for idx, clip in enumerate(video_clips):
    #         if idx > 0:
    #             transition_clip = concatenate_videoclips([clips_with_transitions[-1], clip.set_start(clip.duration - transition_duration)], method="compose", crossfade=transition_duration)
    #             clips_with_transitions[-1] = transition_clip
    #         clips_with_transitions.append(clip)

    #     # Создание CompositeVideoClip
    #     composite_clip = CompositeVideoClip(clips_with_transitions, subtitles=subtitles_clip, audio=audio)

    #     return composite_clip

    

    text = 'Привет! Сегодня расскажу об очень интерестном и прекрасном явлении, таком как северное сияние.'
    audio_file = "out.wav"
    video_clips_tuple = ("out.mp4", "out1.mp4", "out2.mp4")
    print([VideoFileClip(file) for file in video_clips_tuple])
    video = "output_video_file.mp4"
    final_video = "final_video.mp4"
    video_clips = [VideoFileClip(file) for file in video_clips_tuple]


    sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
    sub_clip = SubtitleEditor.create_subtitle_clips(sub,video_clips[0].size,fontsize=70,background='black')

    result_clip = VideoEditor.create_transition(video_clips, sub_clip)

    result_clip.write_videofile(video, codec="libx264", audio_codec="aac")

    VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=final_video)


    

if __name__ == "__main__":
    main()
from mutagen.mp3 import MP3 
from PIL import Image
import imageio 
import os 
import tempfile
import json
import vosk
import wave
from pydub.silence import split_on_silence
from googletrans import Translator
from moviepy.editor import concatenate_audioclips
from moviepy.editor import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.tools.subtitles import file_to_subtitles
from moviepy.config import change_settings
import moviepy
import speech_recognition as sr
import numpy
import imageio
from elevenlabs import generate, save, set_api_key
import moviepy.editor as mp
from pydub import AudioSegment, effects
import soundfile as sf
import scipy.io.wavfile as wav
set_api_key(os.environ.get("ELEVEN_KEY"))

def crop_image(input_path, output_path, resolution = (720, 1280)):
    original_image = Image.open(input_path).crop()
    target_width, target_height = resolution
    if original_image.width >= target_width and original_image.height >= target_height:
        crop_box = ((original_image.width - target_width) // 2, (original_image.height - target_height) // 2,
                        (original_image.width + target_width) // 2, (original_image.height + target_height) // 2)
        cropped_image = original_image.crop(crop_box)
        cropped_image.save(output_path)
        print(f"Image cropped ({cropped_image.width} {cropped_image.height}) and saved to {output_path}")
        return
    else:
        print(f"Image resolution ({original_image.width}x{original_image.height}) is less than {target_width}x{target_height}.")

def ken_burns_effect_video(image_path, output_path, duration=10, zoom_factor=1.4, reverse=False, fps=30):
    img = Image.open(image_path)
    new_width = (img.width // 16) * 16
    new_height = (img.height // 16) * 16
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    frames = []
    long = duration * fps
    for i in range(long):
        current_zoom = 1 + (zoom_factor - 1) * i / long
        position = (
            (img.width - img.width * current_zoom) / 2,
            (img.height - img.height * current_zoom) / 2
        )
        frame = img.resize((int(img.width * current_zoom), int(img.height * current_zoom)), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", img.size, "black")
        canvas.paste(frame, box=(int(position[0]), int(position[1])))
        frames.append(canvas)
    if reverse:
        frames = frames[::-1]
    with imageio.get_writer(output_path, fps=fps) as writer:
        for frame in frames:
            frame_array = numpy.array(frame)
            writer.append_data(frame_array)
    print(f'{output_path} video file created')

def create_transition(clip1_path, clip2_path, output_file = 'output_video.mp4', overlap = 1, resize = False):
    clip1 = mp.VideoFileClip(clip1_path)
    clip2 = mp.VideoFileClip(clip2_path)
    if clip1.size!=clip2.size:
        if resize:
            common_height = min(clip1.size[1], clip2.size[1])
            clip1 = clip1.resize(height=common_height)
            clip2 = clip2.resize(height=common_height)
        else:
            print("Warning: The incoming videos have different resolutions.")
            return
    final_clip = mp.CompositeVideoClip([clip1.crossfadeout(overlap), clip2.set_start(clip1.duration - overlap).crossfadein(overlap)])
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
    final_clip.close()

def voice(voice="Fin", output_file = 'out.wav', text=''):
    audio = generate(
    text=text,
    voice = voice,
    model="eleven_multilingual_v2"
    )
    save(audio, output_file)

def combinate(video_path, audio_path, output_path = 'video_with_voice.mp4', crop=False):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = mp.AudioFileClip(audio_path)
    video_durasion = video_clip.duration
    audio_durasion = audio_clip.duration
    # if video_durasion!=audio_durasion:
    #     print('Files have different durations!')
    #     if crop and video_durasion>audio_durasion:
    #         trimmed_video = video_clip.subclip(0, audio_durasion)
    #         trimmed_video = trimmed_video.set_audio(audio_clip)
    #         trimmed_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
    #         video_clip.close()
    #         trimmed_video.close()
    #         audio_clip.close()
    #         return
    #     if crop and video_durasion<audio_durasion:
    #         trimmed_audio = audio_clip.subclip(0, video_durasion)
    #         video_clip = video_clip.set_audio(trimmed_audio)
    #         video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    #         audio_clip.close()
    #         trimmed_audio.close()
    #         video_clip.close()
    #         return
    # else:
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
    audio_clip.close()

def change_speed(input_path, output_path, format = 'wav', speed = 1.07):
    sound = AudioSegment.from_file(input_path)
    so = sound.speedup(playback_speed = speed)
    so.export(output_path, format = format)

def subtitle_generator():
    # Замените этот список субтитрами вашими значениями
    subtitles = [(0, 5, "Привет, это субтитр 1."),
                 (7, 12, "Это субтитр 2."),
                 (15, 20, "И это субтитр 3.")]
    change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
    generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=60, color='white')
    video_clip = mp.VideoFileClip("video\\2_tr.mp4")
    subtitles = SubtitlesClip('subtitles.srt', generator)
    subtitles = subtitles.set_pos(('center', 'center'))
    video_with_subtitles = mp.CompositeVideoClip([video_clip, subtitles])
    video_with_subtitles.write_videofile("video\\final_sub.mp4", codec="libx264", audio_codec="aac")


def textclip():
    subtitles = [(0, 5, "Привет, это субтитр 1."),
                 (7, 12, "Это субтитр 2."),
                 (15, 20, "И это субтитр 3.")]
    change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
    video_clip = mp.VideoFileClip("video\\2_tr.mp4")
    text_clip = TextClip('subtitles', fontsize=80, color='white',font='Georgia-Regular')
    text_clip = text_clip.set_duration(video_clip.duration)
    video_with_text = mp.CompositeVideoClip([video_clip, text_clip.set_pos(('center', 'center'))])
    video_with_text.write_videofile("video\\final_sub.mp4", codec="libx264", audio_codec="aac")

def audio_to_subtitle_v3(audio_file_path, output_subtitle_path, language='ru'):
    vosk_model_path = "C:\\Users\sansej\\AppData\\Roaming\\Python\\Python312\\site-packages\\vosk-model-ru-0.42"
    vosk_model = vosk.Model(vosk_model_path)
    audio = AudioSegment.from_file(audio_file_path)
    temp_wav_path = "temp.wav"
    audio.export(temp_wav_path, format="wav")
    with wave.open(temp_wav_path, 'rb') as wf:
        sample_rate = wf.getframerate()
        recognizer = vosk.KaldiRecognizer(vosk_model, sample_rate)
    with open(temp_wav_path, 'rb') as audio_file:
        audio_data = audio_file.read()
        recognizer.AcceptWaveform(audio_data)
    result = json.loads(recognizer.FinalResult())
    recognized_text = result['text']
    subtitles = [(0, len(recognized_text.split()), recognized_text)]
    srt_content = create_srt(subtitles)
    with open(output_subtitle_path, "w", encoding="utf-8") as file:
        file.write(srt_content)
    os.remove(temp_wav_path)

def create_srt(subtitles):
    srt_content = ""
    for i, (start_time, end_time, text) in enumerate(subtitles, start=1):
        srt_content += f"{i}\n{format_time(start_time)} --> {format_time(end_time)}\n{text}\n\n"
    return srt_content

def format_time(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

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
    textclip()
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


if __name__ == "__main__":
    main()
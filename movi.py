from mutagen.mp3 import MP3 
from PIL import Image
import imageio 
import os 
from moviepy.editor import concatenate_audioclips
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

def ken_burns_effect_video(image_path, output_path, duration=10, zoom_factor=1.3, reverse=False, fps=30):
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
    if video_durasion!=audio_durasion:
        print('Files have different durations!')
        if crop and video_durasion>audio_durasion:
            trimmed_video = video_clip.subclip(0, audio_durasion)
            trimmed_video = trimmed_video.set_audio(audio_clip)
            trimmed_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
            video_clip.close()
            trimmed_video.close()
            audio_clip.close()
            return
        if crop and video_durasion<audio_durasion:
            trimmed_audio = audio_clip.subclip(0, video_durasion)
            video_clip = video_clip.set_audio(trimmed_audio)
            video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
            audio_clip.close()
            trimmed_audio.close()
            video_clip.close()
            return
    else:
        video_clip = video_clip.set_audio(audio_clip)
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        video_clip.close()
        audio_clip.close()

def change_speed(input_path, output_path, format = 'wav', speed = 1.1):
    sound = AudioSegment.from_file(input_path)
    so = sound.speedup(playback_speed = speed)
    so.export(output_path, format = format)

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
    # combinate(video_path='output_video.mp4', audio_path='out.wav', crop=True)


if __name__ == "__main__":
    main()
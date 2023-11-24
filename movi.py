from mutagen.mp3 import MP3 
from PIL import Image
import imageio 
from moviepy import editor 
import os 
from moviepy.editor import *
import numpy
import imageio
from elevenlabs import generate, save
import moviepy.editor as mp
from elevenlabs import set_api_key
set_api_key("4a8b6658597f8c6d47d47674afc89e56")
key = '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'
import openai

def create_movi():
    audio_path = os.path.join(os.getcwd(), "audio\\audio.mp3") 
    video_path = os.path.join(os.getcwd(), "videos") 
    images_path = os.path.join(os.getcwd(), "images\\giphy")
    audio = MP3(audio_path) 
    audio_length = audio.info.length 
    list_of_images = [] 
    for image_file in os.listdir(images_path): 
        if image_file.endswith('.png') or image_file.endswith('.jpg'): 
            image_path = os.path.join(images_path, image_file) 
            image = Image.open(image_path).resize((400, 400), Image.ANTIALIAS) 
            list_of_images.append(image) 
    duration = audio_length/len(list_of_images) 
    imageio.mimsave('images.gif', list_of_images, fps=1/duration)
    video = editor.VideoFileClip("images.gif") 
    audio = editor.AudioFileClip(audio_path) 
    final_video = video.set_audio(audio) 
    os.chdir(video_path) 
    final_video.write_videofile(fps=60, codec="libx264", filename="video.mp4") 

def rescale_video():
    clip = VideoFileClip("videos\\video.mp4")
    clip1 = clip.subclip(0, 7)
    w1 = clip1.w
    h1 = clip1.h
    print("Width x Height of clip 1 : ", end = " ")
    print(str(w1) + " x ", str(h1))
    print("---------------------------------------")
    clip2 = clip1.resize(0.5)
    w2 = clip2.w
    h2 = clip2.h
    print("Width x Height of clip 2 : ", end = " ")
    print(str(w2) + " x ", str(h2))
    print("---------------------------------------")
    clip2.ipython_display()

def crop_image(input_path = 'logo.jpg', output_path = 'croplogo.jpg'):
    original_image = Image.open(input_path).crop()
    resolutions = [(1080, 1920), (720, 1280)]
    for resolution in resolutions:
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
    print("The image is not suitable for cropping to the specified resolutions.")

def ken_burns_effect_video(image_path = 'crop.jpg', output_path = 'out.mp4', duration=10, zoom_factor=1.3, reverse=True, fps=30):
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

def create_transition(clip1_path = 'outlogo.mp4', clip2_path = 'out.mp4', output_file = 'output_video.mp4', overlap = 1, resize = True):
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
    final_clip = CompositeVideoClip([clip1.crossfadeout(overlap), clip2.set_start(clip1.duration - overlap).crossfadein(overlap)])
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
    final_clip.close()

def voice(voice="Fin", output_file = 'out.wav', text="Привет, сегодня раскажу об очень интерестном и прекрасном явлении, таком как северное сияние!"):
    audio = generate(
    text=text,
    voice = voice,
    model="eleven_multilingual_v2"
    )
    save(audio, output_file)

def combinate(video_path = 'output_video.mp4', audio_path = 'out.wav', output_path = 'video_with_voice.mp4'):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = mp.AudioFileClip(audio_path)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
    audio_clip.close()

def chatGPT():
    client = openai.OpenAI()
    openai.api_key = key
    # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
    # if you saved the key under a different environment variable name, you can do something like:
    # client = OpenAI(
    #   api_key=os.environ.get("CUSTOM_ENV_NAME"),
    # )
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]
    )
    print(response.choices[0].message.content)

def main():
    # create_movi()
    # rescale_video()
    # ken_burns_effect()
    # crop_image()
    # ken_burns_effect_video()
    # create_transition()
    # voice()
    # combinate()
    chatGPT()

if __name__ == "__main__":
    main()
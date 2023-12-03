from audio import AudioEditor
from subtitle import SubtitleEditor, len_simbols
from video import VideoEditor, AudioFileClip
from image import ImageEditor
from youtube import post_shorts
import os 
from moviepy.editor import VideoFileClip
import pyttsx3
from pydub import AudioSegment
import fnmatch
import wave
import numpy as np


CLIP_NAME = 'SantaClaus'

def create_shorts_ru():
        count = 1
        text=''
        folder_image = f'image\\{CLIP_NAME}'
        folter_image_crop = f'image_crop\\{CLIP_NAME}'
        folder_video = f'video\\{CLIP_NAME}'
        voice = f'audio\\sound_{CLIP_NAME}.mp3'
        audio_file = f'audio\\voice_{CLIP_NAME}_ru.mp3'
        video_sound = f'video\\{CLIP_NAME}\\video_sound_{CLIP_NAME}.mp4'
        image_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png']

        try:
            with open(f'text\\{CLIP_NAME}_ru.txt', 'r', encoding='UTF-8') as file:
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

        # try:
        #     AudioEditor.change_speed(input_path=voice, output_path=audio_file, speed=1.08)
        # except:
        #     exit('Error: Failed to create final audio')

        if not os.path.exists(folter_image_crop):
            os.makedirs(folter_image_crop)
            print(f"Folder {folter_image_crop} created")
        else:
            print(f"Folder {folter_image_crop} already exists")

        try:
            for file in os.listdir(folder_image):
                if any(fnmatch.fnmatch(file, img) for img in image_list):
                    try:
                        file_name = file.split('.')
                        ImageEditor.crop_image(input_path=f'{folder_image}\\{file}', output_path=f'{folter_image_crop}\\{file_name[0]}_{CLIP_NAME}.jpg')
                        os.rename(f'{folder_image}\\{file}', f'{folder_image}\\{file_name[0]}_{CLIP_NAME}.{file_name[1]}')
                        print(f'The file was successfully renamed from {file} to {file_name[0]}_{CLIP_NAME}.{file_name[1]}')
                    except FileNotFoundError:
                        print(f'File {file} not found')
                    except FileExistsError:
                        print(f'File {file_name[0]}_{CLIP_NAME}.{file_name[1]} already exists')
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
                if file.endswith(f"_{CLIP_NAME}.jpg"):
                    file_name = file.split('.')
                    if count%3!=0:
                        rev = False
                    else:
                        rev = True
                    ImageEditor.ken_burns_effect_video(image_path=f'{folter_image_crop}\\{file}', output_path=f'{folder_video}\\{file_name[0]}.mp4', duration=7, reverse=rev)
                    count += 1
        except:
            exit('Error: Failed to create video')

        try:
            if os.path.exists(f'{folder_video}\\12_{CLIP_NAME}.mp4'):
                print(f"File 12_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\1_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\2_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\12_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 12')
        try:
            if os.path.exists(f'{folder_video}\\34_{CLIP_NAME}.mp4'):
                print(f"File 34_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\3_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\4_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\34_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 34')
        try:
            if os.path.exists(f'{folder_video}\\56_{CLIP_NAME}.mp4'):
                print(f"File 56_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\5_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\6_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\56_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 56')
        try:
            if os.path.exists(f'{folder_video}\\78_{CLIP_NAME}.mp4'):
                print(f"File 78_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\7_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\8_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\78_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 78')
        try:
            if os.path.exists(f'{folder_video}\\1-4_{CLIP_NAME}.mp4'):
                print(f"File 1-4_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\12_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\34_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\1-4_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 1-4')
        try:
            if os.path.exists(f'{folder_video}\\5-8_{CLIP_NAME}.mp4'):
                print(f"File 5-8_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\56_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\78_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\5-8_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 5-8')
        try:
            if os.path.exists(f'{folder_video}\\1-8_{CLIP_NAME}.mp4'):
                print(f"File 1-8_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\1-4_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\5-8_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\1-8_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 1-8')
        try:
            if os.path.exists(f'{folder_video}\\1-9_{CLIP_NAME}.mp4'):
                print(f"File 1-9_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip(f"{folder_video}\\1-8_{CLIP_NAME}.mp4")
                clip2 = VideoFileClip(f"{folder_video}\\9_{CLIP_NAME}.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile(f"{folder_video}\\1-9_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 1-9')

        try:
            if os.path.exists(video_sound):
                print(f"File {video_sound} found in the folder.")
            else:
                video = f"{folder_video}\\1-9_{CLIP_NAME}.mp4"
                result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
        except:
            exit('Error: Failed to create video video_sub')
        
        try:
            if text!='':
                sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
                sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black')
            else:
                exit(f'Error: File {CLIP_NAME}.txt is empty')
        except:
            exit('Error: Failed to create subtitles')

        try:
            if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}.mp4'):
                print(f"File final_video_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip = VideoFileClip(video_sound)
                result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.75)
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
        if os.path.exists(video_sound):
            print(f"File {video_sound} found in the folder.")
        else:
            video = f"{folder_video}\\1-9_{CLIP_NAME}.mp4"
            result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
    except:
        exit('Error: Failed to create video video_sub')
        
    try:
        if text!='':
            sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
            sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black')
        else:
            exit(f'Error: File {CLIP_NAME}.txt is empty')
    except:
        exit('Error: Failed to create subtitles')
            
    try:
        if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4'):
            print(f"File final_video_{CLIP_NAME}_en.mp4 found in the folder.")
        else:
            clip = VideoFileClip(video_sound)
            result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.75)
            result_clip.write_videofile(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4', codec="libx264", audio_codec=None)
            clip.close()
            result_clip.close()
    except:
        exit('Error: Failed to create video video_sub')

    try:
        if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4'):
            VideoEditor.crop(video_path=f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4', output_path= f'{folder_video}\\final_video_crop_{CLIP_NAME}_en.mp4')
        else:
            print(f"File final_video_{CLIP_NAME}_en.mp4 not found in the folder.")
    except:
        exit(f'Error: Failed to crop video final_video_{CLIP_NAME}_en.mp4')
    print('Successfully!')



def main():
    # create_shorts_ru()
    # create_shorts_en()
    len = len_simbols('text\\ChristmasDecor_en.txt')
    print(len)

if __name__ == "__main__":
    main()
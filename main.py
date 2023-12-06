from audio import AudioEditor
from subtitle import SubtitleEditor, len_simbols
from video import VideoEditor, AudioFileClip
from image import ImageEditor
from youtube import post_shorts
import os 
from moviepy.editor import VideoFileClip
# import pyttsx3
from pydub import AudioSegment
import fnmatch
import wave
import numpy as np
import time
from PIL import Image
key = 'MVsaiNhymA81LvKqS9oezJeEpyZ2pYDtq9zFFQvnuWPwCMPmhiOLaI88'

CLIP_NAME = 'Lava'

def create_shorts_ru():
        count = 1
        text=''
        folder_image = f'image\\{CLIP_NAME}'
        folter_image_crop = f'image_crop\\{CLIP_NAME}'
        folter_image_resize = f'image_resize\\{CLIP_NAME}'
        folder_video = f'video\\{CLIP_NAME}'
        folder_final = f'final\\{CLIP_NAME}'
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

        if not os.path.exists(folder_final):
            os.makedirs(folder_final)
            print(f"Folder {folder_final} created")
        else:
            print(f"Folder {folder_final} already exists")

        # -------------------------------------------------------------------- CREATE VIDEO -----------------------------------------------------------------------------
        current_file = ''

        # for i in range(1,15):
        #     file = f"{i}.mp4"
        #     if i%2!=0:
        #         current_file = file
        #     else:
        #         a = current_file.split('.')
        #         b = file.split('.')
        #         clip1 = VideoFileClip(f"{folder_video}\\{current_file}")
        #         clip2 = VideoFileClip(f"{folder_video}\\{file}")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_final}\\{a[0]}-{b[0]}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()

        # for i,item in enumerate(['1-2','3-4','5-6','7-8','9-10','11-12','13-14']):
        #     file = f'{item}.mp4'
        #     if i==0:
        #         current_file = file
        #     else:
        #         a = current_file.split('-')
        #         b = file.split('.')[0].split('-')
        #         clip1 = VideoFileClip(f"{folder_final}\\{current_file}")
        #         clip2 = VideoFileClip(f"{folder_final}\\{file}")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_final}\\{a[0]}-{b[1]}.mp4", codec="libx264", audio_codec=None)
        #         current_file = f'{a[0]}-{b[1]}.mp4'
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()

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
                    result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.6)
                    result_clip.write_videofile(f"{folder_video}\\1-{i}.mp4", codec="libx264", audio_codec=None)
                    result_clip.close()
                clip1.close()
                clip2.close()
                current_file = f'1-{i}.mp4'



        # try:
        #     if os.path.exists(f'{folder_video}\\12_{CLIP_NAME}.mp4'):
        #         print(f"File 12_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\1_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\2_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\12_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 12')
        # try:
        #     if os.path.exists(f'{folder_video}\\34_{CLIP_NAME}.mp4'):
        #         print(f"File 34_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\3_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\4_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\34_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 34')
        # try:
        #     if os.path.exists(f'{folder_video}\\56_{CLIP_NAME}.mp4'):
        #         print(f"File 56_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\5_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\6_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\56_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 56')
        # try:
        #     if os.path.exists(f'{folder_video}\\78_{CLIP_NAME}.mp4'):
        #         print(f"File 78_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\7_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\8_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\78_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 78')
        
        # try:
        #     if os.path.exists(f'{folder_video}\\910_{CLIP_NAME}.mp4'):
        #         print(f"File 910_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\9_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\10_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\910_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 910')

        # try:
        #     if os.path.exists(f'{folder_video}\\1112_{CLIP_NAME}.mp4'):
        #         print(f"File 1112_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\11_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\12_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\1112_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 1112')

        # try:
        #     if os.path.exists(f'{folder_video}\\1314_{CLIP_NAME}.mp4'):
        #         print(f"File 1314_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\13_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\14_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\1314_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 1314')

        # try:
        #     if os.path.exists(f'{folder_video}\\1-4_{CLIP_NAME}.mp4'):
        #         print(f"File 1-4_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\12_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\34_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\1-4_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 1-4')
        # try:
        #     if os.path.exists(f'{folder_video}\\5-8_{CLIP_NAME}.mp4'):
        #         print(f"File 5-8_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\56_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\78_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\5-8_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 5-8')
        # try:
        #     if os.path.exists(f'{folder_video}\\9-12_{CLIP_NAME}.mp4'):
        #         print(f"File 9-14_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\910_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\1112_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\9-12_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 9-12')
        # try:
        #     if os.path.exists(f'{folder_video}\\1-8_{CLIP_NAME}.mp4'):
        #         print(f"File 1-8_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\1-4_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\5-8_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\1-8_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 1-8')
        # try:
        #     if os.path.exists(f'{folder_video}\\9-14_{CLIP_NAME}.mp4'):
        #         print(f"File 9-14_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\9-12_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\1314_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\9-14_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 9-14')
        # try:
        #     if os.path.exists(f'{folder_video}\\1-14_{CLIP_NAME}.mp4'):
        #         print(f"File 9-14_{CLIP_NAME}.mp4 found in the folder.")
        #     else:
        #         clip1 = VideoFileClip(f"{folder_video}\\1-8_{CLIP_NAME}.mp4")
        #         clip2 = VideoFileClip(f"{folder_video}\\9-14_{CLIP_NAME}.mp4")
        #         result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.5)
        #         result_clip.write_videofile(f"{folder_video}\\1-14_{CLIP_NAME}.mp4", codec="libx264", audio_codec=None)
        #         clip1.close()
        #         clip2.close()
        #         result_clip.close()
        # except:
        #     exit('Error: Failed to create video 1-14')

        # ------------------------------------------------------------- END ----------------------------------------------------------------------------

        try:
            if os.path.exists(f'{folder_video}\\1-14_crop.mp4'):
                print(f"File 1-14_crop.mp4 found in the folder.")
            else:
                VideoEditor.crop(video_path=f'{folder_video}\\1-14.mp4', output_path= f'{folder_video}\\1-14_crop.mp4', audio_path = audio_file)
        except:
            exit(f'Error: Failed to crop video 1-14_crop.mp4')

        try:
            if os.path.exists(video_sound):
                print(f"File {video_sound} found in the folder.")
            else:
                video = f"{folder_video}\\1-14_crop.mp4"
                result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
        except:
            exit('Error: Failed to create video video_sub')
        
        try:
            if text!='':
                sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
                sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black',font='Segoe-UI-Bold')
            else:
                exit(f'Error: File {CLIP_NAME}.txt is empty')
        except:
            exit('Error: Failed to create subtitles')

        try:
            if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}.mp4'):
                print(f"File final_video_{CLIP_NAME}.mp4 found in the folder.")
            else:
                clip = VideoFileClip(video_sound)
                result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
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
        if os.path.exists(f'{folder_video}\\1-14.mp4'):
            VideoEditor.crop(video_path=f'{folder_video}\\1-14.mp4', output_path= f'{folder_video}\\1-14_crop.mp4', audio_path=audio_file)
        else:
            print(f"File 1-14_crop.mp4 not found in the folder.")
    except:
        exit(f'Error: Failed to crop video 1-14.mp4')
    
    try:
        if os.path.exists(video_sound):
            print(f"File {video_sound} found in the folder.")
        else:
            video = f"{folder_video}\\1-14_crop.mp4"
            result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
    except:
        exit('Error: Failed to create video video_sub')
        
    try:
        if text!='':
            sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
            sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black', font='Arial-Rounded-MT-Bold')
        else:
            exit(f'Error: File {CLIP_NAME}.txt is empty')
    except:
        exit('Error: Failed to create subtitles')
            
    try:
        if os.path.exists(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4'):
            print(f"File final_video_en.mp4 found in the folder.")
        else:
            clip = VideoFileClip(video_sound)
            result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.5)
            result_clip.write_videofile(f'{folder_video}\\final_video_{CLIP_NAME}_en.mp4', codec="libx264", audio_codec=None)
            clip.close()
            result_clip.close()
    except:
        exit('Error: Failed to create video final_video_en.mp4')

    print('Successfully!')



def main():
    start_time = time.time()

    # create_shorts_ru()
    create_shorts_en()

    # len = len_simbols('text\\voice_Lava_en.txt')
    # print(len)
    # clip = AudioFileClip('audio\\Lava.mp3').duration
    # print(clip)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time/60} минут")

    # ImageEditor.get_pexels_images(api_key=key,save_path=f'image\\{CLIP_NAME}')




if __name__ == "__main__":
    main()
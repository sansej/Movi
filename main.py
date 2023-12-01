from audio import AudioEditor
from subtitle import SubtitleEditor
from video import VideoEditor, AudioFileClip
from image import ImageEditor
from youtube import post_shorts
import os 
from moviepy.editor import VideoFileClip
import pyttsx3
from pydub import AudioSegment

def create_shorts():
        count = 1
        folder_image = 'image'
        folter_image_crop = 'image_crop'
        folder_video = 'video'
        voice = 'audio\\crop.mp3'
        audio_file = 'audio\\voice.mp3'
        video_sound = 'video\\video_sound.mp4'

        text = """ Темные стороны Луны: Луна всегда обращена к Земле одной и той же стороной из-за синхронного вращения. Её обратная сторона оставалась тайной до момента, когда космические миссии стали исследовать её. Эта загадочная область отличается от видимой стороны по ландшафту и геологии. Лунные трясины: Во время миссий Apollo астронавты заметили необычное явление — лунные трясины. После того как они выпустили модуль на поверхность, Луна "зазвучала" подобно колокольчику. Эти грунтовые волны указывают на наличие подпольных пустот или слоев, делая Луну более загадочной, чем предполагалось. Лунные вулканы: На Луне есть следы деятельности вулканов. Самый высокий вулкан, Олимп, возвышается на 21 километр, превосходя высоту любой вулканической горы на Земле."""
    
        # try:
        #     AudioEditor.create_voice(text=text,output_file=voice)
        # except:
        #     exit('Error: Failed to create sound')
        # try:
        #     AudioEditor.change_speed(input_path=voice, output_path=audio_file, speed=1.08)
        # except:
        #     exit('Error: Failed to create final audio')

        # try:
        #     for file in os.listdir(folder_image):
        #         if file.endswith(".jpg") or file.endswith(".png"):
        #             ImageEditor.crop_image(input_path=f'{folder_image}\\{file}', output_path=f'{folter_image_crop}\\{count}.jpg')
        #             count += 1
        # except:
        #     exit('Error: Failed to crop image')

        try:
            count = 1
            for file in os.listdir(folter_image_crop):
                if count%3!=0:
                    rev = False
                else:
                    rev = True
                ImageEditor.ken_burns_effect_video(image_path=f'{folter_image_crop}\\{file}', output_path=f'{folder_video}\\{count}.mp4', duration=7, reverse=rev)
                count += 1
        except:
            exit('Error: Failed to create video')

        try:
            if os.path.exists('video\\12.mp4'):
                print("File 12.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\1.mp4")
                clip2 = VideoFileClip("video\\2.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\12.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 12')
        try:
            if os.path.exists('video\\34.mp4'):
                print("File 34.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\3.mp4")
                clip2 = VideoFileClip("video\\4.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\34.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 34')
        try:
            if os.path.exists('video\\56.mp4'):
                print("File 56.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\5.mp4")
                clip2 = VideoFileClip("video\\6.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\56.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 56')
        try:
            if os.path.exists('video\\78.mp4'):
                print("File 78.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\7.mp4")
                clip2 = VideoFileClip("video\\8.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\78.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 78')
        try:
            if os.path.exists('video\\1-4.mp4'):
                print("File 1-4.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\12.mp4")
                clip2 = VideoFileClip("video\\34.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\1-4.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 1-4')
        try:
            if os.path.exists('video\\5-8.mp4'):
                print("File 5-8.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\56.mp4")
                clip2 = VideoFileClip("video\\78.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\5-8.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 5-8')
        try:
            if os.path.exists('video\\1-8.mp4'):
                print("File 1-8.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\1-4.mp4")
                clip2 = VideoFileClip("video\\5-8.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\1-8.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 1-8')
        try:
            if os.path.exists('video\\1-9.mp4'):
                print("File 1-9.mp4 found in the folder.")
            else:
                clip1 = VideoFileClip("video\\1-8.mp4")
                clip2 = VideoFileClip("video\\9.mp4")
                result_clip = VideoEditor.create_transition([clip1, clip2],overlap=0.75)
                result_clip.write_videofile("video\\1-9.mp4", codec="libx264", audio_codec=None)
                clip1.close()
                clip2.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video 1-9')

        try:
            if os.path.exists(video_sound):
                print(f"File {video_sound} found in the folder.")
            else:
                video = "video\\1-9.mp4"
                result_clip = VideoEditor.combinate(audio_path=audio_file,video_path=video,output_path=video_sound)
        except:
            exit('Error: Failed to create video video_sub')
        
        try:
            sub = AudioEditor.to_subtitle(audio_file_path=audio_file, text=text)
            sub_clip = SubtitleEditor.create_subtitle_clips(sub,(720,1280),fontsize=70, stroke_color='black')
        except:
            exit('Error: Failed to create subtitles')
        try:
            if os.path.exists('video\\final_video.mp4'):
                print(f"File final_video.mp4 found in the folder.")
            else:
                clip = VideoFileClip(video_sound)
                result_clip = VideoEditor.create_transition([clip],sub_clip,overlap=0.75)
                result_clip.write_videofile('video\\final_video.mp4', codec="libx264", audio_codec=None)
                clip.close()
                result_clip.close()
        except:
            exit('Error: Failed to create video video_sub')

        try:
            if os.path.exists('video\\final_video.mp4'):
                VideoEditor.crop(video_path='video\\final_video.mp4', output_path= 'video\\final_video_crop.mp4')
            else:
                print(f"File final_video.mp4 not found in the folder.")
        except:
            exit('Error: Failed to crop video final_video.mp4')
        print('Successfully!')


def main():
    create_shorts()



    # audio = AudioSegment.from_file("test.mp3")
    # current_duration = len(audio)/1000 # в секундах
    # print(current_duration)
    # target_duration = 60
    # speed_ratio = current_duration / target_duration
    # print(speed_ratio)
    # adjusted_audio = audio.speedup(playback_speed=speed_ratio+0.01)
    # adjusted_audio.export("test_out.mp3", format="mp3")

    # cu_duration = len(AudioSegment.from_file("test_out.mp3")) / 1000  # в секундах
    # print(cu_duration)


if __name__ == "__main__":
    main()
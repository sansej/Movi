from audio import AudioEditor
from subtitle import SubtitleEditor
from video import VideoEditor, AudioFileClip
from image import ImageEditor
from youtube import post_shorts
import os 
from moviepy.editor import VideoFileClip

def create_shorts():
        count = 1
        folder_image = 'image'
        folter_image_crop = 'image_crop'
        folder_video = 'video'
        voice = 'crop.mp3'
        audio_file = 'voice.mp3'
        video_sound = 'video\\video_sound.mp4'

        text = '''Юпи́тер – самая крупная планета в Солнечной системе. Её масса в 318 раз больше массы Земли,
        а объем в 1300 раз больше. Если бы Юпи́тер был ещё чуть-чуть массивнее, он мог бы стать звездой,
        так как в его ядре происходит процесс термоядерного синтеза, подобный тому, что происходит в звёздах.
        На Юпи́тере есть впечатляющее магнитное поле, превосходящее магнитное поле любой другой планеты
        в Солнечной системе. Это поле создает мощные радиальные лучи, наблюдаемые в районе полюсов. Эти
        светящиеся лучи делают Юпи́тер еще более удивительным объектом для наблюдения. У Юпи́тера более 80
        известных спутников. Самый известный из них – Ганимед, самый крупный спутник в Солнечной системе.
        Ещё один известный спутник Юпи́тера – Ио – известен своими вулканическими извержениями и
        ярко-красными пя́тнами на поверхности.'''

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

        # try:
        #     count = 1
        #     for file in os.listdir(folter_image_crop):
        #         if count%3!=0:
        #             rev = False
        #         else:
        #             rev = True
        #         ImageEditor.ken_burns_effect_video(image_path=f'{folter_image_crop}\\{file}', output_path=f'{folder_video}\\{count}.mp4', duration=7, reverse=rev)
        #         count += 1
        # except:
        #     exit('Error: Failed to create video')

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
    # create_shorts()
#     # post_shorts(video_path="video\\final_video.mp4",title="Интресные факты. Сатурн",description="несколько интересных фактов о планете Сатурн")
#     post_shorts()
    s  = VideoFileClip('video\\final_video.mp4').duration
    # a  = VideoFileClip('video\\final_video_crop.mp4').duration
    d  = AudioFileClip('voice.mp3').duration
    print(s,d)


if __name__ == "__main__":
    main()
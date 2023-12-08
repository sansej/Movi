from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
from audio import AudioEditor
from subtitle import SubtitleEditor
import cv2
import numpy as np

class VideoEditor:

    def create_transition(video_files, subtitles_clip=None, overlap = 1, resize = False):
        """
        Parameters
        -----------
        clips_path - path to source first video ``*.MP4``

        subtitles_clip - 

        output_file - path to final video ``*.MP4``

        overlap - transition time in ``seconds``, default ``1s``

        resize - Error ``False`` | crop to min resolution ``True`` (if different resolutions)

        """
        if subtitles_clip:
            final_clip = CompositeVideoClip(video_files + subtitles_clip)
        else:
            files_array = [video_files[0].crossfadeout(overlap),video_files[1].set_start(video_files[0].duration - overlap).crossfadein(overlap)]
            final_clip = CompositeVideoClip(files_array)
        return final_clip

    def combinate(video_path, audio_path, output_path, crop=False):
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        video_durasion = video_clip.duration
        audio_durasion = audio_clip.duration
        video_clip = video_clip.set_audio(audio_clip)
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        video_clip.close()
        audio_clip.close()

    def crop(video_path,  output_path, duration=None, audio_path=None):
        """
        Parameters
        -----------
        video_path - path to source video ``*.MP4``

        output_path - path to final video ``*.MP4``

        duration - duration in ``seconds``, default ``60s``

        """
        video_clip = VideoFileClip(video_path)

        if audio_path:
            audio_clip = AudioFileClip(audio_path)
            if video_clip.duration>audio_clip.duration:
                trimmed_video = video_clip.subclip(0, audio_clip.duration)
                trimmed_video.write_videofile(output_path, codec='libx264', audio_codec=None)
                video_clip.close()
                trimmed_video.close()
                audio_clip.close()
                return
            else:
                return
        
        if duration:
            if video_clip.duration<=duration:
                print('Crop no required')
                return
            else:
                cropped_clip = video_clip.subclip(0, duration)
                cropped_clip.write_videofile(output_path, codec='libx264', audio_codec=None)
                video_clip.close()
                cropped_clip.close()
                return
            
    def chromoKey(input_path, output_path, start_frame=None, end_frame=None, chromo_path='mrSim.mp4'):
        lower_green = np.array([40, 50, 50]) # Определение диапазона цветов хромакея (зеленого фона)
        upper_green = np.array([90, 255, 255])
        cap_chromakey = cv2.VideoCapture(chromo_path)
        cap_background = cv2.VideoCapture(input_path)       
        width = int(cap_chromakey.get(3))# Определение параметров видео (ширина, высота и частота кадров)
        height = int(cap_chromakey.get(4))
        fps = int(cap_chromakey.get(5))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Используйте 'mp4v' для кодирования в MP4
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        start_frame = 100#round(50*fps) # Определение начального и конечного кадра для применения хромакея
        end_frame = 300#round(58*fps)
        frame_number = 0
        while cap_chromakey.isOpened() and cap_background.isOpened():
            ret_chromakey, frame_chromakey = cap_chromakey.read()
            ret_background, frame_background = cap_background.read()
            if not ret_chromakey or not ret_background:
                break
            hsv = cv2.cvtColor(frame_chromakey, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_green, upper_green)
            inverted_mask = cv2.bitwise_not(mask)
            chromakey_result = cv2.bitwise_and(frame_chromakey, frame_chromakey, mask=inverted_mask)
            background_result = cv2.bitwise_and(frame_background, frame_background, mask=mask)
            chromakey_result = cv2.resize(chromakey_result, (width, height))
            if start_frame <= frame_number <= end_frame:
                result = cv2.addWeighted(chromakey_result, 1, background_result, 1, 0, dtype=cv2.CV_8U)
            else:
                result = frame_background
            out.write(result)
            # cv2.imshow('With Background Chromakey', result)# Отображение результата
            # if cv2.waitKey(25) & 0xFF == ord('q'):
            #     break
            frame_number += 1
        cap_chromakey.release()
        cap_background.release()
        out.release()
        cv2.destroyAllWindows()
            
        

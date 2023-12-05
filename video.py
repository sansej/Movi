from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
from audio import AudioEditor
from subtitle import SubtitleEditor

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
        # if clip1.size!=clip2.size:
        #     if resize:
        #         common_height = min(clip1.size[1], clip2.size[1])
        #         clip1 = clip1.resize(height=common_height)
        #         clip2 = clip2.resize(height=common_height)
        #     else:
        #         print("Warning: The incoming videos have different resolutions.")
        #         return
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
            
        

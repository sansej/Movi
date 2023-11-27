import moviepy as mp

class VideoEditor:

    def create_transition(self, clip1_path, clip2_path, output_file, overlap = 1, resize = False):
        """
        clip1_path - path to source first video ``*.MP4``

        clip2_path - path to source second video ``*.MP4``

        output_file - path to final video ``*.MP4``

        overlap - transition time in ``seconds``, default ``1s``

        resize - Error ``False`` | crop to min resolution ``True`` (if different resolutions)

        """
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

    def combinate(self, video_path, audio_path, output_path, crop=False):
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
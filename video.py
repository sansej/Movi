from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
from audio import AudioEditor
from subtitle import SubtitleEditor

class VideoEditor:

    def create_transition(video_files, subtitles_clip, overlap = 1, resize = False):
        """
        Parameters
        -----------
        clips_path - path to source first video ``*.MP4``

        subtitles_clip - 

        output_file - path to final video ``*.MP4``

        overlap - transition time in ``seconds``, default ``1s``

        resize - Error ``False`` | crop to min resolution ``True`` (if different resolutions)

        """
        # video_clips = [VideoFileClip(file) for file in video_files]

        # if clip1.size!=clip2.size:
        #     if resize:
        #         common_height = min(clip1.size[1], clip2.size[1])
        #         clip1 = clip1.resize(height=common_height)
        #         clip2 = clip2.resize(height=common_height)
        #     else:
        #         print("Warning: The incoming videos have different resolutions.")
        #         return
        files_array = []
        for i, clip in enumerate(video_files):
            if i==0:
                files_array.append(clip.crossfadeout(overlap))
            files_array.append(clip.set_start(clip.duration - overlap).crossfadein(overlap))

        final_clip = CompositeVideoClip(files_array + subtitles_clip)
        # final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        # final_clip.close()
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

    def create_composite_clip(video_files, subtitles_clip, audio_file, overlap=1):
        video_clips = [VideoFileClip(file) for file in video_files]
        # video = CompositeVideoClip([clip.crossfadeout(overlap) for clip in video_files])

        clips_to_combine = [video.crossfadeout(overlap) for video in video_clips[:-1]] + \
                        [video.set_start(sum(clip.duration for clip in video_clips[:-1]) - overlap).crossfadein(overlap) for video in video_clips[1:]]
        
        composite_clip = CompositeVideoClip(clips_to_combine)

        if subtitles_clip:

            composite_clip = CompositeVideoClip(clips_to_combine)
        
        if audio_file:
            audio_clip = AudioFileClip(audio_file)
            video_clip = composite_clip.set_audio(audio_clip)
            # for i, video_clip in enumerate(video_clips):
            #     video_clip = video_clip.set_audio(audio_clip.subclip(video_clip.start, video_clip.end))

        # if subtitles_clip:
        #     clips_to_combine.append(subtitles_clip)
        # composite_clip = CompositeVideoClip(clips_to_combine)
        return composite_clip

#     # Пример использования функции с аудио, субтитрами и указанным аудиофайлом
# video_files = ("out.mp4", "out1.mp4", "out2.mp4")
# audio_file = "out.wav"
# composite_clip = VideoEditor.create_composite_clip(video_files, audio_file)
# composite_clip.write_videofile("output_with_audio_and_without_subtitles.mp4", codec='libx264', audio_codec="aac")

#     # Пример использования функции без аудио, субтитров и указания аудиофайла
# text = 'Привет! Сегодня расскажу об очень интерестном и прекрасном явлении, таком как северное сияние.'
# video_files = ("out.mp4", "ou2.mp4")
# sub = AudioEditor.to_subtitle(audio_file_path='out.wav', text=text)
# sub_clip = SubtitleEditor.create_subtitle_clips(sub,video_files[0].size,fontsize=70,background='black')
# composite_clip = VideoEditor.create_composite_clip(video_files, subtitles_clip=sub_clip)
# composite_clip.write_videofile("output_without_audio_and_with_subtitles.mp4", codec='libx264', audio_codec=None)

# text = 'Привет! Сегодня расскажу об очень интерестном и прекрасном явлении, таком как северное сияние.'
# video_files = ("out.mp4")
# audio_file = "out.wav"
# sub = AudioEditor.to_subtitle(audio_file_path='out.wav', text=text)
# sub_clip = SubtitleEditor.create_subtitle_clips(sub,video_files[0].size,fontsize=70,background='black')
# composite_clip = VideoEditor.create_composite_clip(video_files, subtitles_clip=sub_clip, audio_file=audio_file)
# composite_clip.write_videofile("output_with_audio_and_with_subtitles.mp4", codec='libx264', audio_codec='aac')







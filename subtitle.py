from moviepy.editor import TextClip
from moviepy.config import change_settings

class SubtitleEditor:

    def create_subtitle_clips(self, subtitles, videosize,fontsize=80, font='Arial', color='yellow', debug = False):
        subtitle_clips = []
        change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})
        for subtitle in subtitles:
            start_time = self.time_to_seconds(subtitle.start)
            end_time = self.time_to_seconds(subtitle.end)
            duration = end_time - start_time
            video_width, video_height = videosize
            text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color,size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
            subtitle_x_position = 'center'
            subtitle_y_position = 'center'
            text_position = (subtitle_x_position, subtitle_y_position)                    
            subtitle_clips.append(text_clip.set_position(text_position))
        return subtitle_clips
    
    def time_to_seconds(self, time_obj):
        return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000

from moviepy.editor import TextClip
from moviepy.config import change_settings
import unicodedata

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

    def split_text(text, num_parts):
        words = text.split()
        total_chars = len(text.replace(" ", ""))
        chars_per_part = round(total_chars / num_parts)
        current_part = 1
        text_parts = []
        old_part = 1
        word_box = ''
        simbol_counter=0
        current_chars = total_chars
        for word in words:
            ln = len([char for char in unicodedata.normalize('NFD', word) if unicodedata.category(char) != 'Mn'])
            if simbol_counter + ln <= round(chars_per_part*1.1):
                word_box = word_box + word + ' '
                simbol_counter += ln
            else:
                current_part += 1
                current_chars -= simbol_counter
                simbol_counter = ln
                text_parts.append(word_box + ' ')
                word_box = ''
                word_box = word_box + word + ' '
            if old_part!=current_part:
                chars_per_part = round(current_chars / (num_parts - old_part))
                old_part = current_part
        text_parts.append(word_box)
        return text_parts
    
    
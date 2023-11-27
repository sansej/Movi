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

    def split_text(text, num_parts):
        # Разбиваем текст на слова
        words = text.split()

        # Считаем общее количество символов в тексте
        total_chars = sum(len(word) for word in words)

        # Вычисляем примерное количество символов в каждой части
        chars_per_part = total_chars // num_parts

        # Инициализируем переменные для отслеживания текущего количества символов
        current_chars = 0
        current_part = 1

        # Создаем список для хранения частей текста
        text_parts = ['']

        # Проходим по словам и добавляем их к текущей части текста
        for word in words:
            if current_chars + len(word) <= chars_per_part:
                text_parts[current_part - 1] += word + ' '
                current_chars += len(word) + 1  # +1 для пробела между словами
            else:
                # Переходим к следующей части текста
                current_part += 1
                current_chars = len(word) + 1
                text_parts.append(word + ' ')

        # Возвращаем список частей текста
        return text_parts
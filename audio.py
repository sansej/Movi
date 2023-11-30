from elevenlabs import generate, save, set_api_key
from subtitle import SubtitleEditor
import os
import numpy
from pydub import AudioSegment

set_api_key(os.environ.get("ELEVEN_KEY"))

class AudioEditor:

    def create_voice(output_file, text):
        audio = generate(
        text=text,
        voice = "Fin",
        model="eleven_multilingual_v2"
        )
        save(audio, output_file)

    def change_speed(input_path, output_path, format = 'wav', speed = 1.07):
        sound = AudioSegment.from_file(input_path)
        so = sound.speedup(playback_speed = speed)
        so.export(output_path, format = format)

    def to_subtitle_file(audio_file_path, subtitle_file, text):
        """
        creates subtitles from an audio file

        audio_file_path - path to audio file ``*.MP3`` ``*.WAV``

        subtitle_file - sub file path ``*.SRT``

        text
        """
        srt = []
        segments = detect_segments(audio_file_path)
        result = SubtitleEditor.split_text(text, len(segments))
        with open(subtitle_file, 'w', encoding='UTF-8') as f:
            for i, (segment, part_text) in enumerate(zip(segments, result), start=1):
                f.write(f"{i}\n")
                f.write(f"{segment[0]} --> {segment[1]}\n")
                f.write(f"{part_text}\n\n")
                srt.append((segment[0], segment[1], part_text))
        return srt
    
    def to_subtitle(audio_file_path, text):
        """
        creates subtitles from text

        audio_file_path - path to audio file ``*.MP3`` ``*.WAV``

        text
        """
        srt = []

        # audio = AudioSegment.from_file(audio_file_path)
        # duration_in_seconds = len(audio) / 1000  # ms
    
        segments = divide_into_parts(audio_file_path)
        result = SubtitleEditor.split_text(text, len(segments))
        for (segment, part_text) in zip(segments, result):
            srt.append((segment[0], segment[1], part_text))
        return srt

def detect_segments(audio_file_path, silence_threshold=-40, min_silence_duration=1000):
        '''
        Parameters
        -----------
        audio_file_path - path to audio file ``*.MP3`` ``*.WAV``

        silence_threshold - silence threshold, default ``40dB``

        min_silence_duration - minimum silence duration, default ``1000mcs``
        '''
        audio = AudioSegment.from_file(audio_file_path)
        audio_array = numpy.array(audio.get_array_of_samples())
        sound_segments = []
        is_sound = False
        start_time = 0
        for i, sample in enumerate(audio_array):
            if sample > silence_threshold:
                if not is_sound:
                    start_time = i
                    is_sound = True
            else:
                if is_sound:
                    end_time = i
                    is_sound = False
                    duration = end_time - start_time
                    if duration > min_silence_duration:
                        start_time_sec = start_time / audio.frame_rate
                        end_time_sec = end_time / audio.frame_rate
                        start_time_formatted = format_seconds(start_time_sec)
                        end_time_formatted = format_seconds(end_time_sec)
                        sound_segments.append((start_time_formatted, end_time_formatted))
        return sound_segments

def divide_into_parts(audio_file_path):
        '''
        Parameters
        -----------
        audio_file_path - path to audio file ``*.MP3`` ``*.WAV``

        '''
        audio = AudioSegment.from_file(audio_file_path)
        duration_in_seconds = len(audio) # ms
        num_parts = round(duration_in_seconds/2000)
        part_duration = round(duration_in_seconds/num_parts)
        result_array = []
        for i in range(num_parts):
            start_time = format_miliseconds(i * part_duration)
            end_time = format_miliseconds((i + 1) * part_duration)
            result_array.append((start_time, end_time))
        return result_array

    
def format_seconds(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        microseconds = int((seconds % 1) * 1e6)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{microseconds:06d}"

def format_miliseconds(miliseconds):
        seconds, msec = divmod(miliseconds, 1000)
        minuts, sec = divmod(seconds, 60)
        hours, min = divmod(minuts, 60)
        return f"{int(hours):02d}:{int(min):02d}:{int(sec):02d},{msec:03d}"




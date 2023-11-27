from elevenlabs import generate, save, set_api_key
import os
import numpy
from pydub import AudioSegment

set_api_key(os.environ.get("ELEVEN_KEY"))

class AudioEditor:

    def create_voice(self, voice="Fin", output_file = 'out.wav', text=''):
        audio = generate(
        text=text,
        voice = voice,
        model="eleven_multilingual_v2"
        )
        save(audio, output_file)

    def change_speed(self, input_path, output_path, format = 'wav', speed = 1.07):
        sound = AudioSegment.from_file(input_path)
        so = sound.speedup(playback_speed = speed)
        so.export(output_path, format = format)

    def detect_segments(self, audio_file_path, silence_threshold=-40, min_silence_duration=1000):
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
                        start_time_formatted = self.format_seconds(start_time_sec)
                        end_time_formatted = self.format_seconds(end_time_sec)
                        sound_segments.append((start_time_formatted, end_time_formatted))
        return sound_segments

    def format_seconds(self,seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        microseconds = int((seconds % 1) * 1e6)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{microseconds:06d}"
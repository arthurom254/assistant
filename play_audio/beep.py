from pydub import AudioSegment
from pydub.generators import Sine

def generate_beep(file_path):
    sine_wave = Sine(1000).to_audio_segment(duration=500)
    
    sine_wave = sine_wave + 10
    
    sine_wave.export(file_path, format="mp3")
generate_beep("alert_beep.mp3")

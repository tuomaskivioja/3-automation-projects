import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_filenmae = ""
FILENAME_FROM_MIC = "RECORDING.WAV"
VOICE_TEXT_FILENAME = "VOICE_AS_TEXT.txt"

# initialize the recognizer
r = sr.Recognizer()

def recognize_from_file(filename):
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text

def recognize_from_microphone(file_to_write):
    SAMPLE_RATE=44100
    duration = 5  # seconds
    audio_recording = sd.rec(duration * SAMPLE_RATE, samplerate=SAMPLE_RATE, channels=1, dtype='int32')
    print("Recording Audio")
    sd.wait()
    print("Audio recording complete , Play Audio")
    sd.play(audio_recording, SAMPLE_RATE)
    sd.wait()
    print("Play Audio Complete")
    wav.write(file_to_write, SAMPLE_RATE, audio_recording)

def save_text_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


if __name__ == "__main__":
    #print(recognize_from_file(test_filenmae))
    recognize_from_microphone(FILENAME_FROM_MIC)
    text_from_voice = recognize_from_file(FILENAME_FROM_MIC)
    save_text_to_file(text_from_voice, VOICE_TEXT_FILENAME)
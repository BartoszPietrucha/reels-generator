import speech_recognition as sr
from gtts import gTTS
import moviepy.editor as mp

class ReelsGenerator:

    def __init__(self):
        pass

    def _voice_to_text(self, sound_path):
        file = sr.AudioFile(sound_path)
        recognizer = sr.Recognizer()
        with file as source:
            audio = recognizer.record(source)
        #print(recognizer.recognize_google(audio))
        return recognizer.recognize_google(audio)

    def _text_to_voice(self, text, lang="eng"):
        tts = gTTS(text=text, lang=lang)
        tts.save("assets/test_audio/output.mp3")

    def _change_voice(self, sound_path, lang="en"):
        text = self._voice_to_text(sound_path)
        self._text_to_voice(text, lang)

    def _extract_audio(self, video_path):
        clip = mp.VideoFileClip(video_path)
        clip.audio.write_audiofile("assets/test_audio/extracted.wav")



import speech_recognition as sr
from gtts import gTTS
import moviepy.editor as mp
import os

class ReelsGenerator:
    """
    Responsible for editing the video.
    """
    TEMP_LOC = "assets/test_audio/"
    TEMP_AUDIO = f"{TEMP_LOC}extracted.wav"

    def __init__(self):
        pass


    def _edit_video(self, video_path: str, lang="en") -> None:
        """
        Edits the video by changing the voice to other lector.
        """
        self._extract_audio(video_path)
        self._change_voice(self.TEMP_AUDIO, lang)
        self._replace_audio(video_path, self.TEMP_AUDIO, "F:\\Desktop\\TESTREEL\\test.mp4")
        os.remove(self.TEMP_AUDIO)  # removes the temporary audio file


    def _change_voice(self, sound_path: str, lang="en") -> None:
        """
        Extracts the text from the sound and then generates the sound with the new lector.
        """
        text = self._voice_to_text(sound_path)
        self._text_to_voice(text, lang)


    def _voice_to_text(self, sound_path: str) -> str:
        """
        Extracts the text from the sound.
        """
        file = sr.AudioFile(sound_path)
        recognizer = sr.Recognizer()
        with file as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)


    def _text_to_voice(self, text: str, lang="eng") -> None:
        """
        Generates the sound of the given text.
        """
        tts = gTTS(text=text, lang=lang)
        tts.save(self.TEMP_AUDIO)


    def _extract_audio(self, video_path: str) -> None:
        """
        Extracts the audio from the video.
        """
        clip = mp.VideoFileClip(video_path)
        clip.audio.write_audiofile(self.TEMP_AUDIO)


    def _replace_audio(self, video_path: str, sound_path: str, file_output: str) -> None:
        """
        Replaces the audio in the video with the new one.
        """
        video = mp.VideoFileClip(video_path)
        audio = mp.AudioFileClip(sound_path)
        video = video.set_audio(audio)
        video.write_videofile(file_output)



import speech_recognition as sr
from gtts import gTTS
import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip
import os
import assemblyai as aai
import pprint


class ReelsGenerator:
    """
    Responsible for editing the video.
    """
    ID = 0
    

    def __init__(self, output_dir: str = ".", temp_loc: str = "."):
        self.TEMP_LOC = temp_loc
        self.TEMP_AUDIO = f"{self.TEMP_LOC}\\extracted.wav"
        self.OUTPUT_DIR = output_dir


    def _edit_video(self, video_path: str, lang="en") -> None:
        """Edits the video by changing the voice to other lector."""
        file_name = f"{self.OUTPUT_DIR}\\edited_{self.ID}.mp4"
        self._extract_audio(video_path)
        self._change_voice(self.TEMP_AUDIO, lang)
        self._replace_audio(video_path, self.TEMP_AUDIO, file_name)
        os.remove(self.TEMP_AUDIO)  # removes the temporary audio file
        self.ID += 1


    def _change_voice(self, sound_path: str, lang="en") -> None:
        """Extracts the text from the sound and then generates the sound with the new lector."""
        text = self._voice_to_text(sound_path)
        self._text_to_voice(text, lang)


    def _voice_to_text(self, sound_path: str) -> str:
        """Extracts the text from the sound."""
        file = sr.AudioFile(sound_path)
        recognizer = sr.Recognizer()
        with file as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language="en-US")


    def _text_to_voice(self, text: str, lang="eng") -> None:
        """Generates the sound of the given text."""
        tts = gTTS(text=text, lang=lang, slow=False, tld="us")
        tts.save(self.TEMP_AUDIO)


    def _extract_audio(self, video_path: str) -> None:
        """Extracts the audio from the video."""
        with mp.VideoFileClip(video_path) as clip:
            clip.audio.write_audiofile(self.TEMP_AUDIO)


    def _replace_audio(self, video_path: str, sound_path: str, file_output: str) -> None:
        """
        Replaces the audio in the video with the new one.
        Also adds the subtitles to the video.
        """
        with mp.VideoFileClip(video_path) as video:
            video_size = video.size
            generator = lambda txt: mp.TextClip(txt, fontsize=70, font="Dubai-bold", color="white",
                                                    stroke_color="black", stroke_width=2, size=video_size, method="caption",)
            subtitles = self._create_srt(sound_path)
            sub = SubtitlesClip(subtitles, generator)
            with mp.AudioFileClip(sound_path) as audio:
                video = video.set_audio(audio)
                video = mp.CompositeVideoClip([video, sub.set_position(("center", "bottom"))])
                video.write_videofile(file_output)


    def _create_srt(self, audio):
        """Generates subtitles data for the video."""

        def _format_time(time: str) -> str:
            """Formats the srt time to float number."""
            parts = time.split(":")
            return round(3600 * int(parts[0]) + 60 * int(parts[1]) + float(parts[2]), 1)

        def _retrieve_time(srt_time: str) -> tuple:
            """Retrieves the start and end time from the srt time."""
            result = srt_time.replace("\n", "").replace(",", ".")
            start, end = result.split(" --> ")
            return (_format_time(start), _format_time(end))

        

        aai.settings.api_key = os.environ["ASSEMBLYAI_KEY"]
        transcriber = aai.Transcriber()

        transcript = transcriber.transcribe(audio)
        
        srt = transcript.export_subtitles_srt().split("\n")
        #with open("assets/test_audio/test_srt.txt", "r", encoding="utf-8") as file:
            #srt = file.readlines()
        texts = srt[2::4]
        times = srt[1::4]
        return [(_retrieve_time(time), text) for time, text in zip(times, texts)]


    
        


    


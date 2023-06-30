from gtts import gTTS
import re
from transformers import Tool


def generate_voice(file_name,content, language):
    speed = 1  # Adjust the speed (default: 1.0)
    # Add punctuation marks to the input text
    text_with_punctuation = " ".join(re.findall(r"\w+|[^\w\s]", content))

    # Generate the voice with adjusted speed
    summary_voice = gTTS(text=text_with_punctuation, lang=language, slow=False)

    # Adjust the speed of the voice by manipulating the text duration
    summary_voice.speed = speed
    # Save the voice as an audio file
    audio_file_name = f"{file_name}.mp3"
    summary_voice.save(audio_file_name)
    return audio_file_name


class text_to_speech(Tool):
    name = "text_to_speech_tool"
    description = "This is a tool for generating mp3 format audio for a text file content. It takes three inputs named `file_name`, `content` and the `language`. It converts the text to audio in selected language nd saves the file in mp3 format with name `file_name.mp3`."
    input = ["text", "text","text"]
    outputs = ["audio"]

    def __call__(self, file_name: str,content: str, language: str):
        return generate_voice(file_name, content, language)


text_to_speech_tool = text_to_speech()

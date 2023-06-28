from gtts import gTTS
import re
import readPDF as fileReader
from transformers import Tool


def generate_voice(file_name, language):
    # read the file content:
    content = fileReader(file_name)
    speed = 1  # Adjust the speed (default: 1.0)
    # Add punctuation marks to the input text
    text_with_punctuation = " ".join(re.findall(r"\w+|[^\w\s]", content))

    # Generate the voice with adjusted speed
    summary_voice = gTTS(text=text_with_punctuation, lang=language, slow=False)

    # Adjust the speed of the voice by manipulating the text duration
    summary_voice.speed = speed
    # Save the voice as an audio file
    summary_voice.save(f"{file_name}.mp3")


class text_to_speech(Tool):
    name = "text_to_speech_tool"
    description = "This is a tool for generating audio for a text file content. It takes an input named `file_name` and the `language`. It reads through the document and returns the audio file in mp3 format."
    input = ["text"]
    outputs = ["audio"]

    def __call__(self, file_name: str, language: str):
        return generate_voice(file_name, language)


text_to_speech_tool = text_to_speech()

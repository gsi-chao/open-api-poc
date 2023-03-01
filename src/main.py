import os
from dotenv import load_dotenv

import openai

from record_audio import record_audio

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = API_KEY


def get_capabilities():
    # Initialize the OpenAI AI engine
    # Get the model list
    result = openai.Model.list()
    print(result)


def exec_chat_completion(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    print(completion.choices[0].message)


def test_wispers():
    audio_file = open("file.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript.text


def fix_spelling_mistakes(text):
    response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=text,
        instruction="Fix the spelling mistakes"
    )
    print(response.choices[0].text)


if __name__ == '__main__':
    # recording audio
    # record_audio('file.wav', 10)

    # audio to text and text to chatgpt
    # text = test_wispers()
    # exec_chat_completion(text)

    # fix spelling mistakes
    fix_spelling_mistakes(
        'Areglar este testo para comprobar si funciona corectamente')

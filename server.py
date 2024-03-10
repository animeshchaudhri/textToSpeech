from flask import Flask, request, send_file, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file
@app.route('/get-audio/<filename>')
def get_audio(filename):
    # Serve the audio file
    return send_file(filename, as_attachment=True)

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text', '')
    lang = data.get('lang', 'en')

    audio_file = text_to_speech(text, lang)

    audio_file = text_to_speech(text, lang)
    response_data = {
        'message': 'Speech generated successfully.',
        'audio_link': f'http://127.0.0.1:5000/get-audio/{audio_file}'
    }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)

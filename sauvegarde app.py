import os 
import uuid 
import flask 
from flask import Flask, flash, request, redirect
from pydub import AudioSegment

AudioSegment.converter = r"C:/Users/mbodj/Downloads/ffmpeg-6.1.1/ffmpeg-6.1.1/fftools"
UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'mp3'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/save-record', methods=['POST'])
def save_record():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']

    # If the user does not select a file, browser submits an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Check if the file has an allowed extension
    if not allowed_file(file.filename):
        flash('Invalid file type. Allowed types: mp3')
        return redirect(request.url)

    # Generate a unique filename using UUID
    file_name = str(uuid.uuid4()) + ".mp3"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

    # Remove previous audio files
    for existing_file in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], existing_file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Save the new file
    file.save(full_file_name)
    print("............: ",file.name)
    try:
        # Load the audio using pydub
        print("file_name..........", file_name)
        audio = AudioSegment.from_file("./files/"+file_name)

        # Export the audio to WAV format
        wav_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audio_wolof.wav')
        audio.export(wav_path, format="wav")

        # Load the WAV file using torchaudio
       # audio, _ = torchaudio.load(wav_path, normalize=True)
    except Exception as exc:
        print(f"Error loading audio file: {exc}")
        return '<h1>Error</h1>'


    return '<h1>Success</h1>'


if __name__ == '__main__':
    app.run()

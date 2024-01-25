import os 
# Remove previous audio files
for existing_file in os.listdir(app.config['UPLOAD_FOLDER']):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], existing_file)
    if os.path.isfile(file_path):
        os.remove(file_path)

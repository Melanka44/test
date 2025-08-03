from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER_MUSIC'] = 'static/music'
app.config['UPLOAD_FOLDER_COVERS'] = 'static/covers'

@app.route('/')
def index():
    music_files = os.listdir(app.config['UPLOAD_FOLDER_MUSIC'])
    songs = []
    for filename in music_files:
        name = os.path.splitext(filename)[0]
        cover_path = f"covers/{name}.jpg" if f"{name}.jpg" in os.listdir(app.config['UPLOAD_FOLDER_COVERS']) else "covers/default.jpg"
        songs.append({
            'name': name,
            'file': f"music/{filename}",
            'cover': cover_path
        })
    return render_template("index.html", songs=songs)

@app.route('/upload', methods=['POST'])
def upload():
    music = request.files['music']
    cover = request.files['cover']

    if music:
        music_filename = secure_filename(music.filename)
        name_no_ext = os.path.splitext(music_filename)[0]
        music.save(os.path.join(app.config['UPLOAD_FOLDER_MUSIC'], music_filename))

        if cover:
            cover_filename = name_no_ext + ".jpg"
            cover.save(os.path.join(app.config['UPLOAD_FOLDER_COVERS'], cover_filename))

    return redirect(url_for('index'))

@app.route('/delete/<song_name>', methods=['POST'])
def delete(song_name):
    music_path = os.path.join(app.config['UPLOAD_FOLDER_MUSIC'], f"{song_name}.mp3")
    cover_path = os.path.join(app.config['UPLOAD_FOLDER_COVERS'], f"{song_name}.jpg")

    if os.path.exists(music_path):
        os.remove(music_path)
    if os.path.exists(cover_path):
        os.remove(cover_path)

    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs('static/music', exist_ok=True)
    os.makedirs('static/covers', exist_ok=True)
    app.run(debug=True)

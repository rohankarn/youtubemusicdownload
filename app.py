from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

AUDIO_DOWNLOAD_DIR = r""

def download_audio(video_url):
    try:
        video = YouTube(video_url)
        audio = video.streams.filter(only_audio=True).first()
        audio.download(AUDIO_DOWNLOAD_DIR)
        return True
    except Exception as e:
        print(f"Failed to download audio: {str(e)}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        if video_url:
            if download_audio(video_url):
                return render_template('index.html', message="Audio downloaded successfully!")
            else:
                return render_template('index.html', error="Failed to download audio. Please check the URL.")
        else:
            return render_template('index.html', error="Please enter a valid YouTube video URL.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)


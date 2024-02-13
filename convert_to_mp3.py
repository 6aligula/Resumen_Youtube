# Paso 1: Ya lo tienes cubierto con el código de yt_dlp para descargar el audio.
from yt_dlp import YoutubeDL

def descargar_audio(video_url):
    # Configuración de yt_dlp para descargar solo el audio y convertirlo a mp3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'input.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Uso de yt_dlp con las opciones definidas para descargar el audio
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

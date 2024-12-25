import os
import yt_dlp
import shutil

# Caminho para salvar os downloads
download_folder = './Musicas'

# Caminho completo para o executável FFmpeg
ffmpeg_path = shutil.which('ffmpeg')

def baixar_mp3():
    if not ffmpeg_path:
        os.system('cls')
        input('FFmpeg não encontrado, verifique se esteja instalado')
        return
        
    
    # Certifique-se de que o diretório de download existe
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    print('Cole o link da música ou playlist')
    url = input('->  ')


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    }

    # Download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        raise RuntimeError(f"Erro ao baixar o áudio: {e}")


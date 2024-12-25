import os
import yt_dlp
import shutil

# Caminho para salvar os downloads
download_folder = './Musicas'

# Caminho completo para o executável FFmpeg
ffmpeg_path = shutil.which('ffmpeg')

def baixar_mp3(link, progress_callback=None):
    if not link.strip():
        raise ValueError("O link fornecido é inválido.")
    
    if not ffmpeg_path:
        raise EnvironmentError("FFmpeg não foi encontrado no sistema.")
    
    # Certifique-se de que o diretório de download existe
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Configuração para obter informações do vídeo ou playlist
    ydl_opts_info = {
        'quiet': True,
        'extract_flat': False,  # Precisamos das informações completas da playlist
    }

    # Obter informações de quantos vídeos serão baixados
    try:
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(link, download=False)
            if 'entries' in info:
                # Se for uma playlist, contar os itens
                total_musicas = len(info['entries'])
            else:
                # Se for um vídeo único
                total_musicas = 1
    except Exception as e:
        raise RuntimeError(f"Erro ao obter informações: {e}")

    # Notificar a interface sobre o total de músicas
    if progress_callback:
        progress_callback({
            'status': 'info',
            'message': f"Total de músicas na fila: {total_musicas}",
            'total': total_musicas,
        })

    # Configuração para download
    musica_atual = {"baixadas": 0}  # Contador compartilhado para músicas baixadas
    def progress_hook(data):
        status = data.get('status')
        if status == 'downloading':
            # Exibe o progresso da música atual
            percent = data.get('_percent_str', '').strip()
            speed = data.get('_speed_str', '').strip()
            eta = data.get('eta', '---')
            title = data.get('info_dict', {}).get('title', '---')
            progress_callback({
                'status': 'downloading',
                'title': title,
                'percent': percent,
                'speed': speed,
                'eta': eta,
                'atual': musica_atual['baixadas'],
                'total': total_musicas,
            })
        elif status == 'finished':
            # Atualiza o contador ao finalizar
            musica_atual['baixadas'] += 1
            progress_callback({
                'status': 'finished',
                'atual': musica_atual['baixadas'],
                'total': total_musicas,
            })

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
    }

    # Download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as e:
        raise RuntimeError(f"Erro ao baixar o áudio: {e}")


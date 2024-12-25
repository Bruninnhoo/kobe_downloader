import threading
import customtkinter as ctk
from downloader import baixar_mp3

def iniciar_download(link, output_area):
    def progress_callback(data):
        if data['status'] == 'info':
            # Informações gerais (total de músicas)
            output_area.insert("end", f"{data['message']}\n")
        elif data['status'] == 'downloading':
            # Informações do progresso
            output_area.insert(
                "end",
                f"Baixando {data['title']} ({data['atual'] + 1}/{data['total']}) - {data['percent']} "
                f"- {data['speed']} - ETA: {data['eta']}s\n"
            )
        elif data['status'] == 'finished':
            # Música finalizada
            output_area.insert(
                "end",
                f"Música {data['atual']} de {data['total']} baixada com sucesso!\n"
            )
        output_area.see("end")

    try:
        if not link.strip():
            output_area.insert("end", "Por favor, insira um link válido.\n")
            return

        output_area.insert("end", "Analisando o link...\n")
        output_area.see("end")

        # Iniciar o download em uma thread separada
        threading.Thread(target=baixar_mp3, args=(link, progress_callback)).start()
    except Exception as e:
        output_area.insert("end", f"Erro: {e}\n")
        output_area.see("end")



# Configuração da interface gráfica
def criar_interface():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.title("Downloader de Música")
    janela.geometry("600x400")

    # Widgets da interface
    titulo = ctk.CTkLabel(janela, text="Downloader de Música", font=("Arial", 20))
    titulo.pack(pady=10)

    entrada = ctk.CTkEntry(janela, placeholder_text="Insira o link aqui", width=400)
    entrada.pack(pady=10)

    output_area = ctk.CTkTextbox(janela, height=200, width=500)
    output_area.pack(pady=10)

    botao = ctk.CTkButton(
        janela,
        text="Iniciar Download",
        command=lambda: iniciar_download(entrada.get(), output_area)
    )
    botao.pack(pady=10)

    # Iniciar o loop da aplicação
    janela.mainloop()

if __name__ == "__main__":
    criar_interface()

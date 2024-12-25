Kobe Music

O que esse aplicativo faz?
R: Serve para baixar música .mp3 usando links do youtube

Ele precisa de algo para rodar o aplicativo?
R: Sim, precisa do FFmpeg(Coder) e Python 3.13.0

Como baixar as depencias acima?
R: FFmpeg{

    1. Entre no site oficial do FFmpeg(https://ffmpeg.org/download.html#build-windows) e baixe a versão Windows 
    by BtbN https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
    
    2. Vá no disco local C: e crie uma pasta chamada "ffmpeg" e extraia o conteudo baixado dentro dele

    3. Vá até a pasta "bin" do ffmpeg e copie a url/link da pasta
    
    4. Digite na área de busca "Editar variáveis de ambiento do sistema", em seguida clique na opção "Variaveis
    de ambiente"

    5. Na área "Variaveis do sistema" clique duas vezes na variavel chamada "Path"

    6. Clique no botão "Novo" e cole o que copiou na pasta e clique em OK

    Pronto esta instalado! Caso queira ter certeza que esteja, Digite "Prompt de comando" e abre o aplicativo,
    digite o comando "ffmpeg -version", se aparecer alguma coisa que o comando não foi reconhecido ou algo
    semelhante, verifique se foi instalado direito
}
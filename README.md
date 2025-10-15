# 🎬 Unir MP3 e Converter para MP4

Este script **Python interativo** automatiza a tarefa de juntar múltiplos arquivos `.mp3` dentro de uma pasta e convertê-los em um único arquivo de vídeo `.mp4` com uma **tela preta de fundo**.

É ideal para criar rapidamente vídeos simples de **podcasts**, **áudios longos** ou **listas de reprodução** para plataformas que exigem o formato de vídeo.

O projeto inclui uma **verificação de espaço em disco** para evitar falhas de conversão e permite selecionar um **novo destino** para o arquivo de saída se o espaço na pasta original for insuficiente.

## ⚙️ Requisitos

Para que o script funcione, você deve ter os seguintes itens instalados no seu sistema:

- **Python 3**: O script é escrito em Python.  
- **FFmpeg**: O script utiliza o FFmpeg para a concatenação e conversão. Ele deve estar instalado e acessível no PATH do sistema.

### 🔍 Verificação de FFmpeg

Ao iniciar, o script verifica automaticamente a presença do FFmpeg.  
Se ele não for encontrado, uma mensagem de erro será exibida e o script será encerrado.

## 🚀 Como Usar

O script é projetado para ser executado no diretório onde estão localizadas as suas pastas de áudio.

### 1. Organização dos Arquivos

Antes de executar, organize seus arquivos:

- Crie uma **pasta** para cada vídeo que deseja gerar (ex: `MeuPodcast_Ep1`, `Musicas_Parte1`).
- Coloque todos os arquivos `.mp3` que deseja unir dentro dessa pasta.
- **Importante:** Os arquivos MP3 serão concatenados em **ordem alfabética/numérica**.  
  Garanta que seus arquivos estejam nomeados corretamente (ex:  
  `01_intro.mp3`, `02_meio.mp3`, `03_final.mp3`).

### 2. Execução do Script

- Abra o **terminal** ou **prompt de comando**.  
- Navegue até o diretório que contém as pastas de áudio.  
- Execute o script Python:

```bash
python unir_mp3_para_mp4_interativo.py
```

### 3. Interação

O script irá guiá-lo interativamente:

- Ele listará todas as pastas (subdiretórios) encontradas no diretório atual.  
- Selecione a pasta digitando o número correspondente.  
- O script verificará o espaço livre em disco e fará uma estimativa de quanto espaço é necessário.  
- Se o espaço for insuficiente, ele perguntará se você deseja especificar um novo caminho de destino para o arquivo `.mp4` final.  
- A conversão será iniciada.  
  O vídeo final terá o nome da pasta selecionada (ex: `MeuPodcast_Ep1.mp4`).

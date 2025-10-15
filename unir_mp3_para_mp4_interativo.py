import os
import sys
import subprocess
import shutil

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("❌ ERRO: FFmpeg não encontrado!")
        print("Por favor, instale o FFmpeg e garanta que ele esteja no PATH do sistema.")
        sys.exit(1)
    print("✅ FFmpeg encontrado.")

def espaco_livre_mb(caminho="."):
    try:
        _, _, livre = shutil.disk_usage(caminho)
        return livre // (1024 * 1024)
    except FileNotFoundError:
        return 0

def selecionar_pasta():
    limpar_tela()
    print("=== Unir MP3 e Converter para MP4 (Verificação de Espaço) ===\n")

    pastas = [p for p in os.listdir('.') if os.path.isdir(p)]
    if not pastas:
        print("⚠️ Nenhuma pasta encontrada no diretório atual.")
        return None

    for i, pasta in enumerate(pastas, start=1):
        print(f"{i}. {pasta}")

    print("\nEscolha o número da pasta:")
    escolha = input("> ").strip()
    if not escolha.isdigit() or not (1 <= int(escolha) <= len(pastas)):
        print("❌ Opção inválida!")
        input("Pressione ENTER para continuar...")
        return selecionar_pasta()

    return pastas[int(escolha) - 1]

def converter_direto_para_mp4(pasta):
    limpar_tela()
    print(f"🎬 Processando pasta: '{pasta}'...\n")
    caminho_absoluto_pasta = os.path.abspath(pasta)

    arquivos_mp3 = sorted([f for f in os.listdir(caminho_absoluto_pasta) if f.lower().endswith('.mp3')])
    if not arquivos_mp3:
        print("⚠️ Nenhum arquivo MP3 encontrado nesta pasta.")
        input("Pressione ENTER para continuar...")
        return

    # Cria lista para o FFmpeg
    caminho_lista = os.path.join(caminho_absoluto_pasta, "lista_temp.txt")
    with open(caminho_lista, 'w', encoding='utf-8') as f:
        for mp3 in arquivos_mp3:
            caminho_completo = os.path.join(caminho_absoluto_pasta, mp3).replace("'", "'\\''")
            f.write(f"file '{caminho_completo}'\n")

    nome_base = os.path.basename(caminho_absoluto_pasta)
    saida_mp4 = os.path.join(caminho_absoluto_pasta, f"{nome_base}.mp4")

    # Verifica espaço livre antes de iniciar
    espaco_disp = espaco_livre_mb(caminho_absoluto_pasta)
    tamanho_total_mp3 = sum(os.path.getsize(os.path.join(caminho_absoluto_pasta, a)) for a in arquivos_mp3) // (1024 * 1024)
    estimado = int(tamanho_total_mp3 * 1.4)

    print(f"💾 Espaço livre: {espaco_disp} MB")
    print(f"📦 Estimado necessário: {estimado} MB")

    if espaco_disp < estimado:
        print("\n⚠️ Espaço insuficiente!")
        print("Deseja salvar o vídeo em outro local (ex: /sdcard/Movies)? (s/n)")
        if input("> ").strip().lower() == "s":
            novo_destino = input("\nDigite o novo caminho de destino:\n> ").strip()
            if not os.path.exists(novo_destino):
                os.makedirs(novo_destino, exist_ok=True)
            saida_mp4 = os.path.join(novo_destino, f"{nome_base}.mp4")
            print(f"📁 Novo destino configurado: {saida_mp4}")
        else:
            print("\n❌ Conversão cancelada para evitar falha.")
            os.remove(caminho_lista)
            input("Pressione ENTER para continuar...")
            return

    comando = [
        'ffmpeg',
        '-f', 'concat', '-safe', '0', '-i', caminho_lista,
        '-f', 'lavfi', '-i', 'color=black:s=256x144:r=1',
        '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '35',
        '-c:a', 'aac', '-b:a', '96k',
        '-shortest', '-y', saida_mp4
    ]

    try:
        print("\n▶️ Executando FFmpeg (otimizado, 1fps, compressão leve)...")
        subprocess.run(comando, check=True)
        print(f"\n✅ Conversão concluída!\n📁 Arquivo final: {saida_mp4}")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro final na conversão: {e}")
        print("💡 Diagnóstico: Espaço em disco insuficiente ou caminho inacessível.")
    finally:
        if os.path.exists(caminho_lista):
            os.remove(caminho_lista)
            print("🗑️ Lista temporária removida.")

def main():
    limpar_tela()
    verificar_ffmpeg()

    while True:
        pasta = selecionar_pasta()
        if not pasta:
            break

        converter_direto_para_mp4(pasta)

        print("\nDeseja processar outra pasta? (s/n)")
        if input("> ").strip().lower() != "s":
            break

    print("\n👋 Processo finalizado. Até a próxima!")

if __name__ == "__main__":
    main()
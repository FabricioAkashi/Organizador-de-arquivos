import os
import shutil

pasta_alvo = r'C:\Users\SeuUsuario\Downloads'

categorias = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.doc'],
    'Vídeos': ['.mp4', '.avi', '.mov'],
    'Planilhas': ['.xls', '.xlsx', '.csv'],
    'Executáveis': ['.exe', '.msi'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Outros': []
}

for categoria in categorias:
    caminho = os.path.join(pasta_alvo,categoria)
    if not os.path.exists(caminho):
        os.mkdir(caminho)

for arquivo in os.listdir(pasta_alvo):
    caminho_arquivo = os.path.join(pasta_alvo,arquivo)

    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)
        movido = False

        for categoria, extensoes in categorias.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(pasta_alvo, categoria, arquivo)
                shutil.move(caminho_arquivo, destino)
                movido = True
                break

        if not movido:
            destino = os.path.join(pasta_alvo, 'Outros', arquivo)
            shutil.move(caminho_arquivo, destino)
            
print("Arquivos movidos com sucesso!")

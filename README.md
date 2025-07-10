# 🗂️ Organizador de arquivos

Este projeto é um script simple desenvolvido em python com a finalidade de organizar pastas (como 'Downloads') automáticamente ao ser executado.

## 📌 Funcionalidades

- Move arquivos automaticamente para categorias como: Imagens, Documentos, Vídeos, Planilhas, etc.
- Cria as subpastas, caso ainda não existam.
- Se o tipo do arquivo não for reconhecido, ele é movido para a pasta `Outros`.

## 🚀 Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. **Altere o caminho para pasta alvo**

  No arquivo index.py, edite a variável pasta_alvo com o caminho da pasta que deseja organizar:

  pasta_alvo = r'C:\Users\SeuUsuario\Downloads' 

3. **Execute o script**
   python index.py

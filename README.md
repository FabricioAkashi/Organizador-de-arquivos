# 🗂️ Organizador de arquivos

Este projeto é um script simple desenvolvido em python com a finalidade de organizar pastas (como 'Downloads') automáticamente ao ser executado.

## 📌 Funcionalidades

- Move arquivos automaticamente para categorias como: Imagens, Documentos, Vídeos, Planilhas, etc.
- Cria as subpastas, caso ainda não existam.
- Se o tipo do arquivo não for reconhecido, ele é movido para a pasta `Outros`.

## 🚀 Como usar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/fabricioakashi/organizador-arquivos.git
   ```

2. **Instale o Python** (caso ainda não tenha):
   - https://www.python.org/downloads/

3. **Edite o caminho da pasta a ser organizada:**

   No arquivo `index.py`, modifique a variável `pasta_alvo` com o caminho da sua pasta:
   ```python
   pasta_alvo = r'C:\Users\SeuUsuario\Downloads'
   ```

4. **Execute o script:**
   ```bash
   python index.py
   ```

5. Os arquivos serão movidos automaticamente para pastas como:
   - `Imagens`
   - `Documentos`
   - `Planilhas`
   - `Vídeos`
   - `Executáveis`
   - `Compactados`
   - `Outros`

---

## 🧰 Tecnologias utilizadas

- Python 3.x
- Bibliotecas padrão: `os`, `shutil`

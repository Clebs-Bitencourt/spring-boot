from pathlib import Path
import zipfile

# Cria a estrutura de pastas e arquivos para o projeto Flask do "Palácio da Memória"
base_dir = Path("/mnt/data/palacio_memoria")
templates_dir = base_dir / "templates"
static_dir = base_dir / "static" / "imagens"

# Criar diretórios
templates_dir.mkdir(parents=True, exist_ok=True)
static_dir.mkdir(parents=True, exist_ok=True)

# Conteúdo do app.py
app_py_content = """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sala/<int:numero>')
def sala(numero):
    imagem = f"/static/imagens/sala{numero}.png"
    texto = f"Esta é a descrição da sala {numero} no seu Palácio da Memória."
    return render_template('sala.html', numero=numero, imagem=imagem, texto=texto)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
"""

# Conteúdo do index.html
index_html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Palácio da Memória</title>
</head>
<body>
    <h1>Palácio da Memória</h1>
    <h2>Escolha uma sala:</h2>
    <ul>
        {% for i in range(1, 5) %}
            <li><a href="/sala/{{ i }}">Sala {{ i }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# Conteúdo do sala.html
sala_html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Sala {{ numero }}</title>
</head>
<body>
    <h1>Sala {{ numero }}</h1>
    <img src="{{ imagem }}" alt="Imagem da sala {{ numero }}" style="width:300px;height:auto;">
    <p>{{ texto }}</p>
    <a href="/">Voltar ao Palácio</a>
</body>
</html>
"""

# Criar os arquivos
(base_dir / "app.py").write_text(app_py_content, encoding="utf-8")
(templates_dir / "index.html").write_text(index_html_content, encoding="utf-8")
(templates_dir / "sala.html").write_text(sala_html_content, encoding="utf-8")

# Criar imagens de exemplo vazias
for i in range(1, 5):
    (static_dir / f"sala{i}.png").write_bytes(b"")  # Placeholder vazio

# Criar um arquivo zip para download
zip_path = "/mnt/data/palacio_memoria.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for path in base_dir.rglob("*"):
        zipf.write(path, path.relative_to(base_dir.parent))

zip_path

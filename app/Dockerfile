# Usamos uma imagem Python como base
FROM python:3

# Copiar o arquivo Python para o diretório de trabalho do contêiner (/app)
COPY app.py /app/

# Define o diretório de trabalho como /app
WORKDIR /app

# Instala as dependências do script Python
RUN pip install scikit-learn pandas flask

# Verifica se o arquivo modelo.pkl existe em /app e, se existir, executa o comando padrão
CMD ["sh", "-c", "if [ -f /compartilhado/modelo.pkl ]; then python app.py; fi"]

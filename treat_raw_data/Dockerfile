# Usamos uma imagem Python como base
FROM python:3

# Copiar os arquivos Python para o diretório de trabalho do contêiner (/train_model)
COPY treat_raw_data.py /treat_raw_data/
COPY requisicoes.csv /compartilhado/

# Define o diretório de trabalho como /train_model
WORKDIR /treat_raw_data

# Instale dependências adicionais (se necessário)
RUN pip install pandas

# Comando para treinar o modelo e mover o arquivo gerado para a pasta compartilhada
CMD python treat_raw_data.py && \
    if [ -f "base_treinamento.csv" ]; then \
        mv base_treinamento.csv /compartilhado/; \
    fi

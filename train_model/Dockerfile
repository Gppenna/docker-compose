# Usamos uma imagem Python como base
FROM python:3

# Copiar os arquivos Python para o diretório de trabalho do contêiner (/train_model)
COPY train_model.py /train_model/


# Define o diretório de trabalho como /train_model
WORKDIR /train_model

# Instale dependências adicionais (se necessário)
RUN pip install numpy pandas tqdm scikit-learn xgboost

# Comando para treinar o modelo e mover o arquivo gerado para a pasta compartilhada
CMD ["sh", "-c", "if [ -f /compartilhado/base_treinamento.csv ]; then python train_model.py; fi && \
                  if [ -f modelo.pkl ]; then mv modelo.pkl /compartilhado/; fi"]
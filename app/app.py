import pickle
import pandas as pd

# Carregar o modelo treinado
with open('/compartilhado/modelo.pkl', 'rb') as arquivo:
    model = pickle.load(arquivo)

def prever():
  # Obter os dados da requisição em formato JSON
  json_data = {
    "0": [1.0],
    "1": [0.0],
    "2": [0.916073],
    "3": [0.9125],
    "4": [0.253514],
    "5": [0.861702],
    "6": [1.0]
  }

  df_test = pd.DataFrame(json_data)

  print(df_test)

  # Fazer a previsão usando o modelo carregado
  previsao = model.predict(df_test)

  # Retornar a previsão em formato JSON
  print('Previsão (1: Aceita, 0: Bloqueia): ', previsao)

if __name__ == '__main__':
    prever()

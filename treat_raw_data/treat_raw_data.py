import pandas as pd

# Defina o caminho do arquivo CSV
caminho_arquivo_csv = '/compartilhado/requisicoes.csv'  # Substitua pelo caminho real do arquivo CSV

dataRaw = pd.read_csv(caminho_arquivo_csv, on_bad_lines='skip', sep=",")
dataRaw = dataRaw.sample(frac=1, random_state=42).reset_index(drop=True)

dataRaw = dataRaw.loc[dataRaw['Erlang'] >= 40]

dataBlock = dataRaw.loc[dataRaw['Aceita']==0,]

dataNotBlock = dataRaw.loc[dataRaw['Aceita']==1,]

dataConcatenado = pd.concat([dataBlock, dataNotBlock])

dataRefinado = dataConcatenado.drop([
 'ArrivalTime',
 'Path',
 'PathBkp',
 'SlotsAlocados',
 'SlotsAlocadosBkp',
 'SlotsAdicionaisBkp',
 'Duracao',
 'DuracaoBkp',
 'TimeBkp',
 'HoldingSlotPrim',
 'HoldingSlotBkp',
 'EstrAllocate',
 'TimeSimulacao',
 'Time',
 'Repli',
 'idReq'
], axis=1)

dataRefinadoNew = dataRefinado.drop([
 'NumLinkPath',
 'Source',
 'Destination',
 'NumLinkBkp',
 'NumSlots',
 'NumSlotsBkp',
 'SlotsPathUtil',
 'UtilizacaoPath',
 'DispPath',
 'DispPathBkp'
], axis=1)

name = 'base_treinamento.csv'
dataRefinadoNew.to_csv(name, index=False)
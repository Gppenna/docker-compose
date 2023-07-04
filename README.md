# docker-compose

Para o funcionamento, baixe o CSV https://drive.google.com/drive/folders/16I0P7Gb3tB70kdKCWCx9PcGP5aMQEOWX?usp=sharing

Coloque o CSV na pasta de raw data.

Para build e execução da imagem Jenkins execute: 
```
docker-compose -f docker-compose-jenkins.yml up -d
```

Para build e execução das imagens de tratamento dos dados, treinamento do modelo e API de predição: 
```
docker-compose -f docker-compose.yml up -d
```

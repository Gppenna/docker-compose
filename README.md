# docker-compose

Link para o relatório: https://docs.google.com/document/d/1XqMknw4WoxfroAbXLVDI1A5fodR3pDD2j7cn84_fpIE/edit?usp=sharing

Link para slide do ciclo de vida MLOps: https://docs.google.com/presentation/d/12dGEZVKkjzFh6JAW1-CsyFOOUSu-YyAZWPLeRxn_gNE/edit?usp=sharing

Para o funcionamento siga os passos abaixo

Para build e execução da imagem Jenkins execute na ordem:

```
docker network create jenkins
```

```
docker run --name jenkins-docker --rm --detach ^
  --privileged --network jenkins --network-alias docker ^
  --env DOCKER_TLS_CERTDIR=/certs ^
  --volume jenkins-docker-certs:/certs/client ^
  --volume jenkins-data:/var/jenkins_home ^
  --publish 2376:2376 ^
  docker:dind
```

```
docker build -t myjenkins-blueocean:2.401.2-1 .
```

```
docker run --name jenkins-blueocean --restart=on-failure --detach ^
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 ^
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 ^
  --volume jenkins-data:/var/jenkins_home ^
  --volume jenkins-docker-certs:/certs/client:ro ^
  --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.401.2-1
```

Para configuração da pipeline no Jenkins, configure um novo job de pipeline utilizando o Jenkinsfile neste repositório.

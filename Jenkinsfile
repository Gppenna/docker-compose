pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build e Execução') {
      steps {
        sh 'docker-compose up --build -d'
      }
    }
  }
}

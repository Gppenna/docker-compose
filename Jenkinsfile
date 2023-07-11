pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Limpar Docker') {
      steps {
        sh 'docker system prune -a --volumes -f'
      }
    }

    stage('Iniciar Container') {
      steps {
        sh 'docker compose up -d'
        sh 'docker compose ps'
      }
    }
  }
}

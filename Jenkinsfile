pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Iniciar Container') {
      steps {
        sh 'docker version'
        sh 'docker compose version'
      }
    }
  }
}

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

    stage('Build dos Containeres') {
      steps {
        sh 'docker compose build' 
        sh 'docker compose ps'
      }
    }

    stage('Iniciar Container - treat_raw_data') {
      steps {
        sh 'docker compose up -d --wait treat_raw_data' 
        sh 'docker wait treat_raw_data'
      }
    }

    stage('Iniciar Container - train_model') {
      steps {
        sh 'docker compose up -d --wait train_model' 
        sh 'docker wait train_model'
        sh 'docker logs app'
      }
    }

    stage('Iniciar Container - app') {
      steps {
        sh 'docker compose up -d --wait app' 
        sh 'docker wait app'
        sh 'docker logs app'
      }
    }
  }
}

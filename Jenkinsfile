pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/CybeSami/hello.git'
                }
            }
        }
        stage('Setup') {
            steps {
                script {
                    // Créer un environnement virtuel
                    sh 'python3 -m venv venv'
                    // Activer l'environnement virtuel et installer les dépendances
                   sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'source venv/bin/activate && python3 helloworld.py'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Aucun test pour le moment'
            }
        }
    }
}

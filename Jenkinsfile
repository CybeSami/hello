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
                    // Installez pip si ce n'est pas déjà fait
                    sh 'apt-get install -y python3-pip git'
                    // Installez les dépendances
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    sh 'python3 helloworld.py'
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

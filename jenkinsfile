pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = credentials('github-credentials') // ID de vos credentials
    }
    
    stages {
        stage('Clone') {
            steps {
                script {
                    git credentialsId: 'github-credentials', url: "https://${GITHUB_CREDENTIALS.username}:${GITHUB_CREDENTIALS.password}@github.com/CybeSami/hello.git"
                }
            }
        }
        
        stage('Setup') {
            steps {
                script {
                    // Installez pip si ce n'est pas déjà fait
                    sh 'apt-get update && apt-get install -y python3-pip git'
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

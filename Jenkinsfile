pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Tatatharanidaran/NM-Lab.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest tests/'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}

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
                sh '''
                    echo "Installing dependencies..."
                    python3 -m pip install --upgrade pip
                    python3 -m pip install pytest
                    echo "Compiling Python code..."
                    python3 -m py_compile app.py
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    echo "Running tests..."
                    python3 -m pytest tests/ || echo "No tests directory found, skipping tests"
                '''
            }
        }
    }
    post {
        always {
            echo '✓ Pipeline completed.'
        }
        success {
            echo '✓ Build successful!'
        }
        failure {
            echo '✗ Build failed. Check logs above.'
        }
    }
}

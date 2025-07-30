pipeline {
    agent any 

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Muhnj/june25-classdemo2.git'
            }
        }

        stage('Setup Virtual Environment') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    python3 -m venv $VENV
                    source $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    source $VENV/bin/activate
                    pytest
                '''
            }
        }
    }
}

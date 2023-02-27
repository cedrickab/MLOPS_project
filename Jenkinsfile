/* Requires the Docker Pipeline plugin , blue ocean plugin & ssh agent puglin & git plugin  */

pipeline {
       
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS= credentials('dockerhubcredentials')
    }   

    stages {
        stage('Checkout') {
            steps {
                git branch: 'arthy', credentialsId: 'github_ssh', url: 'https://github.com/cedrickab/MLOPS_project.git'
            }
        }   
        stage('Build Backend Image') {
            steps {
                dir('backend') {
                    sh 'pip install -r requirements.txt'
                    sh 'docker build -t arthy05/projet_mlops_backend:latest .'
                }
            }
        }
        stage('Build Frontend Image') {
            steps {
                    sh 'pip install -r requirements.txt'
                    sh 'docker build -t arthy05/projet_mlops_frontend:latest .'
                  }
            }
        
        stage('Login to Docker Hub') {
            steps {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        
        stage('Push Images to Docker Hub'){
            steps {
                    sh 'docker push arthy05/projet_mlops_backend:latest'
                    sh 'docker push arthy05/projet_mlops_frontend:latest'
            }
        }
        
        stage('Deploy') {
            steps {
                sshagent(credentials: ['github_ssh']) {
                                sh '''
                                     cd C:/Users/Arthy/Desktop/Project_MLOPS/
                                     docker-compose build
                                     docker-compose up -d
                                   '''

                }
            }
        }
    }
}

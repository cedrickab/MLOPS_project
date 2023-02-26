/* Requires the Docker Pipeline plugin , blue ocean plugin & ssh agent puglin & git plugin  */


pipeline {
    agent any
    
    environment {
        PATH = "C:\\WINDOWS\\SYSTEM32;C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python37-32;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\mingw64\\bin;C:\\Program Files\\Git\\usr\\bin"
        }
    
    stages {
           stage('connexion'){      
           steps {
                git branch: 'staging', credentialsId: 'SSH', url: 'git@github.com:cedrickab/RESTful-ml-endpoint.git'
                  }
                }
                  
        stage('Testing') {
            steps {
                bat 'python -m pip install Flask'
                bat 'python -m pip install numpy'
                bat 'python -m pip install pandas'
                bat 'python -m pip install scikit-learn==1.0.2'
                bat 'python Test.py'
            }
        }
        stage('retrain_model') {
            steps {
                // bat 'python -m pip install dill'
                bat 'python model.py'
                bat 'python retrain.py fashion-mnist-train-2.csv'
            }
        }
        stage('building and running image') {
            steps {
                // build a Docker image
                bat 'docker build -t endpointmlops .'
                // run a Docker container from the image
                bat 'docker run -d endpointmlops'
            }
        }
        stage('dockerhub and git') {
            environment {
                dockerpass = credentials('dockerhubaccount')
                gitpass = credentials('gitaccount')
                }
            parallel {
                stage("Build&push ") {
                    stages {
                        stage("dockerhub") {
                            agent any
                            steps {
                                //login
                                bat "docker login -u ${dockerpass_USR} -p ${dockerpass_PSW} "
                                // build a Docker image
                                bat 'docker image tag endpointmlops cedrickab/endpoint:myfirstimage'
                                // run a Docker container from the image
                                bat 'docker image push cedrickab/endpoint:myfirstimage'
                                }
                            }
                        }
                    }
                stage("git&push") {
                    stages {
                        stage("merge main branch") {
                            agent any
                            steps {
                                sshagent(credentials:['SSH']){
                                    bat 'git checkout staging'
                                    bat 'git add -A' 
                                    bat 'git commit --allow-empty -am "Merged staging branch into main"'
                                    bat 'git remote set-url origin git@github.com:cedrickab/RESTful-ml-endpoint.git'
                                    bat 'git checkout -b main'
                                    bat 'git pull'
                                    bat 'git merge origin/staging'
                                    // bat 'git commit -m "hello my commit message'
                                    bat 'git push origin main'
                                }
                        
                                }
                           }
                        }
                    }
                }
            }
        }
    }

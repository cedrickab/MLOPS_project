/* Requires the Docker Pipeline plugin , blue ocean plugin & ssh agent puglin & git plugin  */


pipeline {
    agent any
    
    environment {
        PATH = "C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python37-32;C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\mingw64\\bin;C:\\Program Files\\Git\\usr\\bin"
        }
    
    stages {
           stage('connexion'){      
           steps {
                git branch: 'cedric', credentialsId: 'SSH', url: 'git@github.com:cedrickab/MLOPS_project.git'
                  }
                }
                  
        stage('requirements') {
            steps {
                bat 'python.exe -m pip install --upgrade pip'
                bat 'python -m pip uninstall numpy'
                bat 'python -m pip install -r requirements.txt'
                // bat 'python -m pip install Flask'
                // bat 'python -m pip install numpy'
                // bat 'python -m pip install pandas'
                // bat 'python -m pip install scikit-learn==1.0.2'
                // bat 'python Test.py'
            }
        }
        stage('testing') {
            steps {
                bat 'python ML.py'
                bat 'python unitest.py'
                bat 'python -m locust -f stress_test.py --headless -u 10 -r 10 --run-time 1m --host http://127.0.0.1:5000'             
                
            }
        }
    }
}

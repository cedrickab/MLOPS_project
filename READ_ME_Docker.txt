Backend Dockerfile
cd C:\Users\Arthy\Desktop\Project_MLOPS\backend
Commande :
- docker build -t my-backend-image . 
- docker run -p 5000:5000 my-backend-image


Frontend Dockerfile
cd C:\Users\Arthy\Desktop\Project_MLOPS
- docker build -t my-frontend-image .
- docker run -p 4000:4000 my-frontend-image


Backend/FrontEnd/Promotheus/Graphana
Docker-compose
cd C:\Users\Arthy\Desktop\Project_MLOPS
- docker-compose up --build   

Avec Jenkinsfile il suffit de lancer le build
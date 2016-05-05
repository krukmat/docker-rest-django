docker-compose build web
docker-compose build nginx
docker-compose run generate_user
docker-compose up nginx
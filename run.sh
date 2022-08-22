docker compose build;
docker compose up -d;
docker exec -w /srv/www/Somnium -t somniumtest-python-1 sh run.sh

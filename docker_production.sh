apt update
apt upgrade -y
apt autoremove -y
apt install -y docker.io docker-compose supervisor npm python3
reboot

cp .env.production .env
source .env

npm install

docker-compose -f production.yml build
docker-compose -f production.yml up -d

docker-compose -f production.yml run --rm django python manage.py migrate
docker-compose -f production.yml run --rm django python manage.py createsuperuser

cp supervisor_production.cfg /etc/supervisor/conf.d/krv-je-zivot.conf
supervisorctl reread
supervisorctl start krv-je-zivot

apt update
apt upgrade -y
apt autoremove -y
apt install -y docker.io supervisor npm
reboot

apt install -y build-essential libbz2-dev libssl-dev libreadline-dev libsqlite3-dev tk-dev
apt install -y libpng-dev libfreetype6-dev

bash utility/install_os_dependencies.sh install

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

pyenv install 3.6.5
pyenv virtualenv 3.6.5 gvenv
pyenv global gvenv
pip install virtualenv pipenv

docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=pwd --name=postgres96 postgres:9.6
docker run -d -p 6379:6379 --name=redis30 redis:3.0

bash utility/install_python_dependencies.sh install

npm install
python manage.py collectstatic

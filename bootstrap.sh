
#Set Timezone
echo "America/Sao_Paulo" | sudo tee /etc/timezone
apt-get update

#Install Pip
sudo apt-get install python-pip

#Setup Virtual Env.
sudo pip install virtualenv
virtualenv .

#Active Virtual Env
source bin/activate

#Install Django
pip install django
cd /opt
sudo git clone https://github.com/cowrie/cowrie.git
sudo chown -R ubuntu:ubuntu cowrie
cd cowrie
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

cp etc/cowrie.cfg.dist etc/cowrie.cfg
nano etc/cowrie.cfg   # Customize port, banner, etc.
bin/cowrie start

#logs stored at var/log/cowrie.log & var/log/cowrie/json

#Run the following to aid in hardening Admin SSH

sudo nano /etc/ssh/sshd_config
- Change SSH port to 22222

sudo systemctl restart ssh 


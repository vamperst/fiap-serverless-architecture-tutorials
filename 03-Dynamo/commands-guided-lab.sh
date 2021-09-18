cd ~/environment/fiap-serverless-architecture-tutorials/03-Dynamo

sudo apt-get install python3-pip
sudo pip3 install virtualenv 


virtualenv ~/venv 
source ~/venv/bin/activate

python3 dynamo-PK-1.py

python3 dynamo-PK-2.py

python3 dynamo-SK-1.py

python3 dynamo-SK-2.py

python3 dynamo-SK-3.py

python3 dynamo-SK-4.py

python3 dynamo-LCI-1.py

python3 dynamo-LCI-2.py

python3 dynamo-GSI-1.py

python3 dynamo-GSI-2.py

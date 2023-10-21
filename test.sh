python3.11 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py test
deactivate
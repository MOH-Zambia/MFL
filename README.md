# MFL
Master Facility List for Ministry of Health Zambia

To run this application you need to have python 3.5 https://www.python.org installed on your machine.

# Installation

## Ubuntu 18.04 
```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install python3 virtualenv -y

cd /var/lib
```
### Postgresql installation
```bash
sudo apt install postgresql-10 postgresql-common postgresql-server-dev-10 postgresql-10-postgis-2.4 -y
```
```bash 
sudo git clone https://github.com/MOH-Zambia/MFL
```
```bash
cd MFL
```

```bash 
sudo virtualenv -p python3 .
```
```bash 
source bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py runserver
```

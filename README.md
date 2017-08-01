# agenvida

Requirements

      Python 3.6
      Django 1.11

Installation

      You need to install python3

      sudo apt-get install python3 -y
      Virtualenv is optional but strongly suggested

      git clone https://github.com/lcmencia/agenvida.git
      cd agenvida
      virtualenv env -p python3
      source env/bin/activate
      pip install -r requirements.txt

Usage

      ./manage.py migrate
      ./manage.py createsuperuser
      ./manage.py makemigrations capitalario
      ./manage.py migrate capitalario
      ./manage.py runserver localhost:5000
